from django.contrib import admin
from django.urls import path, include
from api.models import ProductResource

product_resource = ProductResource()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('api/', include(product_resource.urls))
]
