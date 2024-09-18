import numpy as np
import plotly.graph_objs as go
import json
import plotly

class Investment:
    def __init__(self):
        self._principal = None
        self._contribution = None
        self._time = None
        self._interest_rate = None
        self._time_plot = None
        self._compound_interest = None
        self._total_contribution = None

    def calculate_future_values(self):
        """Function to calculate future values and total contributions"""
        self._time_plot = np.arange(self._time + 1)
        if self._interest_rate == 0:
            self._compound_interest = self._principal + 12 * self._contribution * self._time_plot
        else:
            self._compound_interest = (
                self._principal * (1 + self._interest_rate) ** self._time_plot
            ) + (
                (12 * self._contribution / self._interest_rate)
                * ((1 + self._interest_rate) ** self._time_plot - 1)
            )
        self._total_contribution = self._principal + self._time_plot * (12 * self._contribution)

    def get_table_data(self):
        """Returns the calculated values as a list of dictionaries for the table."""
        data = []
        for year, future_value, total_contrib in zip(
            self._time_plot, self._compound_interest, self._total_contribution
        ):
            data.append({
                'year': int(year),
                'future_value': future_value,
                'total_contribution': total_contrib
            })
        return data

    # investment_calculator/investment.py

    def get_plot(self):
        """Function to create a customized Plotly graph and return it as JSON"""
        # Create traces with thicker lines
        trace1 = go.Scatter(
            x=self._time_plot,
            y=self._compound_interest,
            mode='lines+markers',
            name='Future Value',
            line=dict(
                color='red',
                width=2  # Plot line thickness
            ),
            marker=dict(
                size=8  # Adjust marker size
            ),
            hovertemplate=(
            '<b>Future Value</b><br>'
            'Amount: $%{y:,.2f}<extra></extra>'
            )
        )
        trace2 = go.Scatter(
            x=self._time_plot,
            y=self._total_contribution,
            mode='lines+markers',
            name='Total Contribution',
            line=dict(
                color='blue',
                width=2  # Plot line thickness
            ),
            marker=dict(
                size=8
            ),
            hovertemplate=(
            '<b>Total Contribution</b><br>'
            'Amount: $%{y:,.2f}<extra></extra>'
            )
        )

        data = [trace1, trace2]

        # Define the layout with custom settings
        layout = go.Layout(
            title=dict(
                text='Total Savings Over Time',
                x=0.5,
                xanchor='center',
                font=dict(size=24)
            ),
            xaxis=dict(
                # ... existing xaxis settings ...
            ),
            yaxis=dict(
                # ... existing yaxis settings ...
            ),
            autosize=True,
            height=600,
            margin=dict(
                l=50,
                r=50,
                t=80,
                b=100  # Increased bottom margin
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            legend=dict(
                orientation='h',
                x=0.5,
                y=-0.2,
                xanchor='center',
                yanchor='top'
            ),
            hovermode='x unified',
        )

        fig = go.Figure(data=data, layout=layout)

        # Convert the plot to JSON format for rendering in the template
        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graph_json
