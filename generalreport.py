# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:31:04 2020

@author: GOlmos01
"""

from dataloader import DataLoader
from data_processor import DataProcessor
import numpy as np
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame, PageTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import *
from reportlab.lib import utils, colors
from reportlab.pdfgen.canvas import Canvas

class GeneralReport():
    def draw_rulers(self, pdf):
        pdf.drawString(100, 810, 'x100')
        pdf.drawString(200, 810, 'x200')
        pdf.drawString(300, 810, 'x300')
        pdf.drawString(400, 810, 'x400')
        pdf.drawString(500, 810, 'x500')
        pdf.drawString(10, 100, 'y100')
        pdf.drawString(10, 200, 'y200')
        pdf.drawString(10, 300, 'y300')
        pdf.drawString(10, 400, 'y400')
        pdf.drawString(10, 500, 'y500')
        pdf.drawString(10, 600, 'y600')
        pdf.drawString(10, 700, 'y700')
        pdf.drawString(10, 800, 'y800')

    def add_header(self, my_canvas):
        #File info
        # my_canvas = Canvas("frame_demo.pdf", pagesize=letter, bottomup = 1)
        page_width, page_height = letter #keep for later
        styles = getSampleStyleSheet()
        normal = styles['Normal']
        normal.alignment = TA_LEFT
        centered_heading = styles['Heading1']
        centered_heading.alignment = TA_CENTER
        centered_normal = styles['Normal']
        centered_normal.alignment = TA_CENTER
        heading = styles['Heading1']
        
        #Information about the content
        title = "Reporte Semanal"
        author = "Gerardo Olmos"
        email = "gerardo.olmos@dentsuaegis.com"
        formatted_time = time.ctime()
        
        #Frames - header
        left_frame = Frame(inch, 8*inch, width=2*inch, height=1.5*inch, showBoundary=0)
        center_frame = Frame(3*inch, 8*inch, width=2.5*inch, height=1.5*inch, showBoundary=0)
        right_frame = Frame(5.5*inch, 8*inch, width=2*inch, height=1.5*inch, showBoundary=0)

        #Flowable lists
        left_flowables = []
        center_flowables = []
        right_flowables = []

        #Header Logos
        logo_carat = "Reports/imgs/carat_logo.png"
        logo_amplifi = "Reports/imgs/amplifi_logo.png"
        
        img = utils.ImageReader(logo_carat)
        img_width, img_height = img.getSize()
        desired_width = 1*inch
        aspect = img_height / float(img_width)
        img = Image(logo_carat, width=desired_width,
        height=(desired_width * aspect))
        left_flowables.append(img)
        
        left_flowables.append(Spacer(1, 0.1*inch))
        
        img = utils.ImageReader(logo_amplifi)
        img_width, img_height = img.getSize()
        desired_width = 1*inch
        aspect = img_height / float(img_width)
        img = Image(logo_amplifi, width=desired_width,
        height=(desired_width * aspect))
        left_flowables.append(img)
        left_flowables.append(Spacer(1, 0.1*inch))
        
        # Paragraphs
        left_flowables.append(Paragraph(author, normal))   
        normal.fontSize = 8
        left_flowables.append(Paragraph(email, normal))
        normal.fontSize = 10        
        center_flowables.append(Paragraph(title, centered_heading))
        right_flowables.append(Paragraph(formatted_time, centered_normal))
        
        # Add from lists
        left_frame.addFromList(left_flowables, my_canvas)
        center_frame.addFromList(center_flowables, my_canvas)
        right_frame.addFromList(right_flowables, my_canvas)
        # my_canvas.save()
        
    def add_group_share(self, canvas, img_path, table_path, title):
        #File info
        page_width, page_height = letter #keep for later
        styles = getSampleStyleSheet()
        normal = styles['Normal']
        normal.alignment = TA_LEFT
        centered_heading = styles['Heading1']
        centered_heading.alignment = TA_CENTER
        centered_normal = styles['Normal']
        centered_normal.alignment = TA_CENTER
        heading = styles['Heading1']

        # Frames & flowables
        top_frame = Frame(inch, 7.5*inch, width=1.5*inch, height=0.5*inch, showBoundary=1)
        left_frame = Frame(inch, 5*inch, width=3*inch, height=2.5*inch, showBoundary=1)
        right_frame = Frame(4*inch, 5*inch, width=4*inch, height=2.5*inch, showBoundary=1)
        
        top_flowables = []
        left_flowables = []
        right_flowables = []
        
        # Brief
        # get_brief()
        title = title
        brief_text = "Quien hace tanta bulla y ni deja."
        top_flowables.append(Paragraph(title, normal))   
        
        
        # Chart
        img = utils.ImageReader(img_path)
        img_width, img_height = img.getSize()
        desired_width = 3*inch
        aspect = img_height / float(img_width)
        img = Image(img_path, width=desired_width,
        height=(desired_width * aspect))
        right_flowables.append(img)
        
        # Table
        img = utils.ImageReader(table_path)
        img_width, img_height = img.getSize()
        desired_width = 2.9*inch
        aspect = img_height / float(img_width)
        img = Image(table_path, width=desired_width,
        height=(desired_width * aspect))
        left_flowables.append(Spacer(1, 0.1*inch))
        left_flowables.append(img)
        
        # Add from lists
        top_frame.addFromList(top_flowables, canvas)
        left_frame.addFromList(left_flowables, canvas)
        right_frame.addFromList(right_flowables, canvas)
        # canvas.save() #TODO sacar esta linea
    def add_client_share(self, canvas, img_path, table_path, title):
        #File info
        page_width, page_height = letter #keep for later
        styles = getSampleStyleSheet()
        normal = styles['Normal']
        normal.alignment = TA_LEFT
        centered_heading = styles['Heading1']
        centered_heading.alignment = TA_CENTER
        centered_normal = styles['Normal']
        centered_normal.alignment = TA_CENTER
        heading = styles['Heading1']

        # Frames & flowables
        top_frame = Frame(inch, 7.5*inch, width=1.5*inch, height=0.5*inch, showBoundary=1)
        left_frame = Frame(inch, 3.5*inch, width=3*inch, height=4*inch, showBoundary=1)
        right_frame = Frame(4*inch, 3.5*inch, width=4*inch, height=4*inch, showBoundary=1)
        #TODO center vertical
        top_flowables = []
        left_flowables = []
        right_flowables = []
        
        # Brief
        # get_brief()
        title = title
        brief_text = "Quien hace tanta bulla y ni deja."
        top_flowables.append(Paragraph(title, normal))   
        
        
        # Chart
        img = utils.ImageReader(img_path)
        img_width, img_height = img.getSize()
        desired_width = 3.9*inch
        aspect = img_height / float(img_width)
        img = Image(img_path, width=desired_width,
        height=(desired_width * aspect))
        right_flowables.append(img)
        
        # Table
        img = utils.ImageReader(table_path)
        img_width, img_height = img.getSize()
        desired_width = 2.9*inch
        aspect = img_height / float(img_width)
        img = Image(table_path, width=desired_width,
        height=(desired_width * aspect))
        left_flowables.append(Spacer(1, 0.1*inch))
        left_flowables.append(img)
        
        # Add from lists
        top_frame.addFromList(top_flowables, canvas)
        left_frame.addFromList(left_flowables, canvas)
        right_frame.addFromList(right_flowables, canvas)
        # canvas.save() #TODO sacar esta linea
        
    def generate_imgs(self, df, scales_path):
        global dict_images
        # Group share
        img_path = DataProcessor().get_group_share(df, df, fig_num)
        table_path = DataProcessor().get_group_share_table(df, df, fig_num)
        dict_images['group_share_chart'] = img_path
        dict_images['group_share_table'] = table_path

        # Client share
        img_path = DataProcessor().get_client_share(df, df, fig_num)
        table_path = DataProcessor().get_client_share_table(df, df, fig_num)
        dict_images['client_share_chart'] = img_path
        dict_images['client_share_table'] = table_path
        
        # Supplier share
        img_path = DataProcessor().get_supplier_share(df, df, fig_num) #TODO change to supplier share
        table_path = DataProcessor().get_supplier_share_table(df, df, fig_num) #TODO change to supplier table
        dict_images['supplier_share_chart'] = img_path
        dict_images['supplier_share_table'] = table_path
    
    def insert_data_in_canvas(self, my_canvas):
        global dict_images
        GeneralReport().add_group_share(my_canvas, dict_images['group_share_chart'], dict_images['group_share_table'], 'Grupos')
        my_canvas.showPage()
        GeneralReport().add_client_share(my_canvas, dict_images['client_share_chart'], dict_images['client_share_table'], 'Clientes')
        my_canvas.showPage()
        GeneralReport().add_client_share(my_canvas, dict_images['supplier_share_chart'], dict_images['supplier_share_table'], 'Proveedores')
   
    def report_demo(self, df_path, scales_path):
        my_canvas = Canvas("report_demo.pdf", pagesize=letter)
        df = DataLoader().load_month_adv(df_path)
        
        # Header
        GeneralReport().add_header(my_canvas)
        
        #Get data
        GeneralReport().generate_imgs(df, "scale_path")
        
        # Add info to canvas
        GeneralReport().insert_data_in_canvas(my_canvas)
        
        # Save canvas
        my_canvas.save()
    
dict_images = {}
db_path = './Data/montly_data/01-2020/consolidado_01-2020.csv'
scale_path = './Data/supplier_data_v1.1/suppliers.csv'
fig_num = 1 #TODO make global var
report = GeneralReport().report_demo(db_path, "scale_path")