from django.views import View
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .utils import confirm_email


class Registration(FormView):
    template_name = 'users/registration.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('confirm_email')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            confirm_email(self.request, user)
        return super(Registration, self).form_valid(form)


class VerifyEmail(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and default_token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('task_list')
        return redirect('invalid_verification')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, ValidationError):
            user = None
        return user


class Login(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task_list')


class UpdateProfile(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'birth_date', 'gender']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('task_list')
