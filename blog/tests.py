from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.post = Post.objects.create(title="Test Post", content="Content here", author=self.user)
        self.comment_url = reverse('blog:add_comment', args=[self.post.id])
        self.like_url = reverse('blog:like_post', args=[self.post.id])
        self.bookmark_url = reverse('blog:toggle_bookmark', args=[self.post.id])

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.content)

    def test_add_comment_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.post(self.comment_url, {'content': 'Nice post!'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)

    def test_add_comment_unauthenticated(self):
        response = self.client.post(self.comment_url, {'content': 'Nice post!'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 403)  # Should block unauthenticated comment

    def test_like_post_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.post(self.like_url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.user in self.post.likes.all())

    def test_bookmark_post_authenticated(self):
        self.client.login(username="testuser", password="pass1234")
        response = self.client.post(self.bookmark_url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.user in self.post.bookmarks.all())

    def test_like_post_unauthenticated(self):
        response = self.client.post(self.like_url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 403)

    def test_bookmark_post_unauthenticated(self):
        response = self.client.post(self.bookmark_url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 403)
