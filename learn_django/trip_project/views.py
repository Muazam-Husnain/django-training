from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from .forms import Create_User_Form, Create_Profile_Form, Edit_User_Form
from .models import Trip, Profile, TripsUser
from .serializers import TripSerializer
from .permissions import IsSuperUserOrStaff


class TripsView(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsSuperUserOrStaff]


def edit_profile(request, username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        user_form = Edit_User_Form(request.POST, instance=user)
        profile_form = Create_Profile_Form(request.POST, instance=profile)
        if user_form.is_valid() & profile_form.is_valid():
            user_form.save()
            profile_form.save()

    if request.user.is_authenticated:
        req_user = TripsUser.objects.get(pk=request.user.id)
        user = User.objects.get(username=username)
        if user == request.user or req_user.is_su_member():
            profile = Profile.objects.get(user=user)
            user_form = Edit_User_Form(instance=user)
            profile_form = Create_Profile_Form(instance=profile)
            return render(request, 'edit_user.html', {
                'profile_form': profile_form,
                'user_form': user_form,
            })
        else:
            return HttpResponse('Unauthorized', status=401)
    else:
        return HttpResponse('Unauthorized', status=401)

def create_profile(request):
    if request.method == 'POST':
        user_form = Create_User_Form(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            profile = Profile.objects.get(user=user)
            profile_form = Create_Profile_Form(request.POST, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
            else:
                messages.error(request, ('Correct information in Profile'))
        else:
            messages.error(request, ('Correct the information in User'))

    user_form = Create_User_Form(request.POST)
    profile_form = Create_Profile_Form(request.POST)
    return render(request, 'create_user.html', {
        'profile_form': profile_form,
        'user_form': user_form,
    })

