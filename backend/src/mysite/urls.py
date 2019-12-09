from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="DAB API Endpoints",
        default_version=f"{settings.API_VERSION}",
        description="API endpoints for DAB backend application",
        terms_of_service="",
        contact=openapi.Contact(email="rezwanul.cse@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('examples/', include('example.urls')),
    path('admin/', admin.site.urls),
    path(
        f"api/{settings.API_VERSION}/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('flights/', include('flights.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
