from django.urls import path
from transactions import views

urlpatterns = [
    path("", views.get_all_transactions, name="get-all"),
    path("<uuid:pk>/", views.get_transaction_by_id, name="get-one"),
    path("post/", views.post_transaction, name="post"),
    path("update/<uuid:pk>/", views.update_transaction, name="update"),
    path("delete/<uuid:pk>/", views.delete_transaction, name="delete"),
]
