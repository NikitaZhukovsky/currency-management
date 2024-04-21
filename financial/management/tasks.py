from celery import shared_task
import requests
from management.models import ExchangesRate, Currency


@shared_task()
def add_to_db():
    data = requests.get('https://api.nbrb.by/exrates/rates?periodicity=0')
    currency_mappings = {
        431: 'USD',
        451: 'EUR',
        456: 'RUB'
    }
    currency_bun = Currency.objects.filter(name='BYN').first()

    for item in data.json():
        cur_id = item['Cur_ID']
        if cur_id in currency_mappings:
            currency_abbreviation = currency_mappings[cur_id]
            currency = Currency.objects.filter(name=currency_abbreviation).first()
            ExchangesRate.objects.create(currency_from=currency, to_currency=currency_bun,
                                         exchange_rate=item['Cur_OfficialRate'])
    return 'The recording was successful'


