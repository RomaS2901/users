from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import MyAuthenticationForm, MyUserChangeForm, MyUserCreationForm


def index(request):
    return render(request, 'index.html')


def users_list(request):
    return render(request, 'users_app/users.html', context={
        'users': get_user_model().objects.all(),
        'user_create_form': MyUserCreationForm(),
        'user_update_form': MyUserChangeForm()
    })


def create_user(request):
    create_user_form = MyUserCreationForm(request.POST)
    if create_user_form.is_valid():
        create_user_form.save()
        return redirect('users-list')
    return render(request, 'users_app/users.html', context={
        'users': get_user_model().objects.all(),
        'user_create_form': create_user_form,
        'user_update_form': MyUserChangeForm()
    })


def update_user(request):
    """ As we want to update any User from this view, we should get each user dynamic """
    user_obj = get_user_model().objects.get(username=request.POST.get('username'))
    update_user_form = MyUserChangeForm(request.POST, instance=user_obj)
    if update_user_form.is_valid():
        update_user_form.save()
        return redirect('users-list')
    return render(request, 'users_app/users.html', context={
        'users': get_user_model().objects.all(),
        'user_create_form': MyUserCreationForm(),
        'user_update_form': update_user_form
    })


def delete_user(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    user.delete()
    return redirect('users-list')


class LogIn(UserPassesTestMixin, View):

    def test_func(self):
        return not self.request.user.is_authenticated

    def get(self, request):
        auth_form = MyAuthenticationForm()
        return render(request, 'users_app/login.html', context={'auth_form': auth_form})

    def post(self, request):
        auth_form = MyAuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('loggedin')
            return render(request, 'users_app/login.html', context={'auth_form': auth_form})
        return render(request, 'users_app/login.html', context={'auth_form': auth_form})


def logout_view(request):
    logout(request)
    return redirect('login')


def logged_in_view(request):
    return render(request, 'users_app/loggedin.html')
