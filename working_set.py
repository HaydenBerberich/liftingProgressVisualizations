import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV file
df = pd.read_csv('data/working_set.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Forward fill missing values for lifting columns except for plotting reps
df_filled = df.copy()
df_filled[['Squat', 'Bench Press', 'Deadlift', 'Overhead Press']] = df_filled[['Squat', 'Bench Press', 'Deadlift', 'Overhead Press']].fillna(method='ffill')

# Plot each column
plt.figure(figsize=(14, 8))

# Plot Body Weight
plt.plot(df['Date'], df['Body Weight'])

# Plot Squat
plt.plot(df['Date'], df_filled['Squat'])

# Plot Bench Press
plt.plot(df['Date'], df_filled['Bench Press'])

# Plot Deadlift
plt.plot(df['Date'], df_filled['Deadlift'])

# Plot Overhead Press
plt.plot(df['Date'], df_filled['Overhead Press'])

# Plot Reps with different colors for each rep count and different shapes
plt.scatter(df['Date'][df['Reps'] == 5], df['Squat'][df['Reps'] == 5], color='red', label='5 Reps', alpha=0.5, zorder=5, marker='o')  # Circle
plt.scatter(df['Date'][df['Reps'] == 3], df['Squat'][df['Reps'] == 3], color='blue', label='3 Reps', alpha=0.5, zorder=5, marker='s')  # Square
plt.scatter(df['Date'][df['Reps'] == 1], df['Squat'][df['Reps'] == 1], color='green', label='1 Rep', alpha=0.5, zorder=5, marker='^')  # Triangle

plt.scatter(df['Date'][df['Reps'] == 5], df['Bench Press'][df['Reps'] == 5], color='red', alpha=0.5, zorder=5, marker='o')
plt.scatter(df['Date'][df['Reps'] == 3], df['Bench Press'][df['Reps'] == 3], color='blue', alpha=0.5, zorder=5, marker='s')
plt.scatter(df['Date'][df['Reps'] == 1], df['Bench Press'][df['Reps'] == 1], color='green', alpha=0.5, zorder=5, marker='^')

plt.scatter(df['Date'][df['Reps'] == 5], df['Deadlift'][df['Reps'] == 5], color='red', alpha=0.5, zorder=5, marker='o')
plt.scatter(df['Date'][df['Reps'] == 3], df['Deadlift'][df['Reps'] == 3], color='blue', alpha=0.5, zorder=5, marker='s')
plt.scatter(df['Date'][df['Reps'] == 1], df['Deadlift'][df['Reps'] == 1], color='green', alpha=0.5, zorder=5, marker='^')

plt.scatter(df['Date'][df['Reps'] == 5], df['Overhead Press'][df['Reps'] == 5], color='red', alpha=0.5, zorder=5, marker='o')
plt.scatter(df['Date'][df['Reps'] == 3], df['Overhead Press'][df['Reps'] == 3], color='blue', alpha=0.5, zorder=5, marker='s')
plt.scatter(df['Date'][df['Reps'] == 1], df['Overhead Press'][df['Reps'] == 1], color='green', alpha=0.5, zorder=5, marker='^')

# Add labels and title
plt.ylabel('Weight (lbs)', rotation=0, labelpad=40)
plt.title('Working Set Progress Over Time')
plt.legend()
plt.grid(True, axis='both')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Format x-axis to show month names
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B'))

# Show the plot
plt.show()