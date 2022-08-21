__name__ = '__main__'

###########################################################
"""
Author: Kenneth Livermore aka Tr8demark
Date: 08/22/22
Title: UICalc
Language: Python3
"""
###########################################################
"""
Pseudocode:
A field that updates when numbers are entered at the top.
A 3x5 grid of numbers and operands that can be selected by keypress or mouse.
Probably just use the top field as a python wrapper.
"""

import PySimpleGUI as sg
#Manual: https://www.pysimplegui.org/en/latest/

layout = [
    [sg.Button("/"), sg.Button("*"), sg.Button("-")],
    [sg.Button("7"), sg.Button("8"), sg.Button("9")],
    [sg.Button("4"), sg.Button("5"), sg.Button("6")],
    [sg.Button("1"), sg.Button("2"), sg.Button("3")],
    [sg.Button("0"), sg.Button("."), sg.Button("+")],
    [sg.Output(size = (10, 5))]
    ]

window = sg.Window('File Compare', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break