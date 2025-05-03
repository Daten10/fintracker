from django.urls import path
from .views import add_transaction, get_stats,get_transactions

urlpatterns = [
    path('add_transaction/', add_transaction),
    path('get_stats/', get_stats),
    path('api/get_transactions/', get_transactions),
]
