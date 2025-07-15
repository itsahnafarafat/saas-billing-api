from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    duration_months = models.IntegerField()

    def __str__(self):
        return f"{self.name} (${self.price})"

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"
    
class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} for {self.user.username}"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"