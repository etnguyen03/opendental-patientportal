from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy


def profile_view(request):
    context = {
        "email": request.user.username,
    }
    return render(request, "profile.html", context)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)
