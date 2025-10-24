from rest_framework.routers import DefaultRouter
from miniDataview.api.views import *

router = DefaultRouter()

router.register(r'logs', LogViewSet, basename="log")

urlpatterns = router.urls