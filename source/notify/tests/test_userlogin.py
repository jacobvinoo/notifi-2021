from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

LOGIN_URL = reverse('login')


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email='test@test.co.nz',
            password='password123',
            name='Test User'
        )

    def test_user_with_credentials_logged_in(self):
        """Test whether an existing user can login in"""

        payload = {
            'username': 'test@test.co.nz',
            'password': 'password123'
        }
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'dashboard.html')

    def test_user_with_wrong_password_does_not_login(self):
        """Test that user with a wrong password cannot login"""

        payload = {
            'username': 'test@test.co.nz',
            'password': 'wrongpassword'
        }
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'login.html')

    def test_user_without_credentials_fail_to_login(self):
        """Test that a user with in valid credentials does not login"""

        payload = {
            'username': 'fake@fake.com',
            'password': 'wrongpassword'
        }
        res = self.client.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'login.html')
