from django.urls import path
from management.views import (CurrenciesListView)


urlpatterns = [
    path('currencies/', CurrenciesListView.as_view(), name='currencies'),
]