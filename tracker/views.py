from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from django.db.models import Sum
from django.http import JsonResponse


@api_view(['POST'])
def add_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success'})  # ✅ Возвращаем JsonResponse
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def get_stats(request):
    income = Transaction.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Transaction.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    return JsonResponse({'income': income, 'expense': expense})  # ✅ JsonResponse для надежности


@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.order_by('-id')[:20]  # последние 20
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
