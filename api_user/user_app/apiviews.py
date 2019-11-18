from rest_framework import viewsets, filters
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from .serializers import *
from .models import *

class ProfileViewSet(viewsets.ModelViewSet):
    # filter_backends = (DynamicSearchFilter,)
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializer