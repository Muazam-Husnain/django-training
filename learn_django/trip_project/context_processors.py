from learn_django import settings
from .models import Profile, SiteConfigration


def access_required_veriables(request):
    site = request.site
    site_configuration = SiteConfigration.objects.filter(site=site)
    timezone = Profile.objects.filter(user=request.user).values('timezone')
    return {'base_usl': settings.BASE_URL, 'trips_dashboard_url': '', 'platform_name': site.name,
            'add_trip_url': site_configuration.values('add_trip_url'), 'timezone': timezone}

