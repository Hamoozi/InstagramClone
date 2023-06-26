from django.urls import path
from . import views
#importing paths
urlpatterns = [
    path('', views.users, name='users')

]