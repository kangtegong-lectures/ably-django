from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.views import CompanyViewSet, ProductViewSet, ProductImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('company', CompanyViewSet)
router.register('product', ProductViewSet)
router.register('productimage', ProductImageViewSet)


urlpatterns =[
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)