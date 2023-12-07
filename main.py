from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

# Functions in which we pass url and keyword, we pass in the keyword to check if it's in the URL and
# if its there we will print it out.
def spider_urls(url, keyword):
    try:
        #Starting with open up a response variable, if the response status code == 200, we continieu with the if statement
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        #print(urls)

        # If a link on a page has not been visited, this loop will crawl the page and open up all links on that page
        # and search for our keyword. If the keyword is there it will give us the site as a possible attack site.
        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                # Use of "urljoin" guarantees it's a real url. But you have to use an absolute url, e.g https://www.yahoo.com
                # not only www.yahoo.com, it wont work.
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    #This is recursively go through all links and grab all domains.
                    spider_urls(url_join, keyword)
            else:
                pass

url = input("Enter the URL you want to scrap. ")
keyword = input("Enter the keyword to search for in the URL provided. ")
spider_urls(url, keyword)

# https://www.yahoo.com









