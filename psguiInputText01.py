# -*- coding: utf-8 -*-
import PySimpleGUI as sg

layout = [[sg.InputText(default_text='ここで文字列を編集',
                       size=(35,1), key='tx1')],
        [sg.Button('read', key='btn1')]]


window = sg.Window('psguiInputText01', layout)

while True:
    event, values = window.read()
    print('イベント:', event,', 値:', values)
    if event == None:
        break

window.close()

