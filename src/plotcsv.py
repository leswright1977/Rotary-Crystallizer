import matplotlib.pyplot as plt
from datetime import datetime
import argparse

# Set up argument parsing for the script
parser = argparse.ArgumentParser(description='Plot temperature data from a CSV file.')
parser.add_argument('filename', type=str, help='Path to the CSV file containing temperature data')
args = parser.parse_args()

# Initialize lists to store the data
date_times = []
target_temperatures = []
actual_temperatures = []
errors = []

# Open the file and read line by line
with open(args.filename, 'r') as file:
	for line in file:
		# Strip any extra whitespace and newline characters, then split by commas
		row = line.strip().split(',')

		# Parse each column
		try:
			date_time_str = row[0]
			target_temp = float(row[2])
			actual_temp = float(row[3])


			# Convert date and time string to datetime object for plotting
			date_time = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

			# Append parsed data to lists
			date_times.append(date_time)
			target_temperatures.append(target_temp)
			actual_temperatures.append(actual_temp)

			# Calculate the error and add it to the errors list
			error = actual_temp - target_temp
			errors.append(error)
		except:
			print("Bad Row! Skipping!")

# Plotting the full temperature data
plt.figure(figsize=(10, 6))
plt.plot(date_times, target_temperatures, label='Target Temperature', color='orange', linestyle='--')
plt.plot(date_times, actual_temperatures, label='Actual Temperature', color='blue', linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.ylim(35, 75)
plt.title('Temperature Monitoring Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()

# Show the full data plot
plt.show()

# Plotting the error data
plt.figure(figsize=(10, 6))
plt.plot(date_times, errors, label='Temperature Error (Actual - Target)', color='red', linestyle='-')
plt.xlabel('Date and Time')
plt.ylabel('Temperature Error (°C)')
plt.title('Temperature Error Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid()

# Show the error plot
plt.show()

