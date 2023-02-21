from rest_framework import serializers
from accounts import models


class _WalletAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'first_name', 'last_name')


class WalletSerializer(serializers.ModelSerializer):
    account = _WalletAccountSerializer(read_only=True)
    pagination_class=None

    class Meta:
        model = models.Wallet
        fields = "__all__"


class _WalletSerializer(serializers.ModelSerializer):
    # account = AccountSerializer(read_only=True, allow_null=True)

    class Meta:
        model = models.Wallet
        fields = (
            'amount',
            'amount_currency'
        )


class CreateAccountSerializer(serializers.ModelSerializer):
    # total_amount = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=4)
    # avg_amount = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=4)
    # custom_amount = serializers.DecimalField(read_only=True, max_digits=14, decimal_places=4)
    wallets = _WalletSerializer(write_only=True, many=True)

    class Meta:
        model = models.Account
        fields = "__all__"


class RetrieveAccountSerializer(serializers.ModelSerializer):
    wallets = _WalletSerializer(read_only=True, many=True)

    class Meta:
        model = models.Account
        fields = "__all__"
