from django.core.management.base import BaseCommand
from django.utils.text import slugify
from blog.models import Post

class Command(BaseCommand):
    help = 'Generate unique slugs for blog posts without a slug'

    def handle(self, *args, **kwargs):
        count = 0
        for post in Post.objects.filter(slug__isnull=True).order_by('id'):
            base_slug = slugify(post.title)
            slug = base_slug
            num = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            post.slug = slug
            post.save()
            count += 1
            self.stdout.write(self.style.SUCCESS(f"Slug '{slug}' generated for post '{post.title}'"))

        if count == 0:
            self.stdout.write(self.style.WARNING("No posts needed slug generation."))
        else:
            self.stdout.write(self.style.SUCCESS(f"✅ Slugs generated for {count} post(s)."))
