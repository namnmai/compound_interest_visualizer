from django import forms


class InvestmentForm(forms.Form):
    principal = forms.IntegerField(
        label="Initial Investment (USD)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    contribution = forms.IntegerField(
        label="Monthly Contribution (USD)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    time = forms.IntegerField(
        label="Time (Years)",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    interest_rate = forms.FloatField(
        label="Annual Interest Rate (%)",
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
        'rows': 5
    }))