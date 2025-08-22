from django.core.management.base import BaseCommand
from django.utils.text import slugify
from blog.models import Post

class Command(BaseCommand):
    help = "Generate unique slugs for blog posts without a slug"

    def generate_unique_slug(self, title, existing_slugs):
        """Generate a unique slug for a post title."""
        base_slug = slugify(title)
        slug = base_slug
        num = 1

        # Ensure uniqueness
        while slug in existing_slugs:
            slug = f"{base_slug}-{num}"
            num += 1

        existing_slugs.add(slug)  # Mark as used
        return slug

    def handle(self, *args, **kwargs):
        posts = Post.objects.filter(slug__isnull=True).order_by("id")
        if not posts.exists():
            self.stdout.write(self.style.WARNING("No posts needed slug generation."))
            return

        # Collect existing slugs to minimize queries
        existing_slugs = set(Post.objects.values_list("slug", flat=True).exclude(slug__isnull=True))

        updated_posts = []
        for post in posts:
            post.slug = self.generate_unique_slug(post.title, existing_slugs)
            updated_posts.append(post)
            self.stdout.write(self.style.SUCCESS(f"Slug '{post.slug}' generated for post '{post.title}'"))

        # Bulk update instead of saving one by one
        Post.objects.bulk_update(updated_posts, ["slug"])

        self.stdout.write(self.style.SUCCESS(f"✅ Slugs generated for {len(updated_posts)} post(s)."))
