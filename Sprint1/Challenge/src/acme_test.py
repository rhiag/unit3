"""
Testcases for Acme products
"""

import pytest
import random
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS, inventory_report


def test_default_product_price():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():
    """Test default product weight being 20."""
    prod = Product('Test Product')
    assert prod.weight == 20


def test_product_with_diff_values():
    """Test product methods by passing different values as attributes"""
    prod = Product('Test Product', price=25, weight=25, flammability=1.2)
    assert prod.stealability() == 'Very Stealable!'
    assert prod.explode() == '...boom!'


def test_default_num_products():
    """Test functioning of default num_products in generated_products"""
    actual_length = len(generate_products())
    assert actual_length == 30


def test_legal_names():
    """Tests if generated name is present in adjective and noun lists"""
    gen_name = str(random.choice(ADJECTIVES) + " " + random.choice(NOUNS))
    prod = Product(name=gen_name)
    first_name = prod.name.split()[0]
    last_name = prod.name.split()[1]
    assert first_name in ADJECTIVES
    assert last_name in NOUNS


def test_default_attributes_boxing_glove():
    """Testing the default values of BoxingGlove"""
    glove = BoxingGlove("New Gloves")
    assert glove.price == 10
    assert glove.weight == 10
