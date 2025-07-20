from django.urls import path
from .views import PlanListView, SubscriptionListCreateView, InvoiceListView, PaymentListView

urlpatterns = [
    path('plans/', PlanListView.as_view(), name='plan-list'),
    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('invoices/', InvoiceListView.as_view(), name='invoice-list'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
]
