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
from django.urls import path, include

from two_factor.urls import urlpatterns as tf_urls
from patientportal.apps.dash.views import dash_view
from patientportal.apps.profile.views import profile_view, CustomPasswordChangeView
from patientportal.apps.admin.views import admin_view
from patientportal.apps.auth.views import logout_view

django_admin.autodiscover()

urlpatterns = [
    path('djangoadmin/', django_admin.site.urls),
    path('admin/', admin_view),
    path('logout/', logout_view),
    path('profile/', profile_view, name="profile"),
    path('profile/chpasswd', CustomPasswordChangeView.as_view(template_name="pwchange.html"), name="password_change"),
    path('', dash_view),
    url(r'', include(tf_urls)),
    url(r'', include('user_sessions.urls', 'user_sessions')),
]
