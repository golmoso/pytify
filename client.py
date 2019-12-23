# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:10:40 2019

@author: GOlmos01
"""

class Client():
    """Represents a client object. This class behaves like a GOF Composite.
    Attributes include: name, artificial_name, rut, investments, childs.
    """
    childs = []
    def __init__(self, group_name, name, artificial_name):
        self.group_name = group_name
        self.name = name
        self.artificial_name = artificial_name
    def add_child(self, client):
        """
        Parameters
        ----------
        client : Client type.

        Returns
        -------
        None.

        """
        self.childs.append(client)
    