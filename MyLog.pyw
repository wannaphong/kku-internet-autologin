# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import threading
from login import login_cli
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('User'), sg.InputText(key='user')],
            [sg.Text('Password'), sg.InputText('', key='password', password_char='*')],
            [sg.OK(), sg.Cancel()]]
thread=None
# Create the Window
window = sg.Window('KKU Internet Autologin', layout)
# Event Loop to process "events"
while True:             
    event, values = window.Read()
    if event in (None, 'Cancel'):
        print("No")
        if thread!=None:
            thread.join()
        break
    if 'user' in values.keys() and 'password' in values.keys():
        sg.PopupOK('ระบบกำลัง Login')
        thread = threading.Thread(target=login_cli, args=[values['user'],values['password']])
        thread.start()

window.Close()