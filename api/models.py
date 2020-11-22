from django.db import models
from tastypie.resources import ModelResource
from products.models import Products

class ProductResource(ModelResource):
    class Meta:
        queryset = Products.objects.all();
        resource_name = 'products'