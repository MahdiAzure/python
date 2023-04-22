import PySimpleGUI as sg
from datetime import datetime
from pathlib import Path  # core python module
import pandas as pd  # pip install pandas openpyxl

# Add some color to the window
sg.theme('DarkTeal9')

layout = [
          
            [sg.Input(key='Date', size=(20,1)), sg.CalendarButton("Done", close_when_date_chosen=True, location=(0,0), no_titlebar=False )],
            [sg.Text('veuillez remplir les cases vides ! ')],
            [sg.Text('CIN', size=(15,1)), sg.InputText(key='CIN')],
            [sg.Text('Nom', size=(15,1)), sg.InputText(key='Nom')],
            [sg.Text('Sex', size=(15,1)), sg.Combo(['Homme', 'Femme'], key='Sex')],
            
            [sg.Text('Nb Doliprane', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                       initial_value=0, key='Doli')],
            [sg.Text('Nb Augmentin', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                       initial_value=0, key='Augm')],
            [sg.Text('Nb GinKor', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                       initial_value=0, key='Gin')],







            [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Projet  Python DS', layout)


# This is to make sure that the arrival date is not before the departure date
def Date1(datetime):
  
    Date1_object = datetime.strptime(Date1, '%Y-%m-%d %H:%M:%S')
    
    return Date1


def clear_input():
    for key in values:
        window[key]('')
    return None



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        #new_record = pd.DataFrame(values, index=[0])
        #df = pd.concat([df, new_record], ignore_index=True)
        #df.to_excel(EXCEL_FILE, index=False)
        print(event , values)
        sg.popup('Data saved!')
    
       
window.close()

