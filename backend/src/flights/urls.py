from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from . import views

app_name = "flights"
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path("", views.index, name='index')
    # path("", include(router.urls))
    path('', views.flight_list, name='flight-list'),
    path('<int:pk>', views.flight_detail, name='flight-detail')
]