from rest_framework import generics
from .models import Plan, Subscription, Invoice, Payment
from .serializers import PlanSerializer, SubscriptionSerializer, InvoiceSerializer, PaymentSerializer

# Plans: Everyone can see
class PlanListView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# Subscriptions: List and Create
class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# Invoices: List only
class InvoiceListView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


# Payments: List only
class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

