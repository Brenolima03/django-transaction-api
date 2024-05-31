from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "total", "created_at", "card_number", "cvv", "holder")
    search_fields = ("holder", "card_number")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
