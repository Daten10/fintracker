from django.urls import path
from .views import add_transaction, get_stats

urlpatterns = [
    path('add_transaction/', add_transaction),
    path('get_stats/', get_stats),
]
