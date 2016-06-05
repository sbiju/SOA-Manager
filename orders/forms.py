from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['client', 'partner_name', 's_type', 'due_date', 'smsf', 'trust_fund', 'company', 'inside_super', 'outside_super', ]
