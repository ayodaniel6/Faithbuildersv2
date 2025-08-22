from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Post, Comment
from random import choice, randint
from faker import Faker

fake = Faker()
User = get_user_model()  # ✅ Use your CustomUser model

class Command(BaseCommand):
    help = 'Generate dummy posts, comments, likes, and bookmarks based on users'

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        if not users:
            for i in range(5):
                users.append(
                    User.objects.create_user(
                        username=f"user{i}",
                        email=f"user{i}@example.com",   # ✅ email required
                        password="password123"
                    )
                )

        for user in users:
            # Each user creates between 1–5 posts
            for _ in range(randint(1, 5)):
                post = Post.objects.create(
                    title=fake.sentence(),
                    content=fake.paragraph(nb_sentences=8),
                    author=user,
                    is_draft=False,
                )

                # Likes (random users liking this post, excluding the author)
                liked_users = {choice(users) for _ in range(randint(0, len(users)))}
                liked_users.discard(user)
                post.likes.set(liked_users)

                # Bookmarks (random users bookmarking this post, excluding the author)
                bookmarked_users = {choice(users) for _ in range(randint(0, len(users)))}
                bookmarked_users.discard(user)
                post.bookmarks.set(bookmarked_users)

                # Comments
                for _ in range(randint(0, 3)):
                    Comment.objects.create(
                        post=post,
                        user=choice(users),
                        content=fake.sentence()
                    )

                post.save()

                self.stdout.write(self.style.SUCCESS(
                    f'Post "{post.title}" created by {user.username}, '
                    f'liked by {len(post.likes.all())} users, '
                    f'bookmarked by {len(post.bookmarks.all())} users.'
                ))
