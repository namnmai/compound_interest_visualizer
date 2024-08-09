import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

# Starting values
principal = int(input('What is your initial investment? (in USD)\n'))
contribution = int(input('How much are you contributing a month? (in USD) \n'))
time = int(input('What is the length of time? (in years)\n'))
interest_rate = int(input('What is the annual interest rate?\n'))/100

# Creates a numpy array to represent the x-values (time)
time_plot = np.arange(time+1)

# Creates two arrays to represent y-values (future values and total contributions)
compound_interest = (principal * (1 + interest_rate)**(time_plot)) + (12*contribution/interest_rate) * ((1 + interest_rate)**time_plot - 1)
total_contribution = principal + time_plot * (12*contribution)

# Configuring the main plot
fig = plt.figure(figsize=(15,7.5))
ax = fig.add_subplot()
plt.title('Total Savings', fontsize=20)
plt.xlabel('Time (years)', fontsize=12.5)
plt.ylabel('US Dollars ($)', fontsize=12.5)
plt.xlim(0, time + 1)
plt.ylim(0, max(compound_interest))

# Shows full y-values (no decimals)
# Source: https://stackoverflow.com/questions/34192971/how-can-i-remove-digits-after-decimal-in-axis-ticks-in-matplotlib
plt.yticks(ticks=plt.yticks()[0], labels=plt.yticks()[0].astype(int))

# Format large y-values by adding commas and dollar sign in front of values
# Source: https://stackoverflow.com/questions/38152356/dollar-sign-with-thousands-comma-tick-labels
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