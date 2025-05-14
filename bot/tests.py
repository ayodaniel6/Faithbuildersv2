from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from bot.models import CounselorRequest
from blog.models import Post

# Create your tests here.

class BotAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='botuser', password='botpass123')
        self.request_url = reverse('bot:request')
        self.ask_url = reverse('bot:ask')

        # Sample blog post
        self.post = Post.objects.create(
            title="Django Testing Guide",
            content="This post is about how to write tests in Django.",
            author=self.user,
            is_draft=False
        )

    def test_redirect_if_not_logged_in_for_request(self):
        response = self.client.get(self.request_url)
        self.assertRedirects(response, f"/accounts/login/?next={self.request_url}")

    def test_logged_in_user_can_access_request_form(self):
        self.client.login(username='botuser', password='botpass123')
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Request a Counsellor")

    def test_counselor_request_submission(self):
        self.client.login(username='botuser', password='botpass123')
        data = {
            'email': 'botuser@example.com',
            'message': 'I need help with anxiety.'
        }
        response = self.client.post(self.request_url, data)
        self.assertRedirects(response, reverse('accounts:dashboard'))
        self.assertTrue(CounselorRequest.objects.filter(user=self.user).exists())

    def test_bot_responds_to_known_question(self):
        self.client.login(username='botuser', password='botpass123')
        response = self.client.post(self.ask_url, {'message': 'django'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Django Testing Guide", response.json().get("response"))

    def test_bot_fallback_for_unknown_question(self):
        self.client.login(username='botuser', password='botpass123')
        response = self.client.post(self.ask_url, {'message': 'What is the capital of Mars?'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("I didn't understand", response.json().get("response"))
