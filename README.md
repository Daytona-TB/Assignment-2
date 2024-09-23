A. This program was designed to answer the prompt "How many flights occur each month?" based on the data set https://www.kaggle.com/datasets/flashgordon/usa-airport-dataset/data. It reads through the data set and and chronologically organizes the flights by date and then sorts the data into flights per month per year. 

B. Functionality
# Input
The program takes a CSV file named Airport2.csv as input.
The CSV file contains flight data with a column header Fly_date that holds the flight dates in the format YYYY-MM-DD.
Output
The program outputs the count of flights for each year and month in chronological order.
The output is printed to the console in the format: Year YYYY, Month MM: X flights.

C. 
Import the CSV Module: The csv module is imported to handle CSV file operations.
Initialize Dictionary: A dictionary flights_per_year_month is initialized to store the count of flights per year and month.
Open CSV File: The CSV file Airport2.csv is opened in read mode.
Create CSV Reader: A csv.DictReader object is created to read the CSV file as a dictionary.
Skip Header: The header row is skipped using next(reader).
Iterate Rows: The program iterates over each row in the CSV file.
Extract Date: The flight date is extracted from the Fly_date column.
Split Date: The date is split into year, month, and day.
Create Key: A key in the format year-month is created.
Update Dictionary: The dictionary is updated to count the flights for each year and month.
Print Results: The dictionary is sorted, and the count of flights for each year and month is printed in chronological order.
