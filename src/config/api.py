from django.urls import path, include
from rest_framework import routers

from app import views as app_views
from sport import views as sport_views
from utils import views as utils_views

api = routers.DefaultRouter()

# utils urls
api.register(r'state', utils_views.StateView, basename='state')

urlpatterns = [
    path('', include(api.urls)),
    path('lockout/', app_views.lockout_view, name='lockout_url'),
]
