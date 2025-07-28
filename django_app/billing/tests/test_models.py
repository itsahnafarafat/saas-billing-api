# django_app/billing/tests/test_models.py
from django.test import TestCase
from decimal import Decimal
from billing.models import Plan
from django.core.exceptions import ValidationError

class PlanModelTest(TestCase):
    def setUp(self):
        """Set up a sample plan for all tests."""
        self.plan = Plan.objects.create(
            name="Pro Plan",
            price=Decimal("29.99"),
            duration=30
        )

    def test_plan_name(self):
        """Test that the plan name is stored correctly."""
        self.assertEqual(self.plan.name, "Pro Plan")

    def test_plan_price(self):
        """Test that the plan price is stored correctly."""
        self.assertEqual(self.plan.price, Decimal("29.99"))

    def test_plan_duration(self):
        """Test that the plan duration is stored correctly."""
        self.assertEqual(self.plan.duration, 30)

    def test_str_method_returns_name(self):
        """Test that __str__ method returns the plan name."""
        self.assertEqual(str(self.plan), "Pro Plan")

    def test_invalid_price_raises_error(self):
        """Test creating a plan with negative price raises ValidationError."""
        plan = Plan(name="Invalid Plan", price=Decimal("-10.00"), duration=30)
        with self.assertRaises(ValidationError):
            plan.full_clean()  # triggers validation

    def test_invalid_duration_raises_error(self):
        """Test creating a plan with negative duration raises ValidationError."""
        plan = Plan(name="Invalid Duration", price=Decimal("19.99"), duration=-5)
        with self.assertRaises(ValidationError):
            plan.full_clean()  # triggers validation
