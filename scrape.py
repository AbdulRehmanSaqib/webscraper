from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/newest'
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
links = (soup.select('.titleline'))
votes = soup.select('.score')

def create_custom_hn(links,votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
    return hn

print(create_custom_hn(links, votes))
driver.quit()