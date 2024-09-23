import csv

# Define a dictionary to store the count of flights per year and month
flights_per_year_month = {}

# Open the CSV file
with open('flight_data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Extract the flight date from the row
        flight_date = row[1]
        
        # Extract the year, month, and date from the flight date
        year, month, date = flight_date.split('-')
        
        # Create a key for the year and month
        year_month = f"{year}-{month}"
        
        # Increment the count of flights for the corresponding year and month
        if year_month in flights_per_year_month:
            flights_per_year_month[year_month] += 1
        else:
            flights_per_year_month[year_month] = 1

# Print the count of flights per year and month in chronological order
for year_month, count in sorted(flights_per_year_month.items()):
    year, month = year_month.split('-')
    print(f"Year {year}, Month {month}: {count} flights")