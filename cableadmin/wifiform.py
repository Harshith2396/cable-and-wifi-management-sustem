from .models import wifi_properties 
from django import forms
class wifi_form(forms.ModelForm):
    wifi_id=forms.CharField(max_length=5)
    wifi_plan_name=forms.CharField(max_length=30)
    wifi_price=forms.CharField(max_length=10)
    speed_provided=forms.CharField(max_length=10)
    class Meta:
        model=wifi_properties
        fields=('wifi_id','wifi_plan_name','wifi_price','speed_provided')