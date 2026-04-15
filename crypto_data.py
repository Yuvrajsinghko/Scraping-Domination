import requests, csv , re

from bs4 import BeautifulSoup





def extract_proxies(url,filepath):
    res=requests.get(url)
    print(res.status_code)
    proxies=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+',res.text)
    with open(filepath,'a',newline="") as file:
        writer=csv.writer(file)
        for proxy in proxies:
            writer.writerow([proxy])


    
url_1="https://free-proxy-list.net/en/"
# extract_proxies(url_1,"scraped_data/crypto.csv")



    


# url = "https://finance.yahoo.com/markets/crypto/all/?start=0&count=100"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }
# response=requests.get(url)

# print(response.status_code)

# nasty_soup=BeautifulSoup()