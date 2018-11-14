from django.urls import path
from students import views

# templates urls

app_name = 'students'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login')
]