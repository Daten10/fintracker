from django.db import models


class Transaction(models.Model):
    TYPE_CHOICES = (('income', 'Доход'), ('expense', 'Расход'))

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"