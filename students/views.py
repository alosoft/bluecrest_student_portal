from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from students import models
from students.forms import (
    UserForm,
    UserProfileInfoForm,
    # PasswordChangeForm
    UserProfileChangeForm)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

# @login_required
# class Index(ListView):
#     model = models.Record
#     template_name = 'students/portal.html'

@login_required
def portal(request):
    data = models.Record.objects.all()

    record_list = {
        'record_list': data,
    }

    return render(request, 'students/portal.html', context=record_list)


def index(request):
    return render(request, 'students/index.html')


def register(request):

    print('route accessed')

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('form was valid')

            if request.POST.get('password') != request.POST.get('password2'):
                messages.error(request, 'Password fields do not match!')
                return HttpResponseRedirect("/")
                # raise forms.ValidationError(
                #     'Password fields do not match'
                # )

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            update_session_auth_hash(request, user)  # Important!

            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
            login(request, new_user)

            messages.info(request, f'Thank you for registering, You are now Logged In {new_user.username}')

            return HttpResponseRedirect("/portal")

            # registered = True

        else:
            messages.error(request, user_form.errors)
            print('form wasn\'t valid')
            print('form wasn\'t valid')
            print('form wasn\'t valid')
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'students/index.html', {
        # 'form'
        'user_form': user_form,
        'profile_form': profile_form,
        # 'registered': registered
    })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    print('accessed login page')
    print(request.POST)
    print(request.method)

    if request.method == 'POST':
        print('tried logging in')

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # messages.success(request, f'Welcome {user.username}')
                return HttpResponseRedirect(reverse('portal'))

            else:
                messages.error(request, 'Account not Active')
                return HttpResponseRedirect('Account not Active')

        else:
            messages.error(request, 'Incorrect login details, Try again or reset password')
            print('Login attempt failed')
            print(f'Username: {username} and password {password}')
            return redirect('/')
            # return HttpResponse('invalid login details supplied <a href="/students/login/">Go Back</a>')

    else:
        return render(request, 'students/index.html', {})


@login_required
def change(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        change_form = UserProfileChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileInfoForm(request.FILES, instance=request.user.userprofileinfo)
        print(request.POST.get('profile_semester'))
        print(request.POST.get('profile_program'))
        if change_form.is_valid() and profile_form.is_valid():
            change_form.save()

            new_profile = profile_form.save(commit=False)
            if 'profile_pic' in request.FILES:
                new_profile.profile_pic = request.FILES['profile_pic']
            new_profile.profile_semester = request.POST['profile_semester']
            new_profile.profile_program = request.POST['profile_program']
            new_profile.save()

            messages.success(request, 'Profile updated successfully')
            return redirect('/')
        else:
            messages.error(request, change_form.errors)
            messages.error(request, profile_form.errors)
            return HttpResponseRedirect('/students/change')
    change_form = UserProfileChangeForm(instance=request.user)
    profile_form = UserProfileInfoForm(instance=request.user.userprofileinfo)
    return render(request, 'students/index.html',
                  {'change_form': change_form, 'profile_form': profile_form, 'route': 'change'})
    # return render(request, 'students/change.html', {'change_form': change_form, 'picture_form': picture_form})


#
# def change_picture(request):
#     if request.method == 'POST':
#         picture_form = UserProfileInfoForm(request.FILES, instance=request.user.userprofileinfo)
#         if picture_form.is_valid():
#             picture_form.save()
#
#             messages.success(request, 'User Profile Picture changed successfully')
#             return redirect('/')
#         else:
#             messages.error(request, 'Error making changes')
#             return HttpResponseRedirect('/change')
#     picture_form = UserProfileInfoForm(instance=request.user.userprofileinfo)
#     return render(request, 'students/change-picture.html', {'form': picture_form})

def application_forms(request):
    return render(request, 'students/form.html')
