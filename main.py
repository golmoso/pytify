# -*- coding: utf-8 -*-

"""
Esta es la clase main.

"""

import pandas as pd
import matplotlib.pyplot as plt 
from dataloader import DataLoader
from pdfwriter import PdfWriter
from Reports.simple_report import GeneralReport

"""Raw data loading"""
# scale_path = './Data/data_v1.1/escalas_clean.csv'
# full_db_path = './Data/data_v1.1/full_db_clean.csv'

# scales_df = DataLoader().load_scales(scale_path)
# full_df = DataLoader().load_full_db(full_db_path)

"""Dataframe loading"""
scales_df = DataLoader().load_pickle('scales')
full_df = DataLoader().load_pickle('full')

"""Reports"""

share_by_group = GeneralReport().anual_share_by(full_df, 'Grupo')
PdfWriter().simple_report(share_by_group)

# plt.figure(0)
# plt.pie(share_by_group['Inversion Total'], labels=share_by_group.index, 
#         startangle=90, autopct='%1.1f%%')
# plt.title("Group Share")
# plt.figtext(0.15, 0.09, s="Fig.1 Distribución de las inversiones realizadas por los grupos")
# plt.savefig("group_share.png")


# share_by_media = GeneralReport().anual_share_by(full_df, 'Tipo de Medio')
# plt.figure(1)
# plt.pie(share_by_media['Inversion Total'], labels=share_by_media.index, 
#         startangle=90, autopct='%1.1f%%')

# monthly_by_tyofmedia = GeneralReport().monthly_share_by(full_df, 'Tipo de Medio')
# monthly_by_tyofmedia.plot(grid=True, yticks=range(1000000, 1500000000, 100000000))

# monthly_by_group = GeneralReport().monthly_share_by(full_df, 'Grupo')
# monthly_by_group.plot(grid=True, yticks=range(1000000, 1500000000, 100000000))

top_clients = GeneralReport().get_some_top(full_df, 'Cliente Titular', 25)
#TODO sort by inversion total

"""DataFrame Writing"""
DataLoader().write_pickle(scales_df, 'scales')
DataLoader().write_pickle(full_df, 'full')
