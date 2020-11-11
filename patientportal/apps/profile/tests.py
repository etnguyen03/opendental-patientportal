from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TestDash(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test@example.com", email="test@example.com", password="topsecret"
        )

    def test_profile_view(self):
        response = self.client.get(reverse("profile"))
        self.assertEqual(302, response.status_code)

        self.client.login(username="test@example.com", password="topsecret")
        response = self.client.get(reverse("profile"))
        self.assertEqual(200, response.status_code)
