from datetime import datetime

from requests import Session
from db_insert import insert_db

cookies = {
    '_gid': 'GA1.2.395381604.1700108420',
    'dom3ic8zudi28v8lr6fgphwffqoz0j6c': 'a8f296f3-3049-4ada-81c2-dc822caad320%3A1%3A1',
    '_ga_CGGR769EX1': 'GS1.1.1700124586.3.1.1700126434.0.0.0',
    '_ga': 'GA1.1.1420649904.1700108420',
}

headers = {
    'authority': 'openproxylist.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '_gid=GA1.2.395381604.1700108420; dom3ic8zudi28v8lr6fgphwffqoz0j6c=a8f296f3-3049-4ada-81c2-dc822caad320%3A1%3A1; _ga_CGGR769EX1=GS1.1.1700124586.3.1.1700126434.0.0.0; _ga=GA1.1.1420649904.1700108420',
    'referer': 'https://kwork.ru/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

def get_source_json():

    # url = 'https://openproxylist.com/pages/terms-and-conditions.html'
    base_url = 'https://openproxylist.com/'
    # url = 'https://openproxylist.com/get-list.html/'
    url = 'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS.txt'
    
    s = Session()
    s.headers.update(headers)

    for i in range(2):
        print(i)
        if i == 0:
            response = s.get(base_url, cookies=cookies, headers=headers)
            print(i)
        else:
            response = s.get(url, cookies=cookies, headers=headers)
            print(i)

            with open('openproxy.txt', 'w', encoding='utf-8') as file:
                file.write(response.text)


def get_result():
    ip = ''
    port = ''
    with open('openproxy.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            addr = line.split(' ')
            if len(addr) > 2 and 'Proxy' != addr[1] and 'CountryFlag' != addr[1]:
                ip = addr[1].split(':')[0]
                port = addr[1].split(':')[1]
                insert_db(ip=ip, port=port)
                print(ip)


if __name__ == '__main__':

    get_source_json()
    get_result()
