from drf_yasg import openapi


params = [
    openapi.Parameter('search', openapi.IN_QUERY, description="search", type=openapi.TYPE_STRING),
]