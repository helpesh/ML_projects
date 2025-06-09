
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Send an HTTP request to the webpage
url = 'https://en.wikipedia.org/wiki/Cloud-computing_comparison'  
try:
    response = requests.get(url)
    response.raise_for_status() #raise an HTTP error for bad requests
except requests.exceptions.HTTPError as err:
    print('HTTP errror occured')
except Exception as err:
    print('Other Error occured')
    

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Print the title of the webpage to verify
print("Title: " + soup.title.text)

#extract the table
table= soup.find('table')

#extract the rows
rows=table.find_all('tr')

#extract headers from the first row 
headers = [header.text.strip() for header in rows[0].find_all('th')]

#Loop through the rows and extract the data
data=[]
for row in rows[1:]:
    cols = row.find_all('td')
    if len(cols)==9:
       # cols = [col.text.strip() for col in cols]
       # data.append(cols)
        if cols[0]:
            Provider = cols[0].text.strip()  
        else:
             'N/A'
        Launched = cols[1].text.strip() if cols[1] else 'N/A'
        Block_storage = cols[2].text.strip() if cols[2] else 'N/A'
        Assignable_IP = cols[3].text.strip() if cols[3] else 'N/A'
        Smpt_Support = cols[4].text.strip() if cols[4] else 'N/A'
        Iops_Guaranteed_minimum = cols[5].text.strip() if cols[5] else 'N/A'
        Security = cols[6].text.strip() if cols[6] else 'N/A'
        Locations = cols[7].text.strip() if cols[7] else 'N/A'
        Notes = cols[8].text.strip() if cols[8] else 'N/A'
        data.append([Provider,Launched,Block_storage,Assignable_IP,Smpt_Support,Iops_Guaranteed_minimum,
        Security,Locations,Notes])
    else:
        print('skipping a row because it is missing')

#convert the data into a pandas Datafram to verify
df = pd.DataFrame(data, columns=headers)

#Display the first few rows of the datafram
print(df.head())

#save the DataFrame to a CSV file
df.to_csv('scraped_data.csv', index=False)
print('Data successfully saved to the file')