# -*- coding: utf-8 -*-
import PySimpleGUI as sg

layout = [[sg.Checkbox('項目11'), sg.Checkbox('項目12'), sg.Checkbox('項目13')],
          [sg.Radio('項目21', group_id='g1', default=True),
           sg.Radio('項目22', group_id='g1'), sg.Radio('項目23', group_id='g1')],
          [sg.Button('Check')]]

window = sg.Window('psguiButtons03', layout)

while True:
    event, values = window.read()
    print('イベント:', event,', 値:', values)
    if event == None:
        break
    
window.close()
