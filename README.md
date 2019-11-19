# installation

```python
pip install Django
pip install djangorestframework
#-----pour la recherche dinamic---#
pip install drf-dynamic-fields

```
### dans le seetings :
```python
INSTALLED_APPS = (
...
'rest_framework',

)

```
### creation des fichier 
```python
apiviews.py
serializers.py

```
### dans le fichier serializers 
```python
from rest_framework import serializers

from .models import *

# sans la recherche dinamic

class modelSerializer(serializers.ModelSerializer):
    class Meta:
        model = model
        fields = '__all__'
         depth = 2   ## pour percé encore plus 
# avec la recherche dinamic

from drf_dynamic_fields import DynamicFieldsMixin

class modelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = model
        fields = '__all__'

```


### apiview 

```python
from rest_framework import viewsets, filters
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from .serializers import *
from .models import *

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class ProfileViewSet(viewsets.ModelViewSet):
    # filter_backends = (DynamicSearchFilter,)
    queryset = Profile.objects.all()
    serializer_class =  ProfileSerializer
   
```

### urls 
```python
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
```
