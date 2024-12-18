import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV file
df = pd.read_csv('data/max.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Plot Body Weight
plt.figure(figsize=(14, 8))
plt.plot(df['Date'], df['Body Weight'])
plt.scatter(df['Date'], df['Body Weight'], color='blue', zorder=5)

# Add labels and title
plt.ylabel('Weight (lbs)', rotation=0, labelpad=40)
plt.title('Body Weight Over Time')
plt.grid(True, axis='both')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Format x-axis to show month and day
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Show the plot
plt.show()