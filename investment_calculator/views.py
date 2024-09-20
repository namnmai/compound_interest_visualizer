from decimal import Decimal
from django.shortcuts import render
from .forms import InvestmentForm
from .investment import Investment  # Ensure this class exists and handles calculations
import json
import plotly.graph_objs as go
import plotly.utils  # Ensure this import for JSON encoding

def calculate_investment(request):
    form = InvestmentForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
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
    else:
        # Create an empty plot and table data if no POST request or invalid form
        graph_json = generate_empty_plot()
        table_data = generate_empty_table()

    return render(request, 'calculator.html', {
        'form': form,
        'graph_json': graph_json,
        'table_data': table_data,
    })

def generate_empty_plot():
    # Create an empty plot with Plotly
    layout = go.Layout(
        title=dict(
            text='Total Savings Over Time',
            x=0.5,  # Center the title
            xanchor='center',
            font=dict(size=24)
        ),
        xaxis=dict(
            title='Time (years)',
            titlefont=dict(size=18),
            tickfont=dict(size=14),
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            zeroline=False,
            ticks='outside',
            ticklen=8,
            tickwidth=2,
            tickcolor='#000'
        ),
        yaxis=dict(
            title='US Dollars ($)',
            titlefont=dict(size=18),
            tickfont=dict(size=14),
            tickformat='$,.0f',
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            zeroline=False,
            ticks='outside',
            ticklen=8,
            tickwidth=2,
            tickcolor='#000'
        ),
        autosize=True,
        height=600,  # Adjust height as needed
        margin=dict(
            l=50,
            r=50,
            t=80,
            b=100  # Increase bottom margin to accommodate legend
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            bordercolor="Black",
            borderwidth=1,
            bgcolor="white",
            orientation='h',  # Horizontal legend
            x=0.5,
            y=-0.2,  # Position below x-axis; adjust as needed
            xanchor='center',
            yanchor='top',
            font=dict(size=14)
        ),
        hovermode='x unified',
    )
    data = []

    empty_plot = go.Figure(data=data, layout=layout)
    return json.dumps(empty_plot, cls=plotly.utils.PlotlyJSONEncoder)

def generate_empty_table():
    # Create an empty table structure with headers but no data
    return []

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')
