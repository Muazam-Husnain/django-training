from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('trips', views.TripsView, 'trips-list')
router.register(r'trip', views.TripsView, 'trip-details')

urlpatterns = [
    url('api/v1/', include(router.urls)),
    url(r'^trips$', views.index, name='index')
]