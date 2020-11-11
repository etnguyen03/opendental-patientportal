from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy

from patientportal.apps.users.models import Patient


@login_required
def profile_view(request):
    patient_list = Patient.objects.filter(user=request.user)
    context = {
        "email": request.user.username,
        "patient_list": patient_list,
    }
    return render(request, "profile.html", context)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)
