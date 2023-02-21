from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from accounts import services, models, filters, serializer
from src import pagination


class WalletViewSet(ModelViewSet):
    queryset = models.Wallet.objects.select_related('account')
    serializer_class = serializer.WalletSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.WalletFilter


class AccountViewSet(ModelViewSet):
    account_services = services.AccountServicesV1()

    pagination_class = pagination.CustomPageNumberPagintion
    # queryset = account_services.get_accounts()

    # serializer_class = serializer.CreateAccountSerializer

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return serializer.RetrieveAccountSerializer

        return serializer.CreateAccountSerializer

    def get_queryset(self):
        return self.account_services.get_accounts(action=self.action)

    def perform_create(self, serializer: serializer.CreateAccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)


class AccountViewSetV2(ModelViewSet):
    account_services = services.AccountServicesV1()
    # queryset = account_services.get_accounts()
    serializer_class = serializer.RetrieveAccountSerializer

    def get_queryset(self):
        return self.account_services.get_accounts()

    def perform_create(self, serializer: serializer.CreateAccountSerializer):
        self.account_services.create_account(data=serializer.validated_data)
