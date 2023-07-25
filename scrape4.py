import requests
from bs4 import BeautifulSoup
import pprint
from itertools import zip_longest

def get_hacker_news(page_number):
    url = f'https://news.ycombinator.com/news?p={page_number}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.select('.titleline a'), soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for link, sub in zip_longest(links, subtext):
        title = link.getText()
        href = link.get('href')
        if sub:
            vote = sub.select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
    return hn

mega_links = []
mega_subtext = []

for page_number in range(1, 3):  # Scraping through first two pages
    links, subtext = get_hacker_news(page_number)
    mega_links.extend(links)
    mega_subtext.extend(subtext)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
