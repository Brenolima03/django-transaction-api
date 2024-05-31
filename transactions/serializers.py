from rest_framework import serializers
from django.core.validators import RegexValidator
from transactions.models import Transaction
from .utils.functions import validate_credit_card
import uuid

class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
    total = serializers.FloatField()
    created_at = serializers.DateTimeField(read_only=True)
    card_number = serializers.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex="^\d{16}$",
                message="Card number must be 16 digits.",
                code="invalid_card_number"
            )
        ]
    )
    cvv = serializers.CharField(
        max_length=3,
        validators=[
            RegexValidator(
                regex="^\d{3}$",
                message="CVV must be 3 digits.",
                code="invalid_cvv"
            )
        ]
    )
    holder = serializers.CharField(
        max_length=80,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-ZÀ-ú\s]+$",
                message="Invalid holder. Only letters and spaces are allowed.",
                code="invalid_holder"
            )
        ]
    )

    class Meta:
        model = Transaction
        fields = "__all__"

    def validate_card_number(self, value):
        """
        Check that the card number is valid using the Luhn algorithm.
        """
        if not validate_credit_card(value):
            raise serializers.ValidationError("Invalid credit card number.")
        return value
