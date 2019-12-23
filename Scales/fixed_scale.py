# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:27:02 2019

@author: GOlmos01
"""

from scales import Scale

class FixedScale(Scale):
    """Represent a scale's child object. Attribute supplier is a
    Supplier object
    Fixed Scales means a fixed range with only one discount"""    
    def __init__(self, supplier, minimun, maximun, discount):
        super().__init__(supplier)
        self.minimun = minimun
        self.maximun = maximun
        self.discount = discount
    def calc_discount(self, investment):
        if investment in range(self.minimun, self.maximun):
            return investment * self.discount
        return 0
    