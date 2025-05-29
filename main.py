import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Based on CDC and NHANES data for 55-year-old males
# Mean cholesterol level is approximately 200 mg/dL
# Standard deviation is approximately 40 mg/dL
mean = 200
std = 40

# Generate normal distribution
x = np.linspace(mean - 4*std, mean + 4*std, 1000)
y = stats.norm.pdf(x, mean, std)

# Calculate percentage of people above and below 184
percentage_below = stats.norm.cdf(184, mean, std) * 100
percentage_above = 100 - percentage_below

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x, y * 100, 'b-', linewidth=2)  # Multiply by 100 to get percentage
plt.fill_between(x, y * 100, where=(x <= 184), color='lightblue', alpha=0.5)
plt.fill_between(x, y * 100, where=(x > 184), color='lightcoral', alpha=0.5)

# Add arrow pointing to 184
plt.annotate('184 mg/dL', 
            xy=(184, stats.norm.pdf(184, mean, std) * 100),
            xytext=(184, stats.norm.pdf(184, mean, std) * 100 + 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            ha='center')

# Add text annotations for percentages
plt.text(mean - 2*std, max(y * 100) * 0.8, 
         f'Below 184: {percentage_below:.1f}%', 
         fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
plt.text(mean + 2*std, max(y * 100) * 0.8, 
         f'Above 184: {percentage_above:.1f}%', 
         fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Customize the plot
plt.title('Distribution of Total Cholesterol Levels in 55-Year-Old US Males', pad=20)
plt.xlabel('Total Cholesterol (mg/dL)')
plt.ylabel('Percentage of Population (%)')
plt.grid(True, alpha=0.3)

# Add mean line
plt.axvline(x=mean, color='red', linestyle='--', alpha=0.5)
plt.text(mean, max(y * 100) * 0.9, 'Mean', 
         rotation=90, va='top', ha='right')

plt.tight_layout()
plt.savefig('cholesterol_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
