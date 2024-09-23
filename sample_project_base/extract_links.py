import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def parse_webpage(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_links(soup, base_url):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag.get('href')
        full_url = urljoin(base_url, href)
        links.append(full_url)
    return links

def print_links(links):
    for link in links:
        print(link)

def main(url):
    html_content = fetch_webpage(url)
    if html_content:
        soup = parse_webpage(html_content)
        links = extract_links(soup, url)
        print_links(links)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    main(url)

