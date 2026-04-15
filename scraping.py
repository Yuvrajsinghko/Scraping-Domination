import requests
import json
import csv

from urllib3.filepost import writer

cookies = {
    '_cg': '4000',
    'X-Default-City': '1',
    'X-Pincode': '400001',
    'XdI': 'wGun-iPxn1CQ05lQsRIKd',
    'X-Feature-Flags': '%7B%22isBestOfferEnabled%22%3Atrue%7D',
    'XPESD': '%7B%22session_id%22%3A%22s_w_wGun-iPxn1CQ05lQsRIKd_1756374859000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22session_start_time%22%3A%222025-08-28T09%3A54%3A19.156Z%22%7D',
    'XPESS_v2': 's_w_wGun-iPxn1CQ05lQsRIKd_1756374859000',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'priority': 'u=1, i',
    'referer': 'https://pharmeasy.in/search/all?name=a',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': '_cg=4000; X-Default-City=1; X-Pincode=400001; XdI=wGun-iPxn1CQ05lQsRIKd; X-Feature-Flags=%7B%22isBestOfferEnabled%22%3Atrue%7D; XPESD=%7B%22session_id%22%3A%22s_w_wGun-iPxn1CQ05lQsRIKd_1756374859000%22%2C%22session_id_flag%22%3A%22ct_id%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22session_start_time%22%3A%222025-08-28T09%3A54%3A19.156Z%22%7D; XPESS_v2=s_w_wGun-iPxn1CQ05lQsRIKd_1756374859000',
}

alphaphet_lits=['h','i','j','k']

response = requests.get(f'https://pharmeasy.in/api/search/search/?intent_id&page={2}&q={'l'}',
                        cookies=cookies, headers=headers)
raw_data = json.loads(response.text)
product = raw_data['data']['products']
for i in range(len(product)):
    products = raw_data['data']['products'][i]
    headers = ["productId", "name", "slug"]
    required_data = {k: v for k, v in products.items() if k in headers}
    print(required_data)
    with open('scraped_data/mdeico_data.csv', 'a', newline="") as file:
        t = csv.DictWriter(file, fieldnames=headers)

        t.writerow(required_data)



