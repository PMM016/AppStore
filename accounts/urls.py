from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    # Login
    path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    ), name="login"),

    # Logout
    path("logout/", auth_views.LogoutView.as_view(next_page="accounts:login"), name="logout"),

    # Password reset
    path("reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html",
        email_template_name="accounts/password_reset_email.html",
        subject_template_name="accounts/password_reset_subject.txt",
        success_url="/accounts/reset/done/"
    ), name="password_reset"),

    path("reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html",
        success_url="/accounts/reset/complete/"
    ), name="password_reset_confirm"),

    path("reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),

    # View account
    path("view/", views.view_account, name="view_account"),
]
