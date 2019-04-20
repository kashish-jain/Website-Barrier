import time
from datetime import datetime as dt
from tkinter import *


hosts_temp=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
websites_list = []
# most common working hours
from_int = 9
to_int = 5


def blocking():
    while True:
        if dt(dt.now().year,dt.now().month,dt.now().day, from_int) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, to_int):
            with open(hosts_temp,'r+') as file:
                content=file.read()
                for website in websites_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+ website+"\n")
        else:
            with open(hosts_temp,'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites_list):
                        file.write(line)
                file.truncate()
        time.sleep(5)


window = Tk()
window.title("Website Barrier")
window.geometry("400x250")

def printing():
    website_name = websites_value.get();
    if(len(website_name) != 0):
        websites_list.append(website_name)
    label_2 = Label(window, text= "Hit block to block the websites that you have added")
    label_2.place(y = 150)
    b2 = Button(window, text = "Block", command = window.destroy)
    b2.place(y = 150, x = 285, width = 75)
    if(len(from_entry.get()) != 0):
        global from_int
        from_int = int(from_entry.get())
    if(len(to_entry.get()) != 0):
        global to_int
        to_int = int(to_entry.get())

label_1 = Label(window, text= "Add full domain of websites one-by-one and hit add after each entry")
label_1.grid(row = 0)
b1 = Button(window, text = "Add Website", command = printing)
websites_value = StringVar()

websites = Entry(window, textvariable = websites_value)
websites.place(x = 40, y = 30, width = 200)
b1.place( x = 275, y = 30)

label_3 = Label(window, text = "When do you want these Websites to be blocked (0-23)")
label_3.place(y = 75)
from_label = Label(window, text = "From")
from_label.place(y = 100)
from_entry = Entry(window, textvariable = from_int)
from_entry.place(x = 40, y = 100)
to_label = Label(window, text = "To")
to_label.place(x = 200, y = 100)
to_entry = Entry(window, textvariable = to_int)
to_entry.place(x = 240, y = 100)
window.mainloop()

if(len(websites_list) != 0):
    blocking()
