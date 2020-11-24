from .models import TripsUser

class ProcessUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request.trip_user = TripsUser.objects.get(pk=request.user.id)
        except TripsUser.DoesNotExist:
            request.trip_user = None
        response = self.get_response(request)

        return response

