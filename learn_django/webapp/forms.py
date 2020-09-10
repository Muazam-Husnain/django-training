
from django import forms
from .models import Customer

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'number', 'email', 'company', 'address')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


