from django.urls import path
from .views import add_transaction, get_stats, get_transactions, get_categories, create_category

urlpatterns = [
    path('add_transaction/', add_transaction),
    path('get_stats/', get_stats),
    path('get_transactions/', get_transactions),
    path("get_categories/", get_categories),
    path("create_category/", create_category),
]
