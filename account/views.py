from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, RegisterForm, EditeProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, logout
from .models import Profile


class Login(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse('account:profile'))


class Logout(LogoutView):
    pass


def profile(request):
    return render(request, 'account/profile.html')


def profile_edit(request):
    if request.method == 'POST':
        form = EditeProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:profile'))
    else:
        form = EditeProfile(instance=request.user.profile)
    return render(request,
                  'account/profile_edit.html',
                  {
                      'form': form
                  })
