from django.contrib import admin
from django.urls import path, include
from mercado.views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
