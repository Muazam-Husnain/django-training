from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'trips/booking', views.BookingsView, 'bookings-list')
router.register('trips', views.TripsView, 'trips-list')
router.register(r'trip', views.TripsView, 'trip-details')

urlpatterns = [
    url('api/v1/trip/(?P<id>[0-9]+)/booking', views.TripBooking.as_view({'get': 'list'})),
    url('api/v1/', include(router.urls)),
    url('^user/$', views.create_profile),
    url('profile/(?P<username>\w{0,50})', views.edit_profile),
    # url('users/<string:username>/', views.edit_profile, name='profile'),
    url('api_auth/', include('rest_framework.urls')),
    url('add_trip', views.add_trip, name='AddTrip')
]
