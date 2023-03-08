from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İbadulla'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Binataliyev'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'badBinataliyev@gmail.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artem'}))
    
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')
