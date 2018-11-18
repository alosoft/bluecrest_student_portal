from django.urls import path
from django.conf.urls import url
from students import views
from django.contrib.auth import views as auth_views

# templates urls

app_name = 'students'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('change/', views.change, name='change'),
    # path('change-picture/', views.change_picture, name='change-profile')
    # path('change-password/', views.change_password, name='change_password'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')

]

# <int:pk>/
#
# urlpatterns = [
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
#
#     ,
# ]
