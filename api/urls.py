
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ClientInfoViewSet, ClientPersDocViewSet,
                    ClientStateViewSet, PlatformRuleViewSet,
                    QualificationViewSet)

router = DefaultRouter()

router.register(r'client', ClientInfoViewSet)
router.register(r'client_pers_doc', ClientPersDocViewSet)
router.register(r'client_state', ClientStateViewSet)
router.register(r'platform_rules', PlatformRuleViewSet)
router.register(r'qualification', QualificationViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
]
