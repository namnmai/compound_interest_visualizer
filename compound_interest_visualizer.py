import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

def get_user_inputs():
    """Function to get user inputs for the investment parameters."""
    principal = int(input('What is your initial investment? (in USD)\n'))
    contribution = int(input('How much are you contributing a month? (in USD) \n'))
    time = int(input('What is the length of time? (in years)\n'))
    interest_rate = float(input('What is the annual interest rate?\n')) / 100
    return principal, contribution, time, interest_rate

def calculate_savings(principal, contribution, time, interest_rate):
    """Function to calculate the future value and total contributions over time."""
    time_plot = np.arange(time + 1)
    compound_interest = (principal * (1 + interest_rate)**(time_plot)) + \
                        (12 * contribution / interest_rate) * ((1 + interest_rate)**time_plot - 1)
    total_contribution = principal + time_plot * (12 * contribution)
    return time_plot, compound_interest, total_contribution

def plot_savings(time_plot, compound_interest, total_contribution):
    """Function to create and display the savings plot."""
    fig = plt.figure(figsize=(15, 7.5))
    ax = fig.add_subplot()
    plt.title('Total Savings', fontsize=20)
    plt.xlabel('Time (years)', fontsize=12.5)
    plt.ylabel('US Dollars ($)', fontsize=12.5)
    plt.xlim(0, max(time_plot) + 1)
    plt.ylim(0, max(compound_interest))

    # Show full y-values (no decimals)
    plt.yticks(ticks=plt.yticks()[0], labels=plt.yticks()[0].astype(int))

    # Format large y-values by adding commas and dollar sign
    fmt = '${x:,.0f}'
    tick = mtick.StrMethodFormatter(fmt)
    ax.yaxis.set_major_formatter(tick)

    plt.style.use('classic')
    plt.plot(time_plot, compound_interest, 'r-', marker='o', label='Future Value')
    plt.plot(time_plot, total_contribution, 'b-', marker='o', label='Total Contribution')
    fig.tight_layout()
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.grid()

    plt.show()

def main():
    """Main function to run the savings calculator."""
    principal, contribution, time, interest_rate = get_user_inputs()
    time_plot, compound_interest, total_contribution = calculate_savings(principal, contribution, time, interest_rate)
    plot_savings(time_plot, compound_interest, total_contribution)

if __name__ == "__main__":
    main()
