# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:31:04 2020

@author: GOlmos01
"""
from reportlab.pdfgen import canvas

def drawRulers(pdf):
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
    
fileName = 'test.pdf'
documentTitle = 'report_test'
title = 'Reporte Simple'
subTitle = 'Este es un reporte general simple'
textLines = [
    'Las inversiones estan bien',
    'Los rebates son un desorden',
    'Quién dejó la luz encendida, si la pieza estaba vacía?',
    'Quién apagó la luz?']
image = 'test_img.jpg'

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)

drawRulers(pdf)

pdf.drawString(250, 770, title)


pdf.save()
