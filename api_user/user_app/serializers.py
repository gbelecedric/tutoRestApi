from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class UserListingField(serializers.RelatedField):
    def to_representation(self, value):
        
        
        data ={'username': value.username,
                'email': value.email,
                'id': value.id
               
        }
        
                
               
               
        #duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return data  

class ProfileSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user = UserListingField( read_only=True,required=False)
    
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1