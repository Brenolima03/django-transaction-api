from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    holder = models.CharField(max_length=80)

    class Meta:
        ordering = ["created_at"]
