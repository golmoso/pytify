# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:32:05 2019

@author: GOlmos01
"""

from scales import Scale

class MultiScale(Scale):
    """Represent a scale's child object. Attribute supplier is a
    Supplier object
    A Multi scale has many ranges, each with a discount"""    
    def __init__(self, supplier):
        super().__init__(supplier)
        self.ranges = []
    def add_discount(self, minimun, maximun, discount):
        """
        Parameters
        ----------
        minimun : int.
        maximun : int.
        discount : int.

        Returns
        -------
        None.

        """
        self.ranges.append(minimun, maximun, discount)
    def calc_total_discount(self, investment):
        """
        Calculates total discount and adds it to instance 
        parameter total_discounts.

        Returns
        -------
        sum : int.

        """
        tmp_sum = 0
        for i in self.ranges:
            tmp_sum += self.calc_discount(investment, i)
        return tmp_sum
    def calc_discount(self, investment, _range_):
        if investment in range(_range_[0], _range_[1]):
            return investment * _range_[2]
        return 0
    