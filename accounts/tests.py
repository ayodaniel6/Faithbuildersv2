from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AccountsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com',
            password='TestPass123!',
            first_name='Test'
        )

    def test_user_registration(self):
        response = self.client.post(reverse('accounts:signup'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'Newpass123!',
            'password2': 'Newpass123!',
            'first_name': 'New'
        })
        self.assertEqual(response.status_code, 302)  # should redirect after sign up
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'testuser',
            'password': 'TestPass123!'
        })
        self.assertEqual(response.status_code, 302)  # should redirect after login
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_profile_dashboard_access(self):
        self.client.login(username='testuser', password='TestPass123!')
        response = self.client.get(reverse('accounts:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')  # checks if first_name is shown

    def test_logout(self):
        self.client.login(username='testuser', password='TestPass123!')
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)
