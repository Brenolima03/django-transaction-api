from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Transaction
from .serializers import TransactionSerializer

@api_view(["GET"])
def get_all_transactions(request):
    """
    Retrieve all transactions or filter transactions based on query parameters.

    If query parameters are provided, filter transactions accordingly.
    Otherwise, retrieve all transactions.
    Return a 200 OK response with the serialized data if transactions are found.
    If no transactions are found, return a 200 OK response with an empty list.
    """
    if request.query_params:
        transactions = Transaction.objects.filter(**request.query_params.dict())
    else:
        transactions = Transaction.objects.all()

    if not transactions.exists():
        return Response([], status=status.HTTP_200_OK)
    
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_transaction_by_id(request, pk):
    """
    Retrieve a single transaction by its ID (pk).
    
    Return a 200 OK response with the serialized data if the transaction is
    found. If the transaction does not exist, return a 404 Not Found response.
    """
    transaction = get_object_or_404(Transaction, pk=pk)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def post_transaction(request):
    """
    Create a new transaction.

    Deserialize the request data using TransactionSerializer.
    If the data is valid, save the transaction and return a 201 Created response
    with a success message. If the data is invalid, return a 400 Bad Request
    response with validation errors.
    """
    serializer = TransactionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Transaction created successfully"},
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            {"message": "Failed to create transaction",
            "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["PUT"])
def update_transaction(request, pk):
    """
    Update an existing transaction by its ID (pk).

    Retrieve the transaction. If it exists, deserialize the request data and
    save the updated transaction. If the data is valid, return a 200 OK response
    with a success message. If the data is invalid, return a 400 Bad Request
    response with validation errors.
    """
    transaction = get_object_or_404(Transaction, pk=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Transaction updated successfully"},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message": "Failed to update transaction",
            "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["DELETE"])
def delete_transaction(request, pk):
    """
    Delete an existing transaction by its ID (pk).

    If the transaction exists, delete it and return a 204 No Content response
    with a success message. If the transaction does not exist, return a 404 Not
    Found response.
    """
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return Response(
        {"message": "Transaction deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )
