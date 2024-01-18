#Load the necessary modules: requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request and get HTML content
url = "http://abulafia.mt.ic.ac.uk/shannon/radius.php"
response = requests.get(url)
html_content = response.content

# Step 2: Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Locate the table element 
table = soup.find('table')  #Inspect the web page that you want to extract and change the value

if table:
    # Initialize variables to track merged column values
    previous_value = None
    previous_value1 = None
    previous_value2 = None

    # Iterate through rows
    for row in table.find_all('tr'):
        # Iterate through columns in each row
        columns = row.find_all(['td', 'th'])
        row_data = [column.text.strip() for column in columns]

        if len(row_data) ==7:
          previous_value = row_data[0]
        if len(row_data)==6:
          previous_value1 = row_data[0]
          row_data.insert(0, previous_value)
        if len(row_data)==5:
          row_data.insert(0, previous_value1)
          row_data.insert(0, previous_value)
          #previous_value = row_data[0]
        if len(row_data) == 7 and row_data[2] == 'VI':
          print(row_data)
else:
    print("Table not found on the web page.")
