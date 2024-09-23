import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_webpage(url: str) -> str:
    """Fetch the webpage from the given URL and return its HTML content.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage or None if an error occurred.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None


def parse_webpage(html_content: str) -> BeautifulSoup:
    """Parse the HTML content using BeautifulSoup.

    Args:
        html_content (str): The HTML content of the webpage.

    Returns:
        BeautifulSoup: A BeautifulSoup object for navigating the parsed HTML.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def extract_links(soup: BeautifulSoup, base_url: str) -> list:
    """Extract all links from the parsed HTML content.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.
        base_url (str): The base URL for resolving relative links.

    Returns:
        list: A list of absolute URLs extracted from the webpage.
    """
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag.get('href')
        full_url = urljoin(base_url, href)
        links.append(full_url)
    return links


def print_links(links: list) -> None:
    """Print the extracted links to the console.

    Args:
        links (list): The list of links to print.
    """
    for link in links:
        print(link)


def main(url: str) -> None:
    """Main function to fetch, parse, and print links from a webpage.

    Args:
        url (str): The URL of the webpage to process.
    """
    html_content = fetch_webpage(url)
    if html_content:
        soup = parse_webpage(html_content)
        links = extract_links(soup, url)
        print_links(links)


if __name__ == "__main__":
    url = input("Enter the URL: ")
    main(url)
