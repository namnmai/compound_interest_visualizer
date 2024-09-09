import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick



def get_user_input():
    """Function to get and validate user input for investment parameters."""
    while True:
        try:
            principal = int(input('What is your initial investment? (in USD)\n'))
            if principal < 0:
                raise ValueError("Initial investment must be a positive number.")
            contribution = int(input('How much are you contributing a month? (in USD) \n'))
            if contribution < 0:
                raise ValueError("Monthly contribution cannot be negative.")
            time = int(input('What is the length of time? (in years)\n'))
            if time < 0:
                raise ValueError("Time must be a positive number of years.")
            interest_rate = float(input('What is the annual interest rate? (in %)\n')) / 100
            if interest_rate < 0 or interest_rate > 1:
                raise ValueError("Interest rate must be between 0% and 100%.")
            return principal, contribution, time, interest_rate
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def calculate_future_values(principal, contribution, time, interest_rate):
    """Function to calculate future values and total contributions."""
    time_plot = np.arange(time + 1)
    compound_interest = (principal * (1 + interest_rate) ** time_plot) + \
                        (12 * contribution / interest_rate) * ((1 + interest_rate) ** time_plot - 1) \
        if interest_rate != 0 else principal + 12 * contribution * time_plot
    total_contribution = principal + time_plot * (12 * contribution)
    return time_plot, compound_interest, total_contribution


def configure_plot(ax, time, compound_interest):
    """Function to configure plot settings."""
    plt.title('Total Savings', fontsize=20)
    plt.xlabel('Time (years)', fontsize=12.5)
    plt.ylabel('US Dollars ($)', fontsize=12.5)
    plt.xlim(0, time + 1)
    plt.ylim(0, max(compound_interest) if max(compound_interest) > 0 else 1)  # Avoid zero y-limits

    plt.yticks(ticks=plt.yticks()[0], labels=plt.yticks()[0].astype(int))

    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)
    plt.grid()


def plot_values(time_plot, compound_interest, total_contribution):
    """Function to plot the future value and total contribution."""
    fig = plt.figure(figsize=(15, 7.5))
    ax = fig.add_subplot()
    plt.style.use('classic')
    configure_plot(ax, len(time_plot) - 1, compound_interest)

    plt.plot(time_plot, compound_interest, 'r-', marker='o', label='Future Value')
    plt.plot(time_plot, total_contribution, 'b-', marker='o', label='Total Contribution')
    fig.tight_layout()
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.show()


def main():
    """Main function to run the investment plot program."""
    principal, contribution, time, interest_rate = get_user_input()
    time_plot, compound_interest, total_contribution = calculate_future_values(principal, contribution, time,
                                                                               interest_rate)
    plot_values(time_plot, compound_interest, total_contribution)


if __name__ == "__main__":
    main()
