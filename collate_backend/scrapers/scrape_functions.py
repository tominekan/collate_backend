"""
Base functions to operate on scraped data
"""
from typing import Iterable

def format_results(source: str, product_names: str, prices: float, ratings: float) -> dict:
    """, 0
    Combines returns list of dictionaries containing metadata, items, prices, and rating
    """

    dict_prices = {"metadata": {"source": source}}
    searched_items = []
    for count, name in enumerate(product_names, 0):
        searched_items.append({
            "name": name.text,
            "price": prices[count],
            "rating": ratings[count]
        })
    
    dict_prices["items"] = searched_items

    return dict_prices;


def combine_numbers(numbers: tuple) -> float: 
    """
    Takes an iterable containing a whole number Soup, and a fractional Soup
    turns them into fraction
    """

    # numbers[0] is whole numbers
    # numbers[1] is price fraction
    return float(numbers[0].text + "." + numbers[1].text)


def get_rating(prices) -> float:
    """
    """

    return float(prices.text.split(sep=" ")[0])