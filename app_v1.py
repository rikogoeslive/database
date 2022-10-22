from tkinter import *
import tkinter as tk
from PIL import ImageTk
import sqlite3

root = tk.Tk()
root.title("Darbuotojų duomenų bazė v1")
root.eval("tk::PlaceWindow . center")
icon = tk.PhotoImage(file = 'icon.png')
root.wm_iconphoto(False, icon)

connector = sqlite3.connect('darbuotojai_v1.db')
cursor = connector.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS darbuotojai (
    name text,
    surname text,
    birth text, 
    responsibilities text,
    salary integer 
    )""")
connector.commit()
connector.close()


def delete():
    connector = sqlite3.connect('darbuotojai_v1.db')
    cursor = connector.cursor()
    cursor.execute("DELETE from darbuotojai WHERE oid= " + delete_box.get())
    connector.commit()
    connector.close()


def save():
    connector = sqlite3.connect('darbuotojai_v1.db')
    cursor = connector.cursor()
    
    record_id = delete_box.get()
    cursor.execute("""UPDATE darbuotojai SET
        name = :name,
        surname = :surname, 
        birth = :birth,
        responsibilities = :responsibilities,
        salary = :salary

        WHERE oid = :oid""",
        {
        'name': name_editor.get(),
        'surname': surname_editor.get(),
        'birth': birth_editor.get(),
        'responsibilities': responsibilities_editor.get(),
        'salary': salary_editor.get(),
        'oid': record_id
        })

    connector.commit()
    connector.close()


def update():
    updater = Tk()
    updater.title("Atnaujinkite darbuotojo duomenis")
    updater.eval("tk::PlaceWindow . center")
    connector = sqlite3.connect('darbuotojai_v1.db')
    cursor = connector.cursor()
    record_id = delete_box.get()
    cursor.execute("SELECT * FROM darbuotojai WHERE oid = " + record_id)
    records = cursor.fetchall()
    
    global name_editor
    global surname_editor
    global birth_editor
    global responsibilities_editor
    global salary_editor

    name_editor = Entry(updater, width=30)
    name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    surname_editor = Entry(updater, width=30)
    surname_editor.grid(row=1, column=1)
    birth_editor = Entry(updater, width=30)
    birth_editor.grid(row=2, column=1)
    responsibilities_editor = Entry(updater, width=30)
    responsibilities_editor.grid(row=3, column=1)
    salary_editor = Entry(updater, width=30)
    salary_editor.grid(row=4, column=1)
   
    name_label = Label(updater, text="Vardas: ")
    name_label.grid(row=0, column=0, pady=(10, 0))
    surname_label = Label(updater, text="Pavardė: ")
    surname_label.grid(row=1, column=0)
    birth_label = Label(updater, text="Gimimo Data: ")
    birth_label.grid(row=2, column=0)
    responsibilities_label = Label(updater, text="Pareigos: ")
    responsibilities_label.grid(row=3, column=0)
    salary_label = Label(updater, text="Atlyginimas: ")
    salary_label.grid(row=4, column=0)
    save_button = Button(updater, text="Įrašyti pakeitimus", command=save)
    save_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=63)

    for record in records:
        name_editor.insert(0, record[0])
        surname_editor.insert(0, record[1])
        birth_editor.insert(0, record[2])
        responsibilities_editor.insert(0, record[3])
        salary_editor.insert(0, record[4])
    
def submit():
    connector = sqlite3.connect('darbuotojai_v1.db')
    cursor = connector.cursor()
    cursor.execute("INSERT INTO darbuotojai VALUES (:name, :surname, :birth, :responsibilities, :salary)",
    {
        "name": name.get(),
        "surname": surname.get(),
        "birth": birth.get(),
        "responsibilities": responsibilities.get(),
        "salary": salary.get()
    })
    name.delete(0, END)
    surname.delete(0, END)
    birth.delete(0, END)
    responsibilities.delete(0, END) 
    salary.delete(0, END)
    connector.commit()
    connector.close()

def query():
    connector = sqlite3.connect('darbuotojai_v1.db')
    cursor = connector.cursor()
    cursor.execute("SELECT *, oid FROM darbuotojai")
    records = cursor.fetchall()
    #print(records)
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\t" +str(record[5]) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    connector.commit()
    connector.close()


name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20, pady=(10, 0))
surname = Entry(root, width=30)
surname.grid(row=1, column=1)
birth = Entry(root, width=30)
birth.grid(row=2, column=1)
responsibilities = Entry(root, width=30)
responsibilities.grid(row=3, column=1)
salary = Entry(root, width=30)
salary.grid(row=4, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=8,column=1, pady=5)


name_label = Label(root, text="Vardas: ")
name_label.grid(row=0, column=0, pady=(10, 0))
surname_label = Label(root, text="Pavardė: ")
surname_label.grid(row=1, column=0)
birth_label = Label(root, text="Gimimo Data: ")
birth_label.grid(row=2, column=0)
responsibilities_label = Label(root, text="Pareigos: ")
responsibilities_label.grid(row=3, column=0)
salary_label = Label(root, text="Atlyginimas: ")
salary_label.grid(row=4, column=0)
delete_box_label = Label(root, text="Nurodykite darbuotojo ID: ")
delete_box_label.grid(row=8, column=0, pady=5)


submit_button = Button(root, text="Pridėti darbuotoją", command=submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_button = Button(root, text="Rodyti darbuotojų sąrašą", command=query)
query_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=83)
delete_button = Button(root, text="Ištrinti darbuotoją", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
update_button = Button(root, text="Atnaujinti darbuotojo duomenis", command=update)
update_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=63)

root.mainloop()

