
from rest_framework.routers import DefaultRouter
from .apiviews import *
from .apiviews import *
from django.urls import path , re_path
from . import views
router = DefaultRouter()
router.register('user',ProfileViewSet, base_name='user')
urlpatterns = [
    ###
]


urlpatterns += router.urls