import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data/max.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Forward fill missing values for lifting columns
df_filled = df.copy()
df_filled[['Squat', 'Bench Press', 'Deadlift', 'Overhead Press']] = df_filled[['Squat', 'Bench Press', 'Deadlift', 'Overhead Press']].fillna(method='ffill')

# Plot each column
plt.figure(figsize=(14, 8))

# Plot Body Weight
plt.plot(df['Date'], df_filled['Body Weight'], label='Body Weight')

# Plot Squat
plt.plot(df['Date'], df_filled['Squat'], label='Squat')
plt.scatter(df['Date'], df['Squat'], color='orange', zorder=5)

# Plot Bench Press
plt.plot(df['Date'], df_filled['Bench Press'], label='Bench Press')
plt.scatter(df['Date'], df['Bench Press'], color='green', zorder=5)

# Plot Deadlift
plt.plot(df['Date'], df_filled['Deadlift'], label='Deadlift')
plt.scatter(df['Date'], df['Deadlift'], color='red', zorder=5)

# Plot Overhead Press
plt.plot(df['Date'], df_filled['Overhead Press'], label='Overhead Press')
plt.scatter(df['Date'], df['Overhead Press'], color='purple', zorder=5)

# Add labels and title
plt.ylabel('Weight (lbs)', rotation=0, labelpad=40)
plt.title('Estimated One Rep Max Progress Over Time')
plt.grid(True, axis='both')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Format x-axis to show month names
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%B'))

# Show the plot
plt.show()