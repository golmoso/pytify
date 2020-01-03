# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 16:27:55 2020

@author: GOlmos01
"""

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

class PdfWriter():
    def simple_report(self, df):
        # df = pd.DataFrame()
        # df['Question'] = ["Q1", "Q2", "Q3", "Q4"]
        # df['Charles'] = [3, 4, 5, 3]
        # df['Mike'] = [3, 3, 4, 4]
        
        # share_by_group = GeneralReport().anual_share_by(full_df, 'Grupo')
        plt.figure(0)
        plt.pie(df['Inversion Total'], labels=df.index, 
                startangle=90, autopct='%1.1f%%')
        plt.title("Group Share")
        plt.figtext(0.15, 0.09, s="Fig.1 Distribución de las inversiones realizadas por los grupos")
        plt.savefig("group_share.png")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial', 'B', 12)
        pdf.cell(60)
        pdf.cell(75, 10, "A Tabular and Graphical Report of Professor Criss's Ratings by Users Charles and Mike", 0, 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-40)
        pdf.cell(50, 10, 'Question', 1, 0, 'C')
        pdf.cell(40, 10, 'Charles', 1, 0, 'C')
        pdf.cell(40, 10, 'Mike', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('arial', '', 12)
        # for i in range(0, len(df)):
        #     pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
        #     pdf.cell(40, 10, '%s' % (str(df.Mike.iloc[i])), 1, 0, 'C')
        #     pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
        #     pdf.cell(-90)
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-30)
        pdf.image('group_share.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
        pdf.output('test.pdf', 'F')