import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 200  # Mean total cholesterol level
std_dev = 35  # Standard deviation

# Generate x values
x = np.linspace(100, 300, 1000)
# Calculate the normal distribution PDF
y = norm.pdf(x, mean, std_dev)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Cholesterol Distribution', color='blue')
plt.fill_between(x, y, where=(x < 184), color='green', alpha=0.5, label='Cholesterol < 184 mg/dL')
plt.fill_between(x, y, where=(x >= 184), color='red', alpha=0.5, label='Cholesterol ≥ 184 mg/dL')

# Add an arrow at 184 mg/dL
plt.annotate('184 mg/dL',
             xy=(184, norm.pdf(184, mean, std_dev)),
             xytext=(184, norm.pdf(184, mean, std_dev) + 0.0005),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

# Labels and title
plt.title('Estimated Distribution of Total Cholesterol Levels in 55-Year-Old U.S. Males')
plt.xlabel('Total Cholesterol (mg/dL)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()