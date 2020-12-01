from learn_django import settings
from django.urls import reverse


def access(request):
    site = request.site
    site_configuration = site.siteconfigration
    timezone = request.user.profile.timezone
    return {'base_usl': settings.BASE_URL, 'trips_dashboard_url': '', 'platform_name': site.name,
            'add_trip_url': reverse('AddTrip'), 'timezone': timezone}

