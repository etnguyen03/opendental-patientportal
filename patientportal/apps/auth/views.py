from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('/')