"""
Scrape products from amazon.
"""
from gazpacho import get, soup
from urllib.parse import quote
import scrape_functions
from pprint import pprint

AMAZON_SEARCH_LINK = "https://www.amazon.com/s?k="
SITE_SOURCE = "AMAZON"

def search_items(query: str, num_results: int=3):
    """
    Searches amazon for query
    Returns list of dictionaries containing items, prices, and ratings
    """

    # Scrape that beech
    url = AMAZON_SEARCH_LINK + quote(query)
    html = get(url)
    amazon_soup = soup.Soup(html)

    # Pull all them items
    # Item Titles
    item_titles = amazon_soup.find("span", {"class": "a-text-normal"})[1:] # 1st item is "RESULTS", we don't need that
    # Prices
    price_whole = amazon_soup.find("span", {"class": "a-price-whole"})
    price_fraction = amazon_soup.find("span", {"class": "a-price-fraction"})
    # Ratings:
    ratings = amazon_soup.find("span", {"class": "a-icon-alt"})
    ratings = list(map(scrape_functions.get_rating, ratings))

    # Turn Prices into actual number
    price_items = list(map(scrape_functions.combine_numbers, zip(price_whole, price_fraction))) # price_whole and price_fraction => [(whole, fraction),],
    # Return formatted data
    return scrape_functions.format_results(SITE_SOURCE, item_titles, price_items, ratings)

pprint(search_items("beats fit pro"))