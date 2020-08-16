from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dash_view(request):
    context = {
        "first_name": request.user.first_name,
    }
    return render(request, "dash.html", context)
