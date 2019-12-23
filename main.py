# -*- coding: utf-8 -*-

"""
Esta es la clase main.

"""

import pandas as pd
from dataloader import DataLoader
from client import Client

"""Raw data loading"""
scale_path = './Data/escalas_clean.csv'
full_db_path = './Data/full_db_clean.csv'

scales_df = DataLoader().load_scales(scale_path)
full_df = DataLoader().load_full_db(full_db_path)

"""Dataframe loading"""
# scales_df = DataLoader().load_pickle('scales')
# full_df = DataLoader().load_pickle('full')

"""DataFrame Writing"""
# DataLoader().write_pickle(scales_df, 'scales')
# DataLoader().write_pickle(full_df, 'full')

"""Data model construction"""

clients_list = []
suppliers_list = []
scales_lists = []

for index, row in full_df.iterrows():
    clients_list.append(Client(row['Cliente grupo 1'], row['Cliente Facturación'], 
                               row['Cliente Titular']))
