from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse
from django.test import TestCase

import re


class TestAdministration(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test@example.com", email="test@example.com",
                                                         password="topsecret")
        self.superuser = get_user_model().objects.create_user(username="admin@example.com", email="admin@example.com",
                                                              password="topsecret123")
        self.superuser.is_superuser = True
        self.superuser.is_staff = True
        self.superuser.save()

    def test_reset_password(self):
        # POST to the reset password page
        self.client.login(username="admin@example.com", password="topsecret123")
        response = self.client.post(reverse("administration:resetpw", kwargs={"user": self.user.username}),
                                    {"checkbox": True})
        self.assertIsNone(authenticate(username=self.user.username, password="topsecret"))

        # Attempt to extract the new password and log in
        new_password = re.search('(?<=id="password">).*(?=</span)', str(response.content))
        self.assertIsNotNone(authenticate(username=self.user.username, password=new_password.group(0)))

        # Assert that the username printed is the given username
        new_username = re.search('(?<=id="email">)[A-z0-9.@+]*(?=</span)', str(response.content))
        self.assertEqual(self.user.username, new_username.group(0))

    def test_reset_password_invalid(self):
        self.client.login(username="admin@example.com", password="topsecret123")
        self.client.post(reverse("administration:resetpw", kwargs={"user": self.user.username}), {"checkbox": False})
        self.assertIsNotNone(authenticate(username=self.user.username, password="topsecret"))

    def test_manage_user_loader_view(self):
        response = self.client.post(reverse("administration:manageuser-loader"), {"email": self.user.username})
        self.assertEqual(302, response.status_code)
        self.assertIn("login", response.url)

        self.client.login(username="admin@example.com", password="topsecret123")
        response = self.client.post(reverse("administration:manageuser-loader"), {"email": self.user.username})
        self.assertEqual(302, response.status_code)
        self.assertIn(self.user.username, response.url)

    def test_manage_user_view(self):
        response = self.client.get(reverse("administration:manageuser", kwargs={"user": self.user.username}))
        self.assertEqual(302, response.status_code)
        self.assertIn("login", response.url)

        self.client.login(username="admin@example.com", password="topsecret123")
        response = self.client.get(reverse("administration:manageuser", kwargs={"user": self.user.username}))
        self.assertIn(self.user.username, str(response.content))

        response = self.client.get(reverse("administration:manageuser", kwargs={"user": "doesntexist@example.com"}))
        self.assertEqual(404, response.status_code)
