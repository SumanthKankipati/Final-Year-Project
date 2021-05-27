
import requests
from bs4 import BeautifulSoup


def fetch_data_from_google(q):

    headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gziphgKElc, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        s = requests.Session()
        q = '+'.join(q.split())
        url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
        print(url)
        r = s.get(url, headers=headers_Get)
        soup = BeautifulSoup(r.text, "html.parser")
        # print(soup.prettify())
        # result = soup.find(class_='iKJnec')
        result1 = soup.find( "div", class_='BNeawe deIvCb AP7Wnd').text
        result2 = soup.find( "div", class_='kCrYT').text

        if(result1 == "People also ask" or result1 == "Related searches") and len(result2) > 50:
            return result2
        elif(result2 == "People also ask" or result2 == "Related searches") and len(result1) > 50:
            return result1
        elif len(result1) > 80 and len(result1) >= len(result2):
            return result1
        elif len(result2) > 80 and len(result2) >= len(result1):
            return result2
        else:
            return "Data Not Found"

    except Exception as e:
        print(e)
        return "Data Not Found"





