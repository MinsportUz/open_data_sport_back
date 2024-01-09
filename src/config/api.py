from django.urls import path

from app import views as app_views
from sport import views as sport_views
from utils import views as utils_views

urlpatterns = [
    path('lockout/', app_views.lockout_view, name='lockout_url'),
]