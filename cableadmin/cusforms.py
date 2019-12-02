from django import forms
from .models import customers
class custforms(forms.ModelForm):
    customer_id=forms.CharField(max_length=5)
    customer_name=forms.CharField(max_length=30)
    area_id=forms.CharField(max_length=5)
    server_id=forms.CharField(max_length=5)
    wifi_plans=forms.CharField(max_length=5)
    cable_plans=forms.CharField(max_length=5)
    class Meta:
        model=customers
        fields=("customer_id","customer_name","server_id","wifi_plans","area_id","cable_plans")