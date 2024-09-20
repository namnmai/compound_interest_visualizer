from django import forms

class InvestmentForm(forms.Form):
    initial_investment = forms.DecimalField(
        label="Initial Investment ($)",
        min_value=0,
        decimal_places=2,
        max_digits=15,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter initial investment',
            'required': 'required'
        })
    )
    monthly_contribution = forms.DecimalField(
        label="Monthly Contribution ($)",
        min_value=0,
        decimal_places=2,
        max_digits=15,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter monthly contribution',
            'required': 'required'
        })
    )
    investment_years = forms.IntegerField(
        label="Investment Duration (Years)",
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter duration in years',
            'required': 'required'
        })
    )
    interest_rate = forms.DecimalField(
        label="Annual Interest Rate (%)",
        min_value=0,
        max_value=100,
        decimal_places=2,
        max_digits=5,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter annual interest rate',
            'required': 'required'
        })
    )
