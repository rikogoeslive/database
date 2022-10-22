import PySimpleGUI as sg
import sqlite3
from tkinter import *


connector = sqlite3.connect('darbuotojai_v3.db')
cursor = connector.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS darbuotojai ( 
    name text,
    surname text,
    gender text,
    birth text,
    resp text,
    salary text
    )""")

connector.commit()
connector.close()

sg.theme('Reds')
sg.set_options(font=('Courier', 10))

layout = [
    [sg.T("Vardas"), sg.Push(), sg.I(size=(20), key='name')],
    [sg.T("Pavardė"), sg.Push(), sg.I(size=(20), key='surname')],
    [sg.T("Lytis"), sg.Push(), sg.Combo(size=(10,3), values=['Vyras', 'Moteris'], key='gender')],
    [sg.CalendarButton(button_text="Gim. data", format='%Y-%m-%d', no_titlebar=True, close_when_date_chosen=True, target='birth'),sg.Push(), sg.I(size=(20), key='birth')],
    [sg.T("Pareigos"), sg.Push(), sg.I(size=(20), key='resp')],
    [sg.T("Uždarbis") ,sg.Push(), sg.I(size=(20), key='salary')],
    [sg.Button('Rodyti visus darbuotojus', expand_x=True)],
    [sg.Button('Pridėti darbuotoją', expand_x=True), sg.Button('Išvalyti laukus', expand_x=True), sg.Button('Išeiti', expand_x=True)]
]

window = sg.Window('Darbuotojų duomenų bazė v3', layout)

def retrieve_worker_records():
    results = []
    connector = sqlite3.connect('darbuotojai_v3.db')
    cursor = connector.cursor()
    query = "SELECT name, surname, gender, birth, resp, salary FROM darbuotojai"
    cursor.execute(query)
    for row in cursor:
        results.append(list(row))
    return results

def get_worker_records():
    worker_records = retrieve_worker_records()
    return worker_records


def show_data():
    worker_records_array = get_worker_records()
    headings = ['Vardas', 'Pavardė', 'Lytis', 'Gimimo data', 'Pareigos', 'Uždarbis']
    layout_for_display = [
        [sg.Table(values=worker_records_array,
        headings=headings,
        max_col_width=35,
        auto_size_columns=True,
        justification='left',
        row_height=50,
        enable_events=True,
        right_click_selects=True
        )],

    ]
    windr=sg.Window('Sąrašo rezultatai', layout_for_display, modal=True)

    while True:
        event, values=windr.read()
        if event == sg.WIN_CLOSED:
            break
        
def clear_inputs():
    for key in values:
        window['name'].update('')
        window['surname'].update('')
        window['gender'].update('')
        window['birth'].update('')
        window['resp'].update('')
        window['salary'].update('')
    return None

def save_to_database():
    connector = sqlite3.connect('darbuotojai_v3.db')
    cursor = connector.cursor()
    cursor.execute("INSERT INTO darbuotojai VALUES (:name, :surname, :gender, :birth, :resp, :salary)",
        {"name": values['name'],
        "surname": values['surname'],
        "gender": values['gender'],
        "birth": values['birth'],
        "resp": values['resp'],
        "salary": values['salary']
        })
        
    connector.commit()
    connector.close()   

while True:
    event, values=window.read()
    if event in (sg.WIN_CLOSED or 'Išeiti'):
        break
    if event == 'Išvalyti laukus':
        clear_inputs()
    if event == 'Rodyti visus darbuotojus':
        show_data()
    if event == 'Pridėti darbuotoją':
        name=values['name']
        surname=values['surname']
        gender=values['gender']
        birth=values['birth']
        resp=values['resp']
        salary=values['salary']
        if name=='':
            sg.PopupError('Neįvestas vardas', 'Prašome užpildyti visus laukus')
        elif surname=='':
            sg.PopupError('Neįvesta pavardė', 'Prašome užpildyti visus laukus')
        elif gender=='':
            sg.PopupError('Nenurodyta lytis.', 'Prašome užpildyti visus laukus!')
        elif birth=='':
            sg.PopupError('Nenurodyta gimimo data.', 'Prašome užpildyti visus laukus!')
        elif resp=='':
            sg.PopupError('Nenurodytos pareigos.', 'Prašome užpildyti visus laukus!')
        elif salary=='':
            sg.PopupError('Nenurodytas atlyginimas', 'Prašome užpildyti visus laukus')
        else:
            try:
                summary_list="Naujas darbuotojas"
                na="\nVardas: " + values['name']
                summary_list+=na
                sur="\nPavardė: " + values['surname']
                summary_list+=sur
                gen="\nLytis: " + values['gender']
                summary_list+=gen
                bir="\nGim. data: " + values['birth']
                summary_list+=bir
                re="\nPareigos: " + values['resp']
                summary_list+=re
                sal="\nUždarbis: " + values['salary']
                summary_list+=sal
                choice = sg.PopupOKCancel(summary_list, "Prašome patvirtinti informaciją")
                if choice=='OK':
                    save_to_database()
                    clear_inputs()
                    sg.PopupQuick("Informacija buvo išsaugota.")
                else:
                    sg.PopupOK("Keisti informaciją")
            except:
                sg.Popup('Neaiški klaida, kreipkitės į administratorių.')
########################### =============================== NOT FINISHED ========================================= ####################################
window.close()