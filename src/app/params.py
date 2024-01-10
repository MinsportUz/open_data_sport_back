from drf_yasg import openapi


params = [
    openapi.Parameter('title', openapi.IN_QUERY, description="title", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('author', openapi.IN_QUERY, description="author", type=openapi.TYPE_STRING, required=True),
]