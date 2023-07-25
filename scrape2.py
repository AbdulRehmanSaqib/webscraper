import requests
from bs4 import BeautifulSoup
import re

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline a')
subtext = soup.select('.subtext')

def extract_points(points_str):
    points_match = re.search(r'(\d+)', points_str)
    return int(points_match.group(1)) if points_match else 0

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        vote = subtext[idx].select('.score')
        points = extract_points(vote[0].getText().strip()) if vote else 0
        print(points)
        hn.append({'title': title, 'link': href, 'points': points})
    return hn

print(create_custom_hn(links, subtext))

