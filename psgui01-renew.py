# -*- coding: utf-8 -*-
import PySimpleGUI as sg
sg.theme('Dark Brown')

layout = [[sg.Text('これはPySimpleGUIを使ったサンプルプログラムです。',
                   enable_events=True, key='tx1')],
          [sg.Button('Quit', size=(15,1), key='btn1'), 
           sg.Button('OK', size=(15,1), key='btn2')]]

window = sg.Window('Sample01-renew', layout) 
#'Sample01'がウインドウのタイトル、layoutで前段の情報を加えている

while True:
    event, values = window.read()
    print('イベント:', event,', 値:', values)
    if event in (None,'btn1'):
        print('終了します')
        break

window.close()