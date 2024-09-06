import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

class Investment:

    def __init__(self):
        self._principal = self.get_principal()
        self._contribution = self.get_contribution()
        self._time = self.get_time()
        self._interest_rate = self.get_interest_rate()
        self._time_plot = None
        self._compound_interest = None
        self._total_contribution = None
        self.calculate_future_values() # Automatically calculate when object is created

    def get_principal(self):
        while True:
            try:
                self._principal = int(input('What is your initial investment? (in USD)\n'))

                if self._principal < 0:
                    raise ValueError('Initial investment must be a positive number.')

                return self._principal

            except ValueError as e:
                print(f'Invalid input: {e}. Please try again.')

    def get_contribution(self):
        while True:
            try:
                self._contribution = int(input('What is your monthly contribution? (in USD)\n'))

                if self._contribution < 0:
                    raise ValueError('Monthly contribution must be a positive number.')

                return self._contribution

            except ValueError as e:
                print(f'Invalid input: {e}. Please try again.')

    def get_time(self):
        while True:
            try:
                self._time = int(input('What is the length of time? (in years)\n'))

                if self._time < 0:
                    raise ValueError('Time must be a positive number of years.')

                return self._time

            except ValueError as e:
                print(f'Invalid input: {e}. Please try again.')

    def get_interest_rate(self):
        while True:
            try:
                self._interest_rate = float(input('What is the annual interest rate? (%)\n'))/100

                if self._interest_rate < 0 or self._interest_rate > 1:
                    raise ValueError('Interest rate must be between 0% and 100%')

                return self._interest_rate

            except ValueError as e:
                print(f'Invalid input: {e}. Please try again.')

    def calculate_future_values(self):
        """Function to calculate future values and total contributions"""

        # Creates a numpy array to represent the x-values (time)
        self._time_plot = np.arange(self._time + 1)

        # To prevent ZeroDivisionError
        if self._interest_rate == 0:
            self._compound_interest = self._principal + 12 * self._contribution * self._time_plot

        # Creates two arrays to represent y-values (future values and total contributions)
        else:
            self._compound_interest = (self._principal * (1 + self._interest_rate) ** self._time_plot) + (12 * self._contribution / self._interest_rate) * (
                        (1 + self._interest_rate) ** self._time_plot - 1)

        self._total_contribution = self._principal + self._time_plot * (12 * self._contribution)

    def configure_plot(self, ax):
        """Function to configure plot settings."""

        plt.title('Total Savings', fontsize=20)
        plt.xlabel('Time (years)', fontsize=12.5)
        plt.ylabel('US Dollars ($)', fontsize=12.5)
        plt.xlim(0, self._time + 1)
        plt.ylim(0, max(self._compound_interest) * 1.15)  # Added a buffer to y-axis limit

        # Shows full y-values (no decimals)
        # Source: https://stackoverflow.com/questions/34192971/how-can-i-remove-digits-after-decimal-in-axis-ticks-in-matplotlib
        plt.yticks(ticks=plt.yticks()[0], labels=plt.yticks()[0].astype(int))

        # Format large y-values by adding commas and dollar sign in front of values
        # Source: https://stackoverflow.com/questions/38152356/dollar-sign-with-thousands-comma-tick-labels
        fmt = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(fmt)
        ax.yaxis.set_major_formatter(tick)
        plt.grid()

    def plot_values(self):
        """Function to plot the future value and total contribution."""

        fig = plt.figure(figsize=(15, 7.5))
        ax = fig.add_subplot()
        plt.style.use('classic')

        self.configure_plot(ax)

        plt.plot(self._time_plot, self._compound_interest, 'r-', marker='o', label='Future Value')
        plt.plot(self._time_plot, self._total_contribution, 'b-', marker='o', label='Total Contribution')
        fig.tight_layout()
        ax.legend(loc='upper left')
        plt.show()

def main():
    """Main function to run the investment plot program."""
    my_investment = Investment()
    my_investment.plot_values()


if __name__ == "__main__":
    main()




