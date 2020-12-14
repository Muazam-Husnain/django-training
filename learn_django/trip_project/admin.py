from django.contrib import admin
from .models import Trip, Itenrary, Host, Location, Profile, SiteConfigration, TripSchedule
admin.site.register(Trip)
admin.site.register(Itenrary)
admin.site.register(Host)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(SiteConfigration)
admin.site.register(TripSchedule)

class TripAdmin(admin.ModelAdmin):
    model = Trip
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


