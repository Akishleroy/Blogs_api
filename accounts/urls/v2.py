from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSetV2, basename='accounts-v2')
router.register(r'wallets', views.WalletViewSet, basename='wallets-v2')

urlpatterns = router.urls
