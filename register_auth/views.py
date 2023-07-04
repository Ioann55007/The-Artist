from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from coreapi.compat import force_text


from .forms import UserLoginForm, UserSetNewPasswordForm, UserForgotPasswordForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token

from django.contrib.auth.models import User
from django.core.mail import EmailMessage




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Пожалуйста перейдите по ссылке и завершите регистрацию'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Ссылка активации была отправлена на вашу электронную почту')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})



def activate(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Спасибо за регистрацию. Сейчас вы можете войти на сайт и зайти  в аккаунт')
    else:
        return HttpResponse('Activation link is invalid!')








class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """

    Представление по сбросу пароля по почте

    """

    form_class = UserForgotPasswordForm



    template_name = 'registration/user_password_reset.html'

    success_url = reverse_lazy('first')

    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'

    # subject_template_name = 'password_subject_reset_mail.txt'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """

    Представление установки нового пароля

    """

    form_class = UserSetNewPasswordForm

    template_name = 'registration/user_password_set_new.html'

    success_url = reverse_lazy('first')

    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Установить новый пароль'

        return context


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('first')
    else:
        form = UserLoginForm
    return render(request, 'registration/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')
