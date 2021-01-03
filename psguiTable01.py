# -*- coding: utf-8 -*-
import PySimpleGUI as sg

T = [[x+20*y for x in range(20)] for y in range(50)]
H = [chr(65+x) for x in range(20)]

L = [[sg.Table(T, headings=H, auto_size_columns=False, vertical_scroll_only=False,
               def_col_width=5,
               num_rows=10,
               display_row_numbers=True,
               )]]

window = sg.Window('psguiTable01.py', L, resizable=True, size=(400,240))

while True:
    event, values = window.read()
    if event == None:
        break
    
window.close()
