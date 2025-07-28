# django_app/billing/tests/test_api.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from billing.models import Plan, Subscription, Invoice, Payment
from datetime import datetime, timedelta
from decimal import Decimal

class BillingAPITest(APITestCase):
    def setUp(self):
        """Create sample user, plan, and authenticated client."""
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        self.plan = Plan.objects.create(
            name="Starter Plan",
            price=Decimal("10.00"),
            duration=30
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            plan=self.plan,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=30),
            active=True
        )

        self.invoice = Invoice.objects.create(
            user=self.user,
            amount=Decimal("10.00"),
            paid=True
        )

        self.payment = Payment.objects.create(
            invoice=self.invoice,
            payment_id="pay_12345",
            status="Paid",
            paid_at=datetime.now()
        )

    def test_plan_list(self):
        """Ensure plans API returns list of available plans."""
        url = reverse('plan-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Plan.objects.count())

    def test_subscription_list(self):
        """Ensure subscriptions API returns user's subscriptions."""
        url = reverse('subscription-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Subscription.objects.filter(user=self.user).count())

    def test_invoice_list(self):
        """Ensure invoices API returns user's invoices."""
        url = reverse('invoice-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Invoice.objects.filter(user=self.user).count())

    def test_payment_list(self):
        """Ensure payments API returns user's payments."""
        url = reverse('payment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Payment.objects.count())
