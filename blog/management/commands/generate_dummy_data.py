from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post, Comment
from random import choice, randint
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy posts, comments, likes, bookmarks'

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        if not users:
            for i in range(5):
                users.append(User.objects.create_user(
                    username=f"user{i}", password="password123"))

        for _ in range(20):
            author = choice(users)
            post = Post.objects.create(
                title=fake.sentence(),
                content=fake.paragraph(nb_sentences=10),
                author=author,
                is_draft=False,
            )

            # Likes
            post.likes.set([choice(users) for _ in range(randint(0, len(users)))])
            post.save()

            # Comments
            for _ in range(randint(0, 3)):
                Comment.objects.create(
                    post=post,
                    user=choice(users),
                    content=fake.sentence()
                )

            # Bookmarks
            bookmarked_users = list({choice(users) for _ in range(randint(0, len(users)))})
            post.bookmarks.set(bookmarked_users)

        post.save()

        self.stdout.write(self.style.SUCCESS(
    f'Post "{post.title}" liked by {len(post.likes.all())} users, bookmarked by {len(post.bookmarks.all())} users.'
))

