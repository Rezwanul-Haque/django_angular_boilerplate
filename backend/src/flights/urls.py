from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path("", views.index, name='index')
    # path("", include(router.urls))
    url(r'^$', views.flight_list, name='flight-list'),
    url(r'^(?P<pk>[0-9]+)$', views.flight_detail, name='flight-detail')
]