from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TestAuth(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test@example.com", email="test@example.com", password="topsecret"
        )

    def test_logout(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(302, response.status_code)

        self.client.login(username="test@example.com", password="topsecret")
        response = self.client.get(reverse("logout"))
        self.assertEqual(302, response.status_code)

        # Check for successful logout
        response = self.client.get(reverse("dash"))
        self.assertEqual(302, response.status_code)
