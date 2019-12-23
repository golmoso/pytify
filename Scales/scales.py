# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:27:02 2019

@author: GOlmos01
"""

class Scale():
    """Represents a scale object. This is the parent class and 
    its an abstract class. Attribute supplier is a
    Supplier object"""
    def __init__(self, supplier):
        self.supplier = supplier
    def calc_discount(self):
        """
        Returns
        -------
        int

        """
        print("Parent Scale says 0 discounts")
        return 0        
    def calc_bonus(self):
        """
        Returns
        -------
        int

        """
        print("Parent Scale says 0 bonus")
        return 0
