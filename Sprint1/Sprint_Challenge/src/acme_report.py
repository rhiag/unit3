"""
Module to generate random products and print a summary of them.
"""
from acme import Product
import random

# Used to generate random names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive',  'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Function to Generate random products"""
    products = []
    for item in range(0, num_products):
        gen_name = str(random.choice(ADJECTIVES) + " " + random.choice(NOUNS))
        price = random.uniform(5, 100)
        weight = random.uniform(5, 100)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name=gen_name,
                                price=price, weight=weight,
                                flammability=flammability))
    return products


def inventory_report(products):
    """Function to generates an inventory report"""
    name_list = set()
    price_list = []
    wt_list = []
    flamablity_list = []

    for p in products:
        name_list.add(p.name)
        price_list.append(p.price)
        wt_list.append(p.weight)
        flamablity_list.append(p.flammability)
# Calculating average for report
    unique_names = len(name_list)
    avg_price = sum(price_list)/len(price_list)
    avg_weight = sum(wt_list)/len(wt_list)
    avg_flammability = sum(flamablity_list)/len(flamablity_list)
# Printing
    print("$ python acme_report.py ")
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", unique_names)
    print("Average price:", round(avg_price, 2))
    print("Average weight:", avg_weight)
    print("Average flammability:", avg_flammability)


if __name__ == '__main__':
    inventory_report(generate_products(15))
