import requests, csv
from bs4 import BeautifulSoup



url ="https://finance.yahoo.com/markets/stocks/52-week-gainers/?start=1400&count=100"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}



response=requests.get(url,headers=headers)
raw_data=response.text

nasty_soup=BeautifulSoup(raw_data,"html.parser")


rows = nasty_soup.find_all("tr",class_="yf-1m4mc7b")

# print(rows)
headers=[th.get_text() for th in rows[0].find_all('th')]
final_raw_data=[]
for row in rows[1:]:

    col=[td.get_text() for td in row.find_all("td",class_="yf-1m4mc7b") ]
    final_raw_data.append(dict(zip(headers,col)))
    


with open("scraped_data/stocks_data.csv","a",newline="") as file:
    writer=csv.DictWriter(file,fieldnames=headers)
    
    writer.writerows(final_raw_data)

print(f"Task Completed successfully  url:{url}")


