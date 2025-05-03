from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from django.db.models import Sum


@api_view(['POST'])
def add_transaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_stats(request):
    income = Transaction.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Transaction.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    return Response({'income': income, 'expense': expense})
