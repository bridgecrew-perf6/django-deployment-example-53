from django.urls import path
from . import views


#Template URLS
app_name = 'myapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
