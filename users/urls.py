from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import Login, Registration, VerifyEmail


urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', VerifyEmail.as_view(), name='verify_email'),
    path('invalid_verification/', TemplateView.as_view(template_name='users/invalid_verification.html'),
         name='invalid_verification'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
