# -*- coding: utf-8 -*-
import PySimpleGUI as sg

layout = [[sg.InputText(default_text='',
                       size=(35,1), 
                       enable_events=True, key='tx1')],
        [sg.Button('文1', key='bn1'), sg.Button('文2', key='bn2'),
         sg.Button('clear', key='bn3'), sg.Button('Quit', key='bn4')]]

window = sg.Window('psguiInputText03', layout)

while True:
    event, values = window.read()
    print('イベント:', event,', 値:', values)
    if event in (None, 'bn4'):
        break
    elif event == 'bn1':
        window['tx1'].Update('お誕生日おめでとう')
    elif event == 'bn2':
        window['tx1'].Update('心よりお祝い申し上げます')
    elif event == 'bn3':
        window['tx1'].Update('')
    
window.close()
