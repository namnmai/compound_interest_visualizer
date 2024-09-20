from decimal import Decimal
from django.shortcuts import render
from .forms import InvestmentForm
from .investment import Investment  # Ensure this class exists and handles calculations

def calculate_investment(request):
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            principal = form.cleaned_data['principal']
            contribution = form.cleaned_data['contribution']
            time = form.cleaned_data['time']
            interest_rate = form.cleaned_data['interest_rate']
            inflation_rate = form.cleaned_data.get('inflation_rate')  # This can be None if not provided

            # Create an instance of the Investment class
            investment = Investment(
                principal=principal,
                contribution=contribution,
                time=time,
                interest_rate=interest_rate,
                inflation_rate=inflation_rate  # Pass the inflation rate, even if it’s None
            )
            
            # Calculate future values
            investment.calculate_future_values()

            # Generate plot and table data
            graph_json = investment.get_plot()
            table_data = investment.get_table_data()

            return render(request, 'investment_result.html', {
                'form': form,
                'graph_json': graph_json,
                'table_data': table_data,
            })
    else:
        form = InvestmentForm()
        
    return render(request, 'investment_form.html', {'form': form})


def about(request):
    return render(request, 'about.html')

from django.shortcuts import render

def faq(request):
    return render(request, 'faq.html')
