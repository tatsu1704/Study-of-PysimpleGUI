# -*- coding: utf-8 -*-
import PySimpleGUI as sg

itm = [1,2,3,'文字列1','文字列2','文字列3',['概ね','どんな型でも','項目にできます']]

layout = [[sg.Listbox(itm, size=(35,7),
                      default_values=[['概ね','どんな型でも','項目にできます']],
                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE),
        sg.Button('Check')]]


window = sg.Window('psguiListbox01', layout)

while True:
    event, values = window.read()
    print('イベント:', event,', 値:', values)
    if event == None:
        break
    
window.close()
