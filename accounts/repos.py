from decimal import Decimal
from typing import Protocol, OrderedDict

from django.db import transaction
from django.db.models import QuerySet, Q, F, Sum, Avg, Case, DecimalField, When, Value
from accounts import constants, models
from accounts.constants import AmountCurrencyChoices

from accounts.models import Account


class AccountsReposInterface(Protocol):

    @staticmethod
    def get_accounts(action: str) -> QuerySet[Account]: ...

    @staticmethod
    def create_account(data: OrderedDict) -> None: ...


class AccountReposV1:

    @staticmethod
    def get_accounts(action: str) -> QuerySet[Account]:
        accounts = models.Account.objects.all()

        if action not in ('list', 'retrieve'):
            return accounts
        return accounts.prefetch_related('wallets').annotate(
            total_amount=Sum(
                'wallets__amount',
                filter=Q(wallets__amount_currency=AmountCurrencyChoices.KZT)
            ),
            avg_amount=Avg(
                'wallets__amount',
                filter=Q(wallets__amount_currency__in=(AmountCurrencyChoices.KZT, AmountCurrencyChoices.USD))
            ),
            custom_amount=Sum(
                Case(
                    When(Q(wallets__amount_currency=AmountCurrencyChoices.KZT), then=F("wallets__amount") * 2),
                    When(Q(wallets__amount_currency=AmountCurrencyChoices.RUB), then=F("wallets__amount") * 3),
                    When(Q(wallets__amount_currency=AmountCurrencyChoices.USD), then=F("wallets__amount") * 6),
                    default=Value(Decimal(0.0)),
                    output_field=DecimalField()
                )
            )
        )

    @staticmethod
    def create_account(data: OrderedDict) -> None:
        with transaction.atomic():
            wallets = data.pop('wallets')
            account = models.Account.objects.create(**data)
            raise AttributeError
            models.Wallet.objects.bulk_create([
                models.Wallet(**w, account=account) for w in wallets
            ])
