# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:25:45 2019

@author: GOlmos01
"""

from scales import Scale

class BonusScale(Scale):
    """Represent a scale's child object. 
    Bonus means a fixed range with a fixed return"""    
    def __init__(self, supplier):
        super().__init__(supplier)
        self.bonuses = []
    def calc_discount(self, investment):
        total_bonus = 0
        for bonus in self.bonuses:
            if investment in range(bonus[0], bonus[1]):
                total_bonus += bonus[2]
        return total_bonus
