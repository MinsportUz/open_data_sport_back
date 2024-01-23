from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication  # Import authentication classes needed
from rest_framework_simplejwt.authentication import JWTAuthentication  # Import JWT Authentication if you're using it
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="darslik.sport.uz Api",
        default_version='v1',
        description="darslik.sport.uz Api documentations",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="haydarovakbar640@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # patterns=[path('api/', include('myapi.urls')), ],
    url=settings.HOST,
    authentication_classes=(TokenAuthentication, JWTAuthentication),
)
