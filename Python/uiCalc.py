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

from typing import Any
import PySimpleGUI as sg
#Manual: https://www.pysimplegui.org/en/latest/

sg.theme('DarkAmber')

calcLayout = [
    #Menu Example: [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]])]],
    [sg.MenubarCustom([['File', ["Settings", "Exit"]], ['History']])],
    [sg.Input(size = (15, 5)), sg.Button("Calculate")],
    [sg.Button(" /  "), sg.Text("     "), sg.Button(" * "), sg.Text("     "), sg.Button("  - ")],
    [sg.Button(" 7 "), sg.Text("     "), sg.Button(" 8 "),sg.Text("     "), sg.Button(" 9 ")],
    [sg.Button(" 4 "), sg.Text("     "), sg.Button(" 5 "), sg.Text("     "), sg.Button(" 6 ")],
    [sg.Button(" 1 "), sg.Text("     "), sg.Button(" 2 "), sg.Text("     "), sg.Button(" 3 ")],
    [sg.Button(" 0 "), sg.Text("     "), sg.Button(" .  "), sg.Text("     "), sg.Button(" + ")],
    [sg.Output(size=(20,1), sbar_width=None)]
    ]

settLayout = [
    [sg.MenubarCustom(['Save and Exit'], ['Exit'])]
]

histLayout = [
    [sg.MenubarCustom(['Exit'])]
]

calcWin = sg.Window('Calculator', calcLayout)
settWin = sg.Window('Settings', settLayout)
histWin = sg.Window('History', histLayout)

while True:                             # The Event Loop
    event, values = calcWin.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break