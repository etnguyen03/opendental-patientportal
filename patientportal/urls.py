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

"""patientportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin as django_admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls

from patientportal.apps.administration import urls as administration_urls
from patientportal.apps.auth.views import logout_view
from patientportal.apps.dash.views import dash_view
from patientportal.apps.profile.views import CustomPasswordChangeView, profile_view

django_admin.autodiscover()

urlpatterns = [
    path("administration/", include(administration_urls)),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path(
        "profile/chpasswd",
        CustomPasswordChangeView.as_view(template_name="pwchange.html"),
        name="password_change",
    ),
    path("", dash_view, name="dash"),
    url(r"", include(tf_urls)),
    url(r"", include("user_sessions.urls", "user_sessions")),
    path("djangoadmin/", django_admin.site.urls),
]
