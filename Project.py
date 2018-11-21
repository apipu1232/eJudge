"""Income account and savings"""
from tkinter import *
from datetime import datetime
import csv
import os.path

root = Tk()
root.title("Income account and savings")
root.geometry("700x720")
time = ''
description = StringVar()
income = IntVar()
expence = IntVar()
result1 = StringVar()
result2 = StringVar()
result3 = StringVar()
summary = StringVar()

"""Show time"""
clock = Label(root, font=(None, 25))
clock.pack(pady=10)

def replaced(sequence, old, new):
    """Replace old with new"""
    #for example a = ['0','1','2','3'] ; a = list(replaced(a, '2', '0')) --> a = ['0','1','0','3']
    return (new if x == old else x for x in sequence)

def tick():
    """Update time every 200ms"""
    global time
    time1 = datetime.now().strftime("%d/%m/%Y\t%H:%M:%S")
    if time1 != time:
        time = time1
        clock.config(text=time1)
    clock.after(200, tick)

def writefile():
    """Write csv file"""
    desc = description.get()
    inc = income.get()
    exp = expence.get()
    time_now = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().strftime("%d/%m/%Y")
    data1 = [desc, inc, exp, date, time_now]
    data1 = list(replaced(data1, '', '0'))
    with open('account.csv', 'a', newline='') as csvfile:
            writecsv = csv.writer(csvfile)
            writecsv.writerow(data1)
    textshow1 = "{0}".format(desc)
    textshow2 = "{0:,d}".format(inc)
    textshow3 = "- {0:,d}".format(exp)
    result1.set(textshow1)
    result2.set(textshow2)
    result3.set(textshow3)
    readfile()

def readfile():
    """Read csv file"""
    listbox.delete(0, END)
    with open('account.csv') as csvfile:
        readcsv = csv.reader(csvfile)
        total = 0
        for row in readcsv:
            desc = row[0]
            inc = row[1]
            exp = row[2]
            date = row[3]
            time_now = row[4]
            total += int(row[1])
            total -= int(row[2])
            text = "{0:<15}+{1:<10}-{2:<10}{3:<12}{4:<8}".format(desc, inc, exp, date,time_now)
            listbox.insert(0, text)
        summary.set(f"Total : {total}")

def start_acc():
    summary.set("Total : 0")

def show():
    """show planner"""
    plan.deiconify()
    
def hide():
    """Hide Planner"""
    plan.withdraw()

label_d = Label(root, text="Description: ").pack(padx=10,pady=5)
entry_d = Entry(root, textvariable=description).pack(padx=10,pady=5)
label_i = Label(root, text="Income(Baht): ").pack(padx=10,pady=5)
entry_i = Entry(root, textvariable=income).pack(padx=10,pady=5)
label_e = Label(root, text="Expence(Baht): ").pack(padx=10,pady=5)
entry_e = Entry(root, textvariable=expence).pack(padx=10,pady=5)
button_a = Button(root, text="Add", command=writefile).pack(padx=10,pady=5)
result_label1 = Label(root, textvariable=result1, foreground="blue").pack(padx=10,pady=5)
result_label2 = Label(root, textvariable=result2, foreground="green").pack(padx=10,pady=5)
result_label3 = Label(root, textvariable=result3, foreground="red").pack(padx=10,pady=5)
summary_label =  Label(root, textvariable=summary, font=(None, 15)).pack(padx=10,pady=5)
listbox = Listbox(root, width=50)
listbox.pack(pady=20)
show_plan = Button(root, text="Show Planner", command=show).pack(padx=10,pady=5)
hide_plan = Button(root, text="Hide Planner", command=hide).pack(padx=10,pady=5)

"""Planning window"""
plan = Toplevel()
plan.geometry("350x600")
plan.title("Planner")
product = StringVar()
prices = IntVar()
days = IntVar()
saving = StringVar()

def add_plan():
    """Add plan on add plan button"""
    name = product.get()
    price = prices.get()
    day = days.get()
    print(name)
    data = [name, price, day]
    data = list(replaced(data, '', '0'))
    print(data)
    with open('planner.csv', 'a', newline='') as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(data)
    readplan()

def readplan():
    """Read csv file"""
    listbox2.delete(0, END)
    with open('planner.csv') as csvfile:
        readcsv = csv.reader(csvfile)
        total = 0
        for row in readcsv:
            name = row[0]
            price = int(row[1])
            day = int(row[2])
            if day != 0:
                save = price // day + 1
            else:
                save = price
            total += save
            text = "{0:<15}\t{1:<10}\t{2:<10}\t{3:<10}".format(name, price, day, save)
            listbox2.insert(0, text)
        saving.set(f"You have to save {total} per day")

def start_plan():
    saving.set("You have to save 0 per day")

label_n = Label(plan, text="Product name").pack(padx=10,pady=5)
entry_n = Entry(plan, textvariable=product).pack(padx=10,pady=5)
label_p = Label(plan, text="Price").pack(padx=10,pady=5)
entry_p = Entry(plan, textvariable=prices).pack(padx=10,pady=5)
label_f = Label(plan, text="Days").pack(padx=10,pady=5)
entry_f = Entry(plan, textvariable=days).pack(padx=10,pady=5)
button_p = Button(plan, text="Plan", command=add_plan).pack(padx=10,pady=5)
listbox2 = Listbox(plan, width=50)
listbox2.pack(pady=20)
saving_label = Label(plan, textvariable=saving, font=(None, 15)).pack(padx=10,pady=5)

if os.path.isfile("account.csv"):
    readfile()
else:
    start_acc()

if os.path.isfile("planner.csv"):
    readplan()
else:
    start_plan()

tick()
plan.withdraw()
root.mainloop()
