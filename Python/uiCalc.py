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
"""

import webbrowser as wb
import PySimpleGUI as sg
#Manual: https://www.pysimplegui.org/en/latest/

sg.theme('DarkAmber')
history = ["Select below:","2+2=5"]
calcLayout = [
    [sg.Titlebar('Calulator')],
    #Menu Example: [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]])]],
    [sg.MenubarCustom(
        [['File', ["Settings", "Exit", "History"]],
        ['Help', ["About...", "Github"]],
        ['History', []]])],
    [sg.Input(size = (15, 5), k = '-INPUT-'), sg.Button("Calculate", k = '-CALC-')],
    [sg.Button("/", k = '-DIV-', size = (2,1)), sg.Text("     "), sg.Button("x", k = '-MULTI-', size = (2,1)), sg.Text("     "), sg.Button("-", k = ' -SUB-', size = (2,1))],
    [sg.Button("7", k = '-7-', size = (2,1)), sg.Text("     "), sg.Button("8", k = '-8-', size = (2,1)),sg.Text("     "), sg.Button("9", k = '-9-', size = (2,1))],
    [sg.Button("4", k = '-4-', size = (2,1)), sg.Text("     "), sg.Button("5", k = '-5-', size = (2,1)), sg.Text("     "), sg.Button("6", k = '-6-', size = (2,1))],
    [sg.Button("1", k = '-1-', size = (2,1)), sg.Text("     "), sg.Button("2", k = '-2-', size = (2,1)), sg.Text("     "), sg.Button("3", k = '-3-', size = (2,1))],
    [sg.Button("0", k = '-0-', size = (2,1)), sg.Text("     "), sg.Button(".", k = '-DOT-', size = (2,1)), sg.Text("     "), sg.Button("+", k = '-ADD-', size = (2,1))],
    [sg.Output(size=(20,1), sbar_width = 0)]
    ]

settLayout = [
    [sg.Titlebar('Settings')],
    [sg.MenubarCustom(
        [["File", ['Save and Exit', 'Exit']]])],
        [sg.DropDown([])]
]

histLayout = [
    [sg.Titlebar('History')],
    [sg.MenubarCustom(
        [["File", ["Exit"]]])],
        [sg.Listbox(history, size=(max(map(len, history))+2, 10), key='HISTLIST')]
]

aboutLayout = [
    [sg.Titlebar('About')],
    [sg.Text("Created by Tr8demark")],
    [sg.Text("Version: 0.1")],
    [sg.Text("Github", enable_events = True, k = "textgit")]
]

calcWin = sg.Window('Calculator', calcLayout)
settWin = sg.Window('Settings', settLayout)
histWin = sg.Window('History', histLayout)
aboutWin = sg.Window('About', aboutLayout)
urlgit = "https://github.com/Tr8demark/Projects/blob/main/Python/uiCalc.py"

while True:                         # The Event Loop
    event, values = calcWin.read()
     #print(event, values) #debug
#   Read Windows
    if event == 'History':
        histWin.read()
    if event == 'Settings':
        settWin.read()
    if event == 'About...':
        aboutWin.read()

#    if event == "textgit":
#        wb.open(urlgit, new = 0, autoraise = True)
#    Below works; above does not work. Clickable text issues.
    if event == "Github":
        wb.open(urlgit, new = 0, autoraise = True)


    if event == '-CALC-':
        #push the result of the input to the output and append string to history list
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