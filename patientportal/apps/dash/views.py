from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def dash_view(request):
    context = {
        "first_name": request.user.first_name,
    }
    return render(request, "dash.html", context)
