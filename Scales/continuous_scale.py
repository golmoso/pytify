# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:36:32 2019

@author: GOlmos01
"""

from scales import Scale

class ContinuousScale(Scale):
    """Represent a scale's child object. Attribute supplier is a
    Supplier object"""

    def __init__(self, supplier):
        self.supplier = supplier
    def add_discount_function(self, function):
        """La idea es recibir una función como input y calcular el descuento
        en base a eso. Se pueden usar distintas librerías de parseo de funciones
        matemáticas, como PyParser."""
        #TODO search for libraries
        return 0
    def calc_total_discount(self, investment):
        #TODO calculate total continious discount
        return 0
    