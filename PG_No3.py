# -*- coding: utf-8 -*-
import PySimpleGUIWeb as sg

# ウィンドウの内容を定義する
layout = [[sg.Text("お名前は何ですか？")],
          [sg.Input(key='-入力-')],
          [sg.Text(size=(55,1), key='-出力-')],
          [sg.Button('はい'), sg.Button('終了')]]

# ウィンドウを作成する
window = sg.Window('ウィンドウタイトル',layout)

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
# ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください
    if event == sg.WINDOW_CLOSED or event == '終了':
        break

    # Output a message to the window
    window['-出力-'].update('ハロー ' + values['-入力-'] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()
