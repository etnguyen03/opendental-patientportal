from django.conf import settings

def global_settings(request):
    return {
        "company_name": settings.COMPANY_NAME,
        "main_page_domain": settings.MAIN_PAGE_DOMAIN,
        "email": request.user.username if request.user is not None else None,
    }