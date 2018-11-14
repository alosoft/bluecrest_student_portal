from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from students import models
from students.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


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
    registered = False

    print('route accessed')
    print('route accessed')
    print('route accessed')
    print(request.method)

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('form was valid')
            print('form was valid')
            print('form was valid')
            print('form was valid')
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print('form wasn\'t valid')
            print('form wasn\'t valid')
            print('form wasn\'t valid')
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'students/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
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
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account not Active')

        else:
            print('Login attempt failed')
            print(f'Username: {username} and password {password}')
            return HttpResponse('invalid login details supplied')

    else:
        return render(request, 'students/login.html', {})

# def index(request):
#     data = models.Record.objects.all()
#
#     form = forms.SearchForm()
#     # if request.method == 'GET':
#     data_query = request.GET.get('query', None)
#     print(data_query)
#     if data_query:
#         search_results = data.filter(
#             Q(program__icontains=data_query) |
#             Q(semester__icontains=data_query)
#         )
#         record_list = {
#             'record_list': search_results,
#         }
#         return render(request, 'students/index.html', context=record_list)
#
#     return render(request, 'students/index.html', {'form': form})
