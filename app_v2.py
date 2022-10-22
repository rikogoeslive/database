from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Darbuotojų duomenų bazė")
root.eval("tk::PlaceWindow . center")
root.geometry("800x500")

main_tree = ttk.Treeview(root)

#database#

#columns
main_tree['columns'] = ("f_name", "l_name", "birth", "respon", "salary", "id")
main_tree.column("#0", width=0, stretch=NO)
main_tree.column("f_name", anchor=W, width=60)
main_tree.column("l_name", anchor=CENTER, width=80)
main_tree.column("birth", anchor=CENTER, width=80)
main_tree.column("respon",anchor=CENTER, width=80)
main_tree.column("salary", anchor=E, width=80)
main_tree.column("id", anchor=E, width=25)
#headings
main_tree.heading("#0", text="", anchor=W)
main_tree.heading("f_name", text="Vardas", anchor=CENTER)
main_tree.heading("l_name", text="Pavardė",anchor=CENTER)
main_tree.heading("birth", text="Gim. data",anchor=CENTER)
main_tree.heading("respon", text="Pareigos",anchor=CENTER)
main_tree.heading("salary", text="Uždarbis", anchor=CENTER)
main_tree.heading("id", text="ID", anchor=CENTER)
#ADD DATA
data = [
    ["Mantas", "Andruska", "1990-04-19", "Juokutis", 5000, 2],
]
global count
count=0
for record in data:
    main_tree.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5]))
    count += 1

#check#
#main_tree.insert(parent="", index="end", iid=0, text="", values=("Mantas", "Andruska", "1990-04-19", "Juokdarys", 5000, 1))
#PACK TO THE SCREEN
main_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)
#LABELS
f_name_l = Label(add_frame, text="Vardas")
f_name_l.grid(row=0, column=1)
l_name_l = Label(add_frame, text="Pavardė")
l_name_l.grid(row=0, column=2)
birth_l = Label(add_frame, text="Gim. data")
birth_l.grid(row=0, column=3)
respon_l = Label(add_frame, text="Pareigos")
respon_l.grid(row=0, column=4)
salary_l = Label(add_frame, text="Uždarbis")
salary_l.grid(row=0, column=5)
id_l = Label(add_frame, text="ID")
id_l.grid(row=0, column=6)
#ENTRIES
f_name_e = Entry(add_frame)
f_name_e.grid(row=1, column=1)
l_name_e = Entry(add_frame)
l_name_e.grid(row=1, column=2)
birth_e = Entry(add_frame)
birth_e.grid(row=1, column=3)
respon_e = Entry(add_frame)
respon_e.grid(row=1, column=4)
salary_e = Entry(add_frame)
salary_e.grid(row=1,column=5)
id_e = Entry(add_frame)
id_e.grid(row=1, column=6)
#FUNCTIONS
def add_record():
    global count
    main_tree.insert(parent="", index="end", iid=count, values=(f_name_e.get(), l_name_e.get(), birth_e.get(), respon_e.get(), salary_e.get(), id_e.get()))
    count+= 1
    #CLEAR THE ENTRIES
    f_name_e.delete(0, END)
    l_name_e.delete(0, END)
    birth_e.delete(0, END)
    respon_e.delete(0, END)
    salary_e.delete(0, END)
    id_e.delete(0, END)
#BUTTONS
add_records = Button(root, text="Pridėti darbuotoją", command=add_record)
add_records.pack(pady=20) 

#################################################################################--------NOT FINISHED-------------####################################################################

root.mainloop()