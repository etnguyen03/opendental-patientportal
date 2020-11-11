from django.urls import path
from . import views

app_name = 'administration'
urlpatterns = [
    path('', views.administration_view, name="index"),
    path('newuser', views.create_new_user_view, name="newuser"),
    path('manage/<str:user>', views.manage_user_view, name="manageuser"),
    path('manage/', views.manage_user_loader_view, name="manageuser-loader"),
    path('manage/resetpw/<str:user>', views.reset_user_password, name="resetpw"),
    path('manage/disable2fa/<str:user>', views.disable_2fa, name="disable2fa"),
    path('manage/addpatient/<str:user>', views.add_patient_view, name="addpatient"),
]