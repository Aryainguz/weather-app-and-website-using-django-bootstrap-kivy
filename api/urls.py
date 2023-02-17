from django.urls import path
from api import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index),
    path("first",views.index),
    path("article",views.article),
    path('loginUser',views.loginUser),
    path("group",views.group),
    path('logoutUser',views.logoutUser),
    path("register",views.RegisterUser),
    path("forgot",PasswordResetView.as_view(template_name='forgot.html')),
    path("password-reset-confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="reset_confirm_password.html"),name="password_reset_confirm"),
    path("password-reset-done/",PasswordResetDoneView.as_view(template_name="reset_password_done.html"),name="password_reset_done"),
    path("password-reset-complete/",PasswordResetCompleteView.as_view(template_name="password_reset_confirm.html"),name="password_reset_complete"),
    path("password-reset-complete/loginUser",views.loginUser),
]


