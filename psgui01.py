# -*- coding: utf-8 -*-
import PySimpleGUI as sg

layout = [[sg.Text('これはPySimpleGUIを使ったサンプルプログラムです。')],
          [sg.Button('Quit'), sg.Button('OK')]]

window = sg.Window('Sample01', layout) 
#'Sample01'がウインドウのタイトル、layoutで前段の情報を加えている

while True:
    event, values = window.read()
    print('イベント:', event,', 値:', values)
    if event in (None,'Quit'):
        print('終了します')
        break

window.close()