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

            investment = Investment()
            investment._principal = principal
            investment._contribution = contribution
            investment._time = time
            investment._interest_rate = interest_rate / 100  # Convert percentage to decimal
            investment.calculate_future_values()

            graph_json = investment.get_plot()
            table_data = investment.get_table_data()

            return render(request, 'investment_result.html', {
                'graph_json': graph_json,
                'table_data': table_data
            })
        
        else:
            # Form is invalid; render form with errors
            return render(request, 'investment_form.html', {'form': form})
        
    else:
        form = InvestmentForm()
        
    return render(request, 'investment_form.html', {'form': form})

def about(request):
    return render(request, 'about.html')