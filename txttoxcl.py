from openpyxl import load_workbook
import pandas as pd

# Read the data from the text file
with open('data.txt', 'r') as file:
    lines = file.readlines()

first_name = lines[0].split()[0]  # First word in the first line
last_name = lines[0].split()[1]  # Second word in the first line
location = lines[1].strip()  # Second line
dob = lines[2].split(': ')[1].strip().replace('/', '')  # Extract DOB and remove slashes
pin = lines[3].strip()

data = {
    'First Name': [first_name],
    'Last Name': [last_name],
    'Location': [location],
    'DOB': [dob.replace('/', '')],  # Assuming you've already removed slashes from dob
    'PIN': [pin]
}
df = pd.DataFrame(data)

# Specify the path for the new Excel file
new_excel_path = 'new_hire_data.xlsx'

# Write the DataFrame to a new Excel file
df.to_excel(new_excel_path, index=False)

print(f"Data written successfully to {new_excel_path}")