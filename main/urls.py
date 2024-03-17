from django.urls import path
from .views import *

urlpatterns = [
    path('', profile),
    path('login/', login),
]
