from django import forms

class InvestmentForm(forms.Form):
    initial_investment = forms.DecimalField(
        label="Initial Investment ($)",
        min_value=0,
        decimal_places=2,
        max_digits=15,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter initial investment'})
    )
    monthly_contribution = forms.DecimalField(
        label="Monthly Contribution ($)",
        min_value=0,
        decimal_places=2,
        max_digits=15,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter monthly contribution'})
    )
    investment_years = forms.IntegerField(
        label="Investment Duration (Years)",
        min_value=1,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter duration in years'})
    )
    interest_rate = forms.DecimalField(
        label="Interest Rate (%)",
        min_value=0,
        max_value=100,
        decimal_places=2,
        max_digits=5,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter annual interest rate'})
    )