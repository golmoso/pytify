# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:31:52 2019

@author: GOlmos01

a.	Composición de la base de datos
b.	Inv. Total por grupo - CHECK
c.	Inv. Total por medio - 
d.	Inv. Total por tipo de medio - CHECK
e.	Top clients - CHECK
f.	Inv. Mensual por grupo - CHECK
g.	Inv. Mensual por grupo de medio (ON-OFF)
h.	Inv. Mensual por tipo de medio - CHECK

Pasar a html

Html a pdf

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import table


class DataProcessor():
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
                                 index=['Mes'], columns=[columns], 
                                 aggfunc=np.sum)
        return monthly
    def time_share_by(self, df, time_period, columns):
        """
        Get the 'time_period' ('Mes', 'Año', 'Semana', 'Dia') share by 'columns'

        Parameters
        ----------
        df : Full DB DataFrame.
        columns : pivot variable.

        Returns
        -------
        share : pivot table DataFrame.

        """
        data = pd.pivot_table(df, values='Inversion Total', 
                                 index=[time_period], columns=[columns], 
                                 aggfunc=np.sum)
        return data
    def get_some_top(self, df, subject, amount):
        """
        Get the top amount of a certain subject.

        Parameters
        ----------
        df : Full DB Dataframe.
        subject : filter subject.
        amount : amount of object you want the 'top' to be comformed by.

        Returns
        -------
        top : dataframe.

        """
        top = df.groupby([subject]).sum()[:amount]
        return top
    def some_by_group(self, df, subject):
        """
        Get the share by group g_num

        Parameters
        ----------
        df : Full DB DataFrame.
        subject : pivot variable.

        Returns
        -------
        share : DataFrame.

        """
        share = pd.pivot_table(df, values='Inversion Total', 
                               index=[subject], columns=['Grupo'], 
                               aggfunc=np.sum)
        return share
        
    def generate_imgs(self, full_df, scale_df):
        """
        - Group share
            - weekly
            - cumulative
        - Generate client share
            - weekly
            - cumulative
        - Generate supplier share
            - weekly
            - cumulative
        - Generate supplier agreements
            - speedometer
        - By group
            - type of media
            - clients
            - suppliers
        - Investments
            - percentual difference between last year

        Returns
        -------
        int
            Returns 1 when operation was successful.

        """
        figure_number = 1
        
        # Exclude values that represent less than 1 percent
        def autopct_more_than_1(pct):
            return ('%1.f%%' % pct) if pct > 1 else ''
        
        # Group share cumulative
        share_by_group = DataProcessor().anual_share_by(full_df, 'Grupo')
        plt.figure(figure_number)
        plt.pie(share_by_group['Inversion Total'], labels=share_by_group.index, 
                startangle=90, autopct='%1.1f%%')
        plt.title("Group Share")
        plt.figtext(0.15, 0.09, s='Fig.%i Distribución por grupo de la inversión acumulada' % figure_number)
        plt.savefig("group_share_cum.png")
        
        plt.show()

        figure_number = figure_number + 1
        
        # TODO Group share weekly
        
        ######################## Client share
        share_by_client = DataProcessor().anual_share_by(full_df, 'Cliente grupo 1')
        fig1, ax = plt.subplots()
        
        # Normalize and sort values
        investment_values = share_by_client['Inversion Total'].values
        share_by_client['Normalized'] = investment_values/investment_values.sum()*100
        share_by_client = share_by_client.sort_values(['Normalized'], ascending= False)
    
        # Plot and labels
        p,t,a = ax.pie(share_by_client['Normalized'].values,
                       autopct=autopct_more_than_1)
        ax.axis('equal')
        h,l = zip(*[(h,lab) for h,lab,i in zip(p,share_by_client.index.values,
                                               share_by_client['Normalized'].values) if i > 1])
        ax.legend(h, l,loc="best", bbox_to_anchor=(1,1))

        # Plot info
        plt.figure(figure_number)
        plt.title("Client Share")
        plt.figtext(0.15, 0.09, s='Fig.%i Distribución por cliente de la inversión acumulada' % figure_number)
        plt.savefig("client_share_cum.png")
        plt.show()
        figure_number = figure_number + 1
        ######################## END Client share

        # TODO Client share weekly

        
         ######################## Supplier share
        share_by_supplier = DataProcessor().anual_share_by(full_df, 'Proveedor agrupado')
        fig1, ax = plt.subplots()
        
        # Normalize and sort values
        investment_values = share_by_supplier['Inversion Total'].values
        share_by_supplier['Normalized'] = investment_values/investment_values.sum()*100
        share_by_supplier = share_by_supplier.sort_values(['Normalized'], ascending= False)
    
        # Plot and labels
        p,t,a = ax.pie(share_by_supplier['Normalized'].values,
                       autopct=autopct_more_than_1)
        ax.axis('equal')
        h,l = zip(*[(h,lab) for h,lab,i in zip(p,share_by_supplier.index.values,
                                               share_by_supplier['Normalized'].values) if i > 1])
        ax.legend(h, l,loc="best", bbox_to_anchor=(1,1))

        # Plot info
        plt.figure(figure_number)
        plt.title("Supplier Share")
        plt.figtext(0.15, 0.09, s='Fig.%i Distribución por proveedor de la inversión acumulada' % figure_number)
        plt.savefig("supplier_share_cum.png")
        plt.show()
        figure_number = figure_number + 1
        ######################## END Supplier share
        
        # TODO Supplier share weekly
        
        # TODO Suppliers speedometers
        
        ####################### Type of media share by group    
        share_typeof_media = DataProcessor().some_by_group(full_df, 'Tipo de Medio')
        for group_i in range(1, 6):
            # Get group table and fill na
            share_tmp = share_typeof_media['CARAT %d' %(group_i)].fillna(0)
            
            # Normalize and sort values
            # share_tmp['Normalized'] = share_tmp.values/share_tmp.values.sum()*100
            # share_tmp = share_tmp.sort_values(['Normalized'], ascending= False)
    
            # Plot and labels
            p,t,a = ax.pie(share_tmp.values,
                            autopct=autopct_more_than_1)
            ax.axis('equal')
            he,lo = zip(*[(he,lab) for he,lab,i in zip(p,share_tmp.index.values,
                                                    share_tmp.values) if i > 1])
            ax.legend(he, lo,loc="best", bbox_to_anchor=(1,1))
            plt.figure(figure_number)
            plt.pie(share_tmp.values, labels=share_tmp.index, 
                    startangle=90, autopct='%1.1f%%')       
            plt.title('Type of Media CARAT %d' %(group_i))
            plt.figtext(0.15, 0.09, s='Fig.%i Distribución por grupo de la inversión acumulada' % figure_number)
            plt.savefig('group%d_media_share.png' %(group_i))
            plt.show()
            figure_number = figure_number + 1
            ####################### END Type of media share by group    

        
        # TODO Share clients by group
        # TODO Share suppliers by group
        # Percentual differences with 2019 by group

    def get_group_share(self, full_df, scale_df, fig_num):
        """

        Parameters
        ----------
        full_df : Pandas DataFrame.
        scale_df : Pandas DataFrame.
        fig_num : int.

        Returns
        -------
        img_path = string.

        """
        
        # Exclude values that represent less than 1 percent
        def autopct_more_than_1(pct):
            return ('%1.f%%' % pct) if pct > 1 else ''
        
        # Group share cumulative
        share_by_group = DataProcessor().anual_share_by(full_df, 'Grupo')
        img_path = "group_share_pie.png"
    
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        wedges, texts, autotexts = ax.pie(share_by_group, autopct=autopct_more_than_1, textprops=dict(color="w"))
        ax.legend(wedges, share_by_group.index,
                  title="Grupo",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.setp(autotexts, size=9, weight="bold")
        ax.set_title("Group share")
        plt.savefig(img_path)
        plt.show()
        return img_path
        
        # # Group share cumulative
        # share_by_group = DataProcessor().anual_share_by(full_df, 'Grupo')
        # plt.pie(share_by_group['Inversion Total'], labels=share_by_group.index, 
        #         startangle=90, autopct='%1.1f%%')
        # plt.title("Group Share")
        # img_path = "group_share_pie.png"
        # plt.savefig(img_path)
        # plt.show()
        # return img_path
    def get_group_share_table(self, full_df, scale_df, fig_num):
        share_by_group = DataProcessor().anual_share_by(full_df, 'Grupo')
        fig, ax = plt.subplots(figsize=(3, 2)) # set size frame
        # fig, ax = plt.subplots() # set size frame
        img_path = "group_share_table.png"
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis
        ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
        tabla = table(ax, share_by_group, loc='upper right', colWidths=[0.17]*len(share_by_group.columns))  # where df is your data frame
        tabla.auto_set_font_size(False) # Activate set fontsize manually
        tabla.set_fontsize(10) # if ++fontsize is necessary ++colWidths
        tabla.scale(3, 1.2) # change size table
        plt.savefig(img_path, transparent=True)
        return img_path
    def get_client_share(self, full_df, scale_df, fig_num):
        """

        Parameters
        ----------
        full_df : Pandas DataFrame.
        scale_df : Pandas DataFrame.
        fig_num : int.

        Returns
        -------
        img_path = string.

        """
        # Exclude values that represent less than 1 percent
        def autopct_more_than_1(pct):
            return ('%1.f%%' % pct) if pct > 2 else ''
        
        # Client share cumulative
        share_by_client = DataProcessor().anual_share_by(full_df, 'Cliente grupo 1')
        img_path = "client_share_pie.png"
    
        # Normalize and sort values
        investment_values = share_by_client['Inversion Total'].values
        share_by_client['Normalized'] = investment_values/investment_values.sum()*100
        share_by_client = share_by_client.sort_values(['Normalized'], ascending= False)
        
        # Plot and labels
        fig1, ax = plt.subplots(figsize=(9, 5))
        p,t,a = ax.pie(share_by_client['Normalized'].values,
                       autopct=autopct_more_than_1, textprops=dict(color="w"))
        ax.axis('equal')
        h,l = zip(*[(h,lab) for h,lab,i in zip(p,share_by_client.index.values,
                                               share_by_client['Normalized'].values) if i > 1])
        ax.legend(h, l,loc="best", bbox_to_anchor=(1,1))
        plt.setp(a, size=9, weight="bold")
        ax.set_title("Client share")
        
        # Save img
        plt.savefig(img_path)
        plt.show()
        return img_path

        
        ######################## Client share
        share_by_client = DataProcessor().anual_share_by(full_df, 'Cliente grupo 1')
        fig1, ax = plt.subplots()
        
        # Normalize and sort values
        investment_values = share_by_client['Inversion Total'].values
        share_by_client['Normalized'] = investment_values/investment_values.sum()*100
        share_by_client = share_by_client.sort_values(['Normalized'], ascending= False)
    
        # Plot and labels
        p,t,a = ax.pie(share_by_client['Normalized'].values,
                        autopct=autopct_more_than_1)
        ax.axis('equal')
        h,l = zip(*[(h,lab) for h,lab,i in zip(p,share_by_client.index.values,
                                                share_by_client['Normalized'].values) if i > 1])
        ax.legend(h, l,loc="best", bbox_to_anchor=(1, 0, 0.5, 1))
        # ax.legend(wedges, share_by_client.index,
        #   title="Cliente",
        #   loc="center left",
        #   bbox_to_anchor=(1, 0, 0.5, 1))
        plt.setp(t, size=9, weight="bold")

        # Plot info
        plt.title("Client Share")
        img_path = "client_share_cum.png"
        plt.savefig(img_path)
        plt.show()
        return img_path
        ######################## END Client share
    
    def get_client_share_table(self, full_df, scale_df, fig_num):
        share_by_client = DataProcessor().anual_share_by(full_df, 'Cliente grupo 1')
        share_by_client = share_by_client.sort_values(['Inversion Total'], ascending=False)[:15]
        fig, ax = plt.subplots(figsize=(4.2, 5)) # set size frame
        img_path = "client_share_table.png"
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis
        ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
        tabla = table(ax, share_by_client, loc='upper right', colWidths=[0.17]*len(share_by_client.columns))  # where df is your data frame
        tabla.auto_set_font_size(False) # Activate set fontsize manually
        tabla.set_fontsize(10) # if ++fontsize is necessary ++colWidths
        tabla.scale(2, 1.5) # change size table
        plt.savefig(img_path, transparent=True)
        return img_path
    