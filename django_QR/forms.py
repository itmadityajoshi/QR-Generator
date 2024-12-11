from django import forms

class QrCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=55, 
        label='Restaurant Name', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the Restaurant Name'
        })
        )
    url = forms.URLField(
        max_length=500, 
        label='Menu Url',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the URL of your Online Menu'
        })
        )