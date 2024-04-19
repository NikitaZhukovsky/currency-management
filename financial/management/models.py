from django.db import models
from users.models import CustomUser


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Currencies'


class ExchangesRate(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    currency_from = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_from')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_currency')
    exchange_rate = models.DecimalField(max_digits=5, decimal_places=3)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Exchanges Rates'


class Subscription(models.Model):
    NOTIF = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)

    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    notification = models.PositiveIntegerField(choices=NOTIF, default=1)
    is_paid = models.BooleanField(default=False)
