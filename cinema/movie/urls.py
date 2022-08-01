from django.urls import path
from .views import *


urlpatterns = [
    path('single/', get_single),
    path('', Home.as_view(), name='home')
]