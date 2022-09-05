import sys
import random
import faker
from faker.providers import company

# Add collate backend
sys.path.append("../../collate_backend")
from collate_backend.scrapers import scrape_functions

# Create a fake soup
class FakeSoup:
    def __init__(self, example_data):
        self.text = example_data

# Create instance to generate fake data
fake = faker.Faker()
fake.add_provider(company)

def test_get_rating():
    test_float = random.randint(0, 5) + (random.randint(0, 100) / 100) # Generate random float to test
    assert scrape_functions.get_rating(FakeSoup(f"{test_float} out of 5 stars")) == test_float
    

def test_format_results():
    random_price = [random.random() * random.randint(1, 100),]
    random_rating = [random.random() + random.randint(0, 4),]
    random_product_name = [FakeSoup(fake.name()),]
    random_company = fake.company()
    correct_gen_data = {
        "metadata": {"source": random_company},
        "items": [{"name": random_product_name[0].text, "price": random_price[0], "rating": random_rating[0]},]}
    
    assert scrape_functions.format_results(random_company, random_product_name, random_price, random_rating) == correct_gen_data