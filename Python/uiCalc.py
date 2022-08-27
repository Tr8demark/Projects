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

sg.theme('DarkAmber')

calcLayout = [
    #Menu Example: [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]])]],
    [sg.MenubarCustom(
        [['File', ["Settings", "Exit",]],
        ['Help', ["About...",]]])],
    [sg.Input(size = (15, 5), k = '-INPUT-'), sg.Button("Calculate", k = '-CALC-'), sg.Button("History", k = '-HIST-')],
    [sg.Button(" / ", k = '-DIV-'), sg.Text("      "), sg.Button(" x ", k = '-MULTI-'), sg.Text("     "), sg.Button(" -  ", k = ' -SUB-')],
    [sg.Button(" 7 ", k = '-7-'), sg.Text("     "), sg.Button(" 8 ", k = '-8-'),sg.Text("     "), sg.Button(" 9 ", k = '-9-')],
    [sg.Button(" 4 ", k = '-4-'), sg.Text("     "), sg.Button(" 5 ", k = '-5-'), sg.Text("     "), sg.Button(" 6 ", k = '-6-')],
    [sg.Button(" 1 ", k = '-1-'), sg.Text("     "), sg.Button(" 2 ", k = '-2-'), sg.Text("     "), sg.Button(" 3 ", k = '-3-')],
    [sg.Button(" 0 ", k = '-0-'), sg.Text("     "), sg.Button(" .  ", k = '-DOT-'), sg.Text("     "), sg.Button(" + ", k = '-ADD-')],
    [sg.Output(size=(20,1), sbar_width=None)]
    ]

settLayout = [
    [sg.MenubarCustom(
        [["File", ['Save and Exit'], ['Exit']]])]
]

histLayout = [
    [sg.MenubarCustom(
        [["File", ["Exit"],["Test"]]])]
]

calcWin = sg.Window('Calculator', calcLayout)
settWin = sg.Window('Settings', settLayout)
histWin = sg.Window('History', histLayout)

while True:                             # The Event Loop
    event, values = calcWin.read()
     #print(event, values) #debug
    if event == '-HIST-':
        histWin.read()
    if event == 'Settings':
        settWin.read()

    if event == '-CALC-':
        #push the result of the input to the output
        pass
    if event == '-DIV-':
        #enter / into the input field
        pass
    if event == '-MULTI-':
        #enter * character into the input field
        pass
    if event == '-SUB-':
        #enter - character into input field
        pass
    if event == '-DOT-':
        #enter . character into the input field
        pass
    if event == '-ADD-':
        #enter + character into the input field
        pass
    if event == '-9-':
        pass
    if event == '-8-':
        pass
    if event == '-7-':
        pass
    if event == '-6-':
        pass
    if event == '-5-':
        pass
    if event == '-4-':
        pass
    if event == '-3-':
        pass
    if event == '-2-':
        pass
    if event == '-1-':
        pass
    if event == '-0-':
        pass

    if event in (None, 'Exit', 'Cancel'):
        break