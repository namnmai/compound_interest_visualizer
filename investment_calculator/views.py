from django.shortcuts import render
from .forms import InvestmentForm
from .investment import Investment

def calculate_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            initial_investment = form.cleaned_data['initial_investment']
            monthly_contribution = form.cleaned_data['monthly_contribution']
            investment_years = form.cleaned_data['investment_years']
            interest_rate = form.cleaned_data['interest_rate']

            # Perform calculations
            investment = Investment(
                initial_investment=initial_investment,
                monthly_contribution=monthly_contribution,
                investment_years=investment_years,
                interest_rate=interest_rate
            )
            graph_json = investment.get_plot()
            table_data = investment.get_table_data()

            context = {
                'graph_json': graph_json,
                'table_data': table_data,
                'form': form  # Optional: Pass the form back for further use
            }
            return render(request, 'calculator/investment_result.html', context)
    else:
        form = InvestmentForm()
    return render(request, 'calculator/investment_form.html', {'form': form})


def about(request):
    return render(request, 'about.html')
