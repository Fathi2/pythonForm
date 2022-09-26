from tkinter import *
import sqlite3

root = Tk()
root.config(bg="black")
root.title("from to input data")
root.geometry('500x500')
el = StringVar()
e2 = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()


def insert_database():
    name1 = el.get()
    emaill = e2.get()
    gander = var.get()
    country = c.get()
    programming = var1.get()
    conn = sqlite3.connect("frpm.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS STUDENT (Fullname TEXT,Email TEXT,gander TEXT,Countey TEXT,Progamming TEXT )")
        cursor.execute("INSERT INTO student(Fullname,Email,gander,Countey,Progamming  ) values(?,?,?,?,?)",
                       (name1, emaill, gander, country, programming))
        conn.commit()


def delete_database():
    name1 = el.get()
    emaill = e2.get()
    gander = var.get()
    country = c.get()
    programming = var1.get()
    conn = sqlite3.connect("frpm.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('delete from student where Fullname=? and Email=? and gander=? and Countey=? and Progamming=?',
                       (name1, emaill, gander, country, programming))
        conn.commit()


Label(root, text="regestration from", width=20, fg='red', font=("bold", 20)).place(x=90, y=53)
Label(root, text="Fullname", width=20, font=("bold", 10)).place(x=80, y=130)
Entry(root, textvar=el).place(x=250, y=130)
Label(root, text="email", width=20, fg='red', font=("bold", 10)).place(x=68, y=180)
Entry(root, textvar=e2).place(x=250, y=180)
var = IntVar()
Label(root, text="gender", width=20, font=("blod", 10)).place(x=65, y=230)
Radiobutton(root, text="male", padx=3, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="famle", padx=15, variable=var, value=2).place(x=290, y=230)
Label(root, text="country", width=20, font=("bold", 10)).place(x=70, y=280)
list1 = ["Canda", "india", "UK", "yemen"]
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=18)
c.set("select the country")
droplist.place(x=250, y=280)
Label(root, text="programming", width=20, font=("bold", 10)).place(x=85, y=330)
var1 = IntVar()
Checkbutton(root, text="java", variable=var1).place(x=280, y=330)
Checkbutton(root, text="python", variable=var1).place(x=350, y=330)
Button(root, text="insert", width=20, bg="brown", fg='white', command=insert_database).place(x=180, y=390)
Button(root, text="delete", width=20, bg="brown", fg='white', command=delete_database).place(x=180, y=450)
root.mainloop()











