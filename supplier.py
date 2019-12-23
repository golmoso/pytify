# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:16:30 2019

@author: GOlmos01
"""

class Supplier():
    """Represents a supplier object. This class behaves like a GOF Composite.
    Attributes include: name, artificial_name, rut, childs.
    """
    childs = []
    supports = []
    def __init__(self, name, artificial_name, rut):
        self.name = name
        self.artificial_name = artificial_name
        self.rut = rut
    def add_child(self, client):
        self.childs.append(client)
    