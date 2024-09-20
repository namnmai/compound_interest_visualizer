from django import forms

class InvestmentForm(forms.Form):
    principal = forms.DecimalField(
        label="Initial Investment (USD)",
        min_value=0,
        decimal_places=2,
        max_digits=15,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter initial investment',
            'required': 'required'
        })
    )
    contribution = forms.DecimalField(
        label="Monthly Contribution (USD)",
        min_value=0,
        decimal_places=2,
        max_digits=15,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter monthly contribution',
            'required': 'required'
        })
    )
    time = forms.IntegerField(
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
    inflation_rate = forms.DecimalField(
        label="Inflation Rate (%)",
        min_value=0,
        max_value=100,
        decimal_places=2,
        max_digits=5,
        required=False,  # Make this field optional
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter inflation rate (optional)',
        })
    )
