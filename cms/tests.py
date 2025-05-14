from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post

# Create your tests here.

class CMSTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = User.objects.create_user(username='author1', password='cms123')
        self.other_user = User.objects.create_user(username='otheruser', password='other123')

        self.post = Post.objects.create(
            title="Test CMS Post",
            content="Test content for CMS",
            author=self.author,
            is_draft=False
        )

        self.create_url = reverse('cms:create_post')
        self.edit_url = reverse('cms:edit_post', args=[self.post.pk])
        self.delete_url = reverse('cms:delete_post', args=[self.post.pk])

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.create_url)
        self.assertRedirects(response, f'/accounts/login/?next={self.create_url}')

    def test_author_can_create_post(self):
        self.client.login(username='author1', password='cms123')
        data = {
            'title': 'New CMS Post',
            'content': 'Content here',
            'is_draft': False,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful create
        self.assertTrue(Post.objects.filter(title='New CMS Post').exists())

    def test_author_can_edit_post(self):
        self.client.login(username='author1', password='cms123')
        response = self.client.post(self.edit_url, {'title': 'Updated Title', 'content': 'New content'})
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_non_author_cannot_edit_post(self):
        self.client.login(username='otheruser', password='other123')
        response = self.client.post(self.edit_url, {'title': 'Hacked Title', 'content': 'Hacked'})
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_author_can_delete_post(self):
        self.client.login(username='author1', password='cms123')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_non_author_cannot_delete_post(self):
        self.client.login(username='otheruser', password='other123')
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())
