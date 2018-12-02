"""Income account and savings"""
from tkinter import *
from tkinter import ttk
from datetime import datetime
import csv
import os.path

root = Tk()
root.title("Income account and savings")
root.geometry("700x720")

tab_control = ttk.Notebook(root)
save = ttk.Frame(tab_control)
plan = ttk.Frame(tab_control)
tab_control.add(save, text='     Income and Expense     ')
tab_control.add(plan, text='     Planning     ')
tab_control.pack(expand=1, fill='both')

time = ''
description = StringVar()
income = IntVar()
expence = IntVar()
result1 = StringVar()
result2 = StringVar()
result3 = StringVar()
summary = StringVar()

"""Show time"""
clock = Label(root, font=(None, 20))
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


label_d = Label(save, text="Description: ").pack(padx=10,pady=5)
entry_d = Entry(save, textvariable=description).pack(padx=10,pady=5)
label_i = Label(save, text="Income(Baht): ").pack(padx=10,pady=5)
entry_i = Entry(save, textvariable=income).pack(padx=10,pady=5)
label_e = Label(save, text="Expence(Baht): ").pack(padx=10,pady=5)
entry_e = Entry(save, textvariable=expence).pack(padx=10,pady=5)
button_a = Button(save, text="Add", command=writefile).pack(padx=10,pady=5)
result_label1 = Label(save, textvariable=result1, foreground="blue").pack(padx=10,pady=5)
result_label2 = Label(save, textvariable=result2, foreground="green").pack(padx=10,pady=5)
result_label3 = Label(save, textvariable=result3, foreground="red").pack(padx=10,pady=5)
summary_label =  Label(save, textvariable=summary, font=(None, 15)).pack(padx=10,pady=5)
listbox = Listbox(save, width=50)
listbox.pack(pady=20)

"""Planning window"""
product = StringVar()
prices = IntVar()
goals = StringVar()
saving = StringVar()

def add_plan():
    """Add plan on add plan button"""
    name = product.get()
    price = prices.get()
    goal = goals.get()
    data = [name, price, goal]
    data = list(replaced(data, '', '0'))
    with open('planner.csv', 'a', newline='') as csvfile:
        writecsv = csv.writer(csvfile)
        writecsv.writerow(data)
    readplan()

def readplan():
    """Read csv file"""
    listbox2.delete(0, END)
    date = datetime.now().strftime("%d/%m/%Y")
    with open('planner.csv') as csvfile:
        readcsv = csv.reader(csvfile)
        total = 0
        for row in readcsv:
            name = row[0]
            price = int(row[1])
            goal = row[2]
            day = timess(date, goal)
            save = price // day + 1
            total += save
            text = "{0:<15}\t{1:<10}\t{2:<10}\t{3:<10}".format(name, price, day, save)
            listbox2.insert(0, text)
        saving.set(f"You have to save {total} per day")

def timess(Today,Goalday):
    Today = Today.split("/")
    day1 = int(Today[0])
    month1 = int(Today[1])
    year1 = int(Today[2])
    Goalday = Goalday.split("/")
    day2 = int(Goalday[0])
    month2 = int(Goalday[1])
    year2 = int(Goalday[2])
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day = 0
    # นับวัน
    if day1 > day2:
        day = day + day2 + (months[month1] - day1)
    elif day1 < day2:
        day = day + (day2 - day1)
    elif day1 == day2:
        day = day + (months[month1] - day1) + day2
    # นับเดือน
    if month1 > month2:
        for i in range(month1 + 1, 12):
            day = day + months[i]
        for j in range(1, month2):
            day = day + months[j]
    elif month1 < month2:
        for k in range(month1 + 1, month2):
            day = day + months[k]
    elif month1 == month2:
        pass
    # กรณี วันเเดียวกัน เดือนเดียวกัน เเต่คนละปี
    if day1 == day2 and month1 == month2:
        day = 0
    # นับปี
    day = day + ((year2 - year1) * (365 * (year2 > year1)))
    # เช็ค leapyear.
    leapyear = 0
    if month1 < 3:
        if month1 == 2 and day1 == 29:
            for l in range(year1 + 1, year2 + 1):
                if l % 400 == 0:
                    leapyear = leapyear + 1
                elif l % 4 == 0:
                    leapyear = leapyear + 1
        elif year1 != year2:
            for m in range(year1, year2 + 1):
                if m % 400 == 0:
                    leapyear = leapyear + 1
                elif m % 4 == 0:
                    leapyear = leapyear + 1
        elif year1 == year2:
            if year1 % 400 == 0:
                leapyear = leapyear + 1
            elif year1 % 4 == 0:
                leapyear = leapyear + 1
    elif year1 != year2:
        for n in range(year1 + 1, year2 + 1):
                if n % 400 == 0:
                    leapyear = leapyear + 1
                elif n % 4 == 0:
                    leapyear = leapyear + 1
    return day + leapyear

def start_plan():
    saving.set("You have to save 0 per day")

label_n = Label(plan, text="Product name").pack(padx=10,pady=5)
entry_n = Entry(plan, textvariable=product).pack(padx=10,pady=5)
label_p = Label(plan, text="Price").pack(padx=10,pady=5)
entry_p = Entry(plan, textvariable=prices).pack(padx=10,pady=5)
label_f = Label(plan, text="Goal date (dd/mm/yyyy)").pack(padx=10,pady=5)
entry_f = Entry(plan, textvariable=goals).pack(padx=10,pady=5)
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
root.mainloop()
