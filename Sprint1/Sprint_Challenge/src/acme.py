"""
Product class to model ACME Product
"""

import random


class Product:
    """Models an ACME Product
    Parameters:
    - `name` (string)
    - `price` (integer: default 10)
    - `weight` (integer: default 20)
    - `flammability` (float:default 0.5)
    - `identifier` (integer)
    """

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        """Constructor for Product class"""
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        This method calculates the steal ratio = price/weight.
        Prints a message based on the ratio
        """
        self.steal = float(self.price/self.weight)
        if self.steal < 0.5:
            return 'Not so stealable...'
        elif self.steal >= 0.5 and self.steal < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very Stealable!'

    def explode(self):
        """
        This method calculates the flammable index  = flammability * weight.
        Prints a message based on the index
        """
        self.flameable_index = float(self.flammability * self.weight)
        if self.flameable_index < 10:
            return '...fizzle.'
        elif self.flameable_index >= 10 and self.flameable_index < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """Inherits an ACME Product
    Parameters:
    - same as ACME Product Class except weight
    - `weight` (integer: default 10)
    """

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        """BoxingGlove constructor extends Product Class"""
        super().__init__(name, price, weight, flammability)

    def explode(self):
        """
        This method overrides Product's method explode()
        """
        return "...it's a glove."

    def punch(self):
        """
        This method is specific to BoxingGlove Class.
        It return a message based on the weight."""
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
