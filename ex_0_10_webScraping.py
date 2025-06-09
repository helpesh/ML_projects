import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.coursera.org/learn/foundations-of-ai-and-machine-learning/supplement/zfZgP/practice-activity-setup-of-a-basic-data-scraper-in-python"
response=requests.get(url)
if response.status_code==200:
    print("Request successful")
else:
    print("Failed to retrieve the web page")