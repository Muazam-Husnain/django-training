from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('trips', views.TripsView, 'trips-list')
router.register(r'trip', views.TripsView, 'trip-details')

urlpatterns = [
    url('api/v1/', include(router.urls)),
    url('^user/$', views.create_profile),
    url('profile/(?P<username>\w{0,50})', views.edit_profile),
    # url('users/<string:username>/', views.edit_profile, name='profile'),
    url('api_auth/', include('rest_framework.urls'))
]
