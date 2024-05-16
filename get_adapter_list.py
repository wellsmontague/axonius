import requests
import pandas as pd
from bs4 import BeautifulSoup

#another squirly script written by Wells Montague 5/16/2024

# Step 1: Fetch the webpage content
url = 'https://docs.axonius.com/docs/adapters-list'
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Locate the table in the HTML
table = soup.find('table')

# Step 4: Extract table headers
headers = []
for th in table.find('thead').find_all('th'):
    headers.append(th.text.strip())

# Step 5: Extract table rows
rows = []
for tr in table.find('tbody').find_all('tr'):
    cells = tr.find_all('td')
    rows.append([cell.text.strip() for cell in cells])

# Step 6: Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Step 7: Drop the first column labelled 'Adapter Logo'
df = df.drop(columns=['Adapter Logo'])

# Step 8: Save the DataFrame to a CSV file
csv_filename = 'adapters_list.csv'
df.to_csv(csv_filename, index=False)

print(f'Table data has been saved to {csv_filename}')

