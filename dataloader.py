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
        col_names = ['supplier_macro_group_name', 'supplier_group_name', 'year', 
                     'month_start', 'month_end', 'media_type', 
                     'supplier_com_name', 'supplier_rut', 'media_name', 
                     'bonif_type', 'min1', 'max1', 'bono1', 'min2', 'max2', 
                     'bono2', 'min3', 'max3', 'bono3', 'min4', 'max4', 
                     'bono4', 'min5', 'max5', 'bono5', 'min6', 'max6', 
                     'bono6', 'min7', 'max7', 'bono7', 'agreement_status', 
                     'agency', 'check_status']
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
        col_names =['Mes', 'Año', 'Pauta', 'Divisiones', 'Plan', 'Tema Plan', 
                    'JobNumber', 'Tema JobNumber', 'Presupuesto', 'Orden', 
                    'Rev. Orden', 'Período', 'Cliente Titular', 
                    'Cliente Facturación',  'Producto', 'Nº Pedido Cli.', 
                    'Nro Item', 'Detalle Item', 'Material', 'Campaña', 
                    'Proveedor', 'R.U.T.', 'Proveedor Real', 'Nombre del Medio', 
                    'Zona', 'Tipo de Medio', 'Contrato', 'Descripción', 
                    'SubContrato', 'Descripción2', 'Spots', 'Saldo Inicial', 
                    'Consumo', 'Saldo Actual', 'Facturable', 'Bonificable', 
                    'Intercambio', 'Inversión Total', 'VTR', 'AnoMes', 
                    'Subtotal', 'Estado', 'Revisión', 'Tipo Pub.', 
                    'Unidad de Medida', 'Macro Grupo de Productos', 
                    'Grupo de Productos', 'Forma de Pago (Pauta)', 
                    'Forma de Pago (Contrato)', 'Agencia X', 'Nº O.C.', 
                    'Nº Factura Medio', 'Importe F. Medio', 
                    'Tipo Facturación', 'Observaciones', 'USD Facturable', 
                    'USD Bonificable', 'USD Intercambio', 'USD Total', 
                    'Fac. Cliente', 'Fac. Serv. Ag.', 'A Vencer o Corriente', 
                    'Vencido 1 - 30', 'Vencido 31 - 60', 'Vencido 61 - 90', 
                    'Vencido 91 - 120', 'Vencido + 121', 'Pasa x Agencia']
        try:
            return pd.read_csv(path, sep=';', index_col=False, names=col_names)
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
                     'Orden', 'Rev. Orden', 'Periodo', 'Cliente grupo 1', 
                     'Cliente grupo 2', 'Cliente Titular', 'Cliente Facturacion', 
                     'Producto', 'Nº Pedido Cli.', 'Nro Item', 'Campaña', 
                     'Grupo proveedor titular', 'Proveedor', 'R.U.T. Proveedor', 
                     'Proveedor Real', 'Grupo proveedor real', 
                     'Nombre del Medio', 'Zona', 'Plataforma', 'MEDIO ON/OFF', 
                     'Clasificacion', 'Macro Clasificacion','Tipo de Medio', 
                     'Spots', 'Facturable', 'Inversion Total', 'Estado', 
                     'Macro Grupo de Productos', 'Grupo de Productos', 
                     'Forma de Pago (Pauta)', 'Forma de Pago (Contrato)', 
                     'Agencia X', 'Tipo Facturacion ', 'Observaciones', 
                     'Fac. Cliente', 'Fac. Serv. Ag.', 'ERROR?', 'Grupo',
                     'Proveedor agrupado', 'GRUPO TABLA RUT-TDM', 'MACRO GRUPO TABLA RUT-TDM', 
                     'TIPO BONIFICACION', 'Inv Total', 'Inv relativa', 
                     'Rebate total', 'Rebate relativo']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def load_db(self, path):
        col_names = ['Año', 'Mes', 
             'IDMesAñoBD', 'ID_TipoMedio_RUT', 'Pauta', 'Plan', 
             'Tema Plan', 'JobNumber', 'Tema JobNumber', 'Presupuesto', 
             'Orden', 'Rev. Orden', 'Periodo', 'Cliente grupo 1', 
             'Cliente grupo 2', 'Cliente Titular', 'Cliente Facturacion', 
             'Producto', 'Nº Pedido Cli.', 'Nro Item', 'Campaña', 
             'Grupo proveedor titular', 'Proveedor', 'R.U.T. Proveedor', 
             'Proveedor Real', 'Grupo proveedor real', 
             'Nombre del Medio', 'Zona', 'MEDIO ON/OFF', 'Tipo de Medio', 
             'Spots', 'Facturable', 'Inversion Total', 'Estado', 
             'Macro Grupo de Productos', 'Grupo de Productos', 
             'Forma de Pago (Pauta)', 'Forma de Pago (Contrato)', 
             'Agencia X', 'Tipo Facturacion ', 'Observaciones', 
             'Fac. Cliente', 'Fac. Serv. Ag.']
        try:
            return pd.read_csv(path, sep=';', names=col_names)
        except FileNotFoundError:
            print("Archivo no existe")
            return 0
    def load_month_adv(self, path):
        """
        Loads ADV data from CARAT, DentsuX, Deepblue, Iprospect, Amnet and Vizuem
        
        Parameters
        ----------
        path : path to the file.
        
        Returns
        -------
        DataFrame.
        
        """
        col_names =['Semana', 'Macro Agencia', 'Agencia', 'Mes/Año', 'Pauta', 
                    'Divisiones', 'Plan', 'Tema Plan', 'JobNumber', 
                    'Tema JobNumber', 'Presupuesto', 'Orden', 'Rev. Orden', 
                    'Período', 'Cliente grupo 1', 'Cliente grupo 2', 
                    'Cliente Titular', 'Cliente Facturación', 'Producto', 
                    'Nº Pedido Cli.', 'Nro Item', 'Detalle Item', 'Material', 
                    'Campaña', 'Proveedor', 'R.U.T.', 'Proveedor Real', 
                    'Nombre del Medio', 'Medio ON/OFF/PLATAFORMA', 
                    'Plataforma', 'Zona', 'Tipo de Medio', 'Clasificación', 
                    'Macro clasificación', 'Contrato', 'DescripciónX', 
                    'SubContrato', 'Descripción', 'Spots', 'Saldo Inicial', 
                    'Consumo', 'Saldo Actual', 'Facturable', 'Bonificable', 
                    'Intercambio', 'Inversion Total', 'VTR', 'AnoMes', 
                    'Subtotal', 'Estado', 'Revisión', 'Tipo Pub.', 
                    'Unidad de Medida', 'Macro Grupo de Productos', 
                    'Grupo de Productos', 'Forma de Pago (Pauta)', 
                    'Forma de Pago (Contrato)', 'Agencia X', 'Nº O.C.', 
                    'Nº Factura Medio', 'Importe F. Medio', 'Tipo Facturación', 
                    'Observaciones', 'USD Facturable', 'USD Bonificable', 
                    'USD Intercambio', 'USD Total', 'Fac. Cliente', 
                    'Fac. Serv. Ag.', 'Grupo', 'ID_Medio_Rut', 
                    'Macro Grupo Tabla', 'Grupo Tabla', 'TIPO BONIFICACIÓN', 
                    'Inversion total prov', 'Inversion relativa', 'Rebate total', 
                    'Rebate relativo']
        try:
            return pd.read_csv(path, sep=';', index_col=False, names=col_names)
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