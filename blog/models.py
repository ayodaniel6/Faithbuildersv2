from django.db import models
from django.conf import settings

# All posts to be tagged with keywords
from taggit.managers import TaggableManager
from django.utils.text import slugify
from datetime import timedelta
from django.utils import timezone


def extract_keywords(text, num_keywords=5):
    # keyword extraction tool for tagging and categorizing content with heavy ML
    from keybert import KeyBERT
    # Avoid declaring it globally, only load when needed
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 1),
        stop_words='english',
        top_n=num_keywords
    )
    return [kw[0] for kw in keywords]

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    file = models.FileField(upload_to='blog/files/', blank=True, null=True)
    audio = models.FileField(upload_to='blog/files/', blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmarked_posts', blank=True)
    slug = models.SlugField(unique=True, blank=True)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube or external video link")

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def comment_count(self):
        return self.comments.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate slug if not set

        super().save(*args, **kwargs)

        # Auto-generate tags only if none were manually added
        if not self.tags.exists():
            full_text = f"{self.title} {self.content}"
            keywords = extract_keywords(full_text)
            self.tags.set(keywords)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    @property
    def is_new(self):
        return self.date_published >= timezone.now() - timedelta(hours=24)


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarks')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookmarked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.user.username}: {self.message}"

