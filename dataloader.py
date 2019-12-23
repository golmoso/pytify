# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:05:44 2019

@author: GOlmos01
"""

import pandas as pd

class DataLoader():
    def load_scales(self, path):
        """
        DataLoader for scales file
        
        Parameters
        ----------
        path : path to the file.
        col_names : column names.
        separator : character that separates each value.

        Returns
        -------
        DataFrame containing data.

        """
        #scale_path = './Data/escalas2019.csv'
        col_names = ['supplier_group_name', 'year', 'media_type', 
                     'supplier_com_name', 'supplier_rut', 'media_name', 
                     'bonif_type', 'min1', 'max1', 'bono1', 'min2', 'max2', 
                     'bono2', 'min3', 'max3', 'bono3', 'min4', 'max4', 
                     'bono4', 'min5', 'max5', 'bono5', 'min6', 'max6', 
                     'bono6', 'min7', 'max7', 'bono7', 'agreement_status']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def load_adv(self, path):
        """
        Loads ADV data from CARAT, DentsuX, Deepblue, Iprospect, Amnet and Vizuem

        Parameters
        ----------
        path : path to the file.

        Returns
        -------
        DataFrame.

        """
        col_names = ['Mes/Año', 'Pauta', 
                     'Divisiones', 'Plan', 'Tema Plan', 'JobNumber', 
                     'Tema JobNumber', 'Presupuesto', 'Orden', 'Rev. Orden', 
                     'Período', 'Cliente Titular', 'Cliente Facturación', 
                     'Producto', 'Nº Pedido Cli.', 'Nro Item', 
                     'Detalle Item', 'Material', 'Campaña', 'Proveedor', 
                     'R.U.T.', 'Proveedor Real', 'Nombre del Medio', 
                     'Zona', 'Tipo de Medio', 'SubContrato', 
                     'Descripción', 'Spots', 'Facturable', 
                     'Bonificable', 'Intercambio', 'Inversión Total', 
                     'VTR', 'AnoMes', 'Subtotal', 'Estado', 
                     'Revisión', 'Tipo Pub.', 'Unidad de Medida', 
                     'Macro Grupo de Productos', 'Grupo de Productos', 
                     'Forma de Pago (Pauta)', 'Agencia', 'Nº O.C.', 
                     'Nº Factura Medio', 'Importe F. Medio', 
                     'Tipo Facturación']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def load_padd(self, path):
        col_names = ['Razon Social CLIENTE', 'Cliente', 'ANO', 'Mes', 
                     'Nro de Ctto.', 'Nro de Orden', 'Version', 'Medio', 
                     'Razon Soc.Proveedor', 'Proveedor', 'RUT Prov.', 'Soporte', 
                     'Campana', 'OC Cliente', 'Producto', 'Age.Crea', 'Inv.Neta', 
                     'Tipo Compra', 'Total Unidades', 'Nro Fact.Prov.', 
                     'Fecha Fact.Prov.', 'Nro Fact.Age.', 'Fecha', 'Fact.Age.', 
                     'Monto Neto Fact.', 'Tipo Ctto.', 'Usuario Grupo']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def load_full_db(self, path):
        col_names = ['Macro BD', 'BD', 'Macro Agencia', 'Agencia', 'Año', 'Mes', 
                     'IDMesAñoBD', 'ID_TipoMedio_RUT', 'Pauta', 'Plan', 
                     'Tema Plan', 'JobNumber', 'Tema JobNumber', 'Presupuesto', 
                     'Orden', 'Rev. Orden', 'Período', 'Cliente grupo 1', 
                     'Cliente grupo 2', 'Cliente pseudo facturacion', 
                     'Cliente Titular', 'Cliente Facturación', 
                     'Producto', 'Nº Pedido Cli.', 'Nro Item', 'Campaña', 
                     'Grupo proveedor titular', 'Proveedor', 'R.U.T. Proveedor', 
                     'Proveedor Real', 'Grupo proveedor real', 
                     'Nombre del Medio', 'Zona', 'MEDIO ON/OFF', 'Tipo de Medio', 
                     'Spots', 'Facturable', 'Inversión Total', 'Estado', 
                     'Macro Grupo de Productos', 'Grupo de Productos', 
                     'Forma de Pago (Pauta)', 'Forma de Pago (Contrato)', 
                     'Agencia X', 'Tipo Facturación ', 'Observaciones', 
                     'Fac. Cliente', 'Fac. Serv. Ag.', 'ERROR?', 'Grupo', 
                     'GRUPO TABLA RUT-TDM', 'GRUPO TABLA', 'TIPO BONIFICACIÓN']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def load_pickle(self, file):
        """
        Reads DataFrame
        
        Parameters
        ----------
        file : scales or full.

        Returns
        -------
        DataFrame containing respective data

        """
        if file == 'scales':
            return pd.read_pickle('scales_db')
        elif file == 'full':
            return pd.read_pickle('full_db')
        return 0
    def write_pickle(self, df, file):
        """
        Writes DataFrame

        Parameters
        ----------
        df : dataframe.
        file : scales or full.

        Returns
        -------
        Nothing.

        """
        if file == 'scales':
            return df.to_pickle('scales_db')
        elif file == 'full':
            return df.to_pickle('full_db')
        return 0