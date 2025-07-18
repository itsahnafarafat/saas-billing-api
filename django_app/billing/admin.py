from django.contrib import admin
from .models import Plan, Subscription, Invoice, Payment

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_months')

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'active')
    list_filter = ('active',)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'created_at', 'paid')
    list_filter = ('paid',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'invoice', 'status', 'paid_at')
    list_filter = ('status',)
