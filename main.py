import os
import requests
from bs4 import BeautifulSoup

url = 'https://id.indeed.com/jobs?'
params = {
    'q' : 'python developer',
    'l' : 'jakarta',
    'vjk': 'bc1a8336347c7677'
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

res = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')


#css-jbuxu0 ecydgvn0
#pagination-list

def get_total_pages():
    params = {
        'q': 'python developer',
        'l': 'jakarta',
        'vjk': 'bc1a8336347c7677'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')

    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    #Scraping Step
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul', 'pagination-list')
    pages = pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    total = int(max(total_pages))
    return total

def get_all_items():
    params = {
        'q': 'python developer',
        'l': 'jakarta',
        'vjk': 'bc1a8336347c7677'
    }
    res = requests.get(url, params=params, headers=headers)

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    soup = BeautifulSoup(res.text, 'html.parser')

    # Scraping Process

if __name__ == '__main__' :
    get_total_pages()
