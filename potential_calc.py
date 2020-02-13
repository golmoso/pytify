# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:02:28 2020

@author: GOlmos01
"""

import pandas as pd

class PotencialCalc():
    def load_scales(self, path):
        col_names = ['MACRO GRUPO TABLA RUT-TDM', 'GRUPO TABLA RUT-TDM', 
                     'ID_TipoMedio_RUT', 'TIPO DE MEDIO', 'Total', 
                     'TIPO DE BONIFICACIÓN', 'MIN1', 'TRAMO1', 'MAX1', 
                     'BONI1', 'MIN2', 'TRAMO2', 'MAX2', 'BONI2', 'MIN3', 
                     'TRAMO3', 'MAX3', 'BONI3', 'MIN4', 'TRAMO4', 'MAX4', 
                     'BONI4', 'MIN5', 'TRAMO5', 'MAX5', 'BONI5', 'MIN6', 
                     'TRAMO6', 'MAX6', 'BONI6', 'MIN7', 'TRAMO7', 'MAX7', 
                     'BONI7', 'BONOS', 'TOTAL ESCALAS', 'REBATE NETO', 
                     'ESTA EN TRAMO?']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def as_int(self, df):
        df['MIN1'] = pd.to_numeric(df['MIN1'])
        df['MIN2'] = pd.to_numeric(df['MIN2'])
        df['MIN3'] = pd.to_numeric(df['MIN3'])
        df['MIN4'] = pd.to_numeric(df['MIN4'])
        df['MIN5'] = pd.to_numeric(df['MIN5'])
        df['MIN6'] = pd.to_numeric(df['MIN6'])
        df['MIN7'] = pd.to_numeric(df['MIN7'])
        df['MAX1'] = pd.to_numeric(df['MAX1'])
        df['MAX2'] = pd.to_numeric(df['MAX2'])
        df['MAX3'] = pd.to_numeric(df['MAX3'])
        df['MAX4'] = pd.to_numeric(df['MAX4'])
        df['MAX5'] = pd.to_numeric(df['MAX5'])
        df['MAX6'] = pd.to_numeric(df['MAX6'])
        df['MAX7'] = pd.to_numeric(df['MAX7'])
        df['BONI1'] = df['BONI1'].astype(float)
        df['BONI2'] = df['BONI2'].astype(float)
        df['BONI3'] = df['BONI3'].astype(float)
        df['BONI4'] = df['BONI4'].astype(float)
        df['BONI5'] = df['BONI5'].astype(float)
        df['BONI6'] = df['BONI6'].astype(float)
        df['BONI7'] = df['BONI7'].astype(float)
        return df
    def iterate_on_suppliers(self, df):
        for index, row in df.iterrows():
            print ('Iniciando proceso para ' + row['GRUPO TABLA RUT-TDM'])
            tmp = 0
            for i in range(0,500000000, 100000):
                if i >= row['MIN1'] and i < row['MAX1']:
                    tmp = tmp + i*row['BONI1']
                if i >= row['MIN2'] and i < row['MAX2']:
                    tmp = tmp + i*row['BONI2']
                if i >= row['MIN3'] and i < row['MAX3']:
                    tmp = tmp + i*row['BONI3']
                if i >= row['MIN4'] and i < row['MAX4']:
                    tmp = tmp + i*row['BONI4']
                if i >= row['MIN5'] and i < row['MAX5']:
                    tmp = tmp + i*row['BONI5']
                if i >= row['MIN6'] and i < row['MAX6']:
                    tmp = tmp + i*row['BONI6']
                if i >= row['MIN7'] and i < row['MAX7']:
                    tmp = tmp + i*row['BONI7']
                df.at[index, 'Potential'] = tmp
        return df
                

scale_path = './Data/supplier_data_v1.1/suppliers.csv'

op = PotencialCalc()
scales = op.load_scales(scale_path)
scales = op.as_int(scales)
scales['Potential'] = 0
op.iterate_on_suppliers(scales)


