from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'service', ServiceViewSet, base_name='service')
router.register(r'order', OrderViewSet, base_name='order')
urlpatterns = [
    url(r'^create_order', CreateOrder.as_view()),
]
urlpatterns += router.urls
