# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:31:52 2019

@author: GOlmos01

a.	Composición de la base de datos
b.	Inv. Total por grupo - CHECK
c.	Inv. Total por medio
d.	Inv. Total por tipo de medio - CHECK
e.	Top clients
f.	Inv. Mensual por grupo
g.	Inv. Mensual por grupo de medio (ON-OFF)
h.	Inv. Mensual por tipo de medio

"""

import pandas as pd
import numpy as np

class GeneralReport():
    def anual_share_by(self, df, columns):
        """
        Get the anual share by 'columns'

        Parameters
        ----------
        df : Full DB DataFrame.
        columns : pivot variable.

        Returns
        -------
        share : pivot table DataFrame.

        """
        share = pd.pivot_table(df, values='Inversion Total', 
                               index=[columns], aggfunc=np.sum)
        return share
    def monthly_share_by(self, df, columns):
        """
        Get the monthly share by 'columns'

        Parameters
        ----------
        df : Full DB DataFrame.
        columns : pivot variable.

        Returns
        -------
        share : pivot table DataFrame.

        """
        monthly = pd.pivot_table(df, values='Inversion Total', 
                                 index=[columns], columns=['Mes'], 
                                 aggfunc=np.sum)
        
        return monthly
    