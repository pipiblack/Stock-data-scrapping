import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data = requests.get(url).text
soup = bs(data,"html.parser")

# print(data)

netflix_df = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")

    date = col[0].text
    open = col[1].text
    high = col[2].text
    Low = col[3].text
    close = col[3].text
    volume = col[4].text

    netflix_df = netflix_df.append({"Date":date,"Open":open,"High":high,"Low":Low,"Close":close,"Volume":volume},ignore_index=True)

print(netflix_df.head(20))


print("exporting to dataframe...")

print(netflix_df)
print("exported data to dataframe")

netflix_df.to_csv("netflix_stock.csv", index=False)
print("CSV file exported successfully.")

download_link = '<a href="netflix_stock.csv" download>Download CSV</a>'
print(f"Click the link to download the CSV file: {download_link}")
