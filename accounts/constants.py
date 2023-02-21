from django.db import models


class AmountCurrencyChoices(models.TextChoices):
    RUB = "rub", "руб",
    KZT = "kzt", "тенге",
    USD = "usd", "доллары",
