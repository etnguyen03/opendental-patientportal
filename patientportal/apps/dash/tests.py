# Copyright (c) 2020 Ethan Nguyen. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TestDash(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test@example.com", email="test@example.com", password="topsecret"
        )

    def test_dash_view(self):
        response = self.client.get(reverse("dash"))
        self.assertEqual(302, response.status_code)

        self.client.login(username="test@example.com", password="topsecret")
        response = self.client.get(reverse("dash"))
        self.assertEqual(200, response.status_code)
