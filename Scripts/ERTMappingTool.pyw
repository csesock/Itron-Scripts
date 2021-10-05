import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

window = tk.Tk()
window.geometry('320x250+500+500')
window.title('ERT Mapping Tool v0.1')
window.resizable(False, False)
s = ttk.Style().theme_use('xpnative')
current_file = ''

file_label = ttk.Label(text="Current file:").place(x=40, y=30)
file = tk.StringVar()
current_file = ttk.Label(textvariable=file).place(x=120, y=30)
file.set("None")

ert_label = ttk.Label(text="ERT Number: ").place(x=40, y=80)
ert_entry = ttk.Entry(width=25)
ert_entry.place(x=120, y=80)

ert_model_label = ttk.Label(text="ERT Model: ").place(x=40, y=110)
ert_model = tk.StringVar()
ert_model_output = ttk.Label(textvariable=ert_model).place(x=120, y=110)
ert_model.set("None")

calculate_one_button = ttk.Button(text="Calculate", width=15, command=lambda:ert_model.set(str((mapERTNumber(ert_entry.get()))))).place(x=60, y=160)
calculate_multi_button = ttk.Button(text="Calculate File", width=15, command=lambda:mapMultiple(current_file)).place(x=160, y=160)

load_file_button = ttk.Button(text="Load File...", width=15, command=lambda:loadFile()).place(x=60, y=185)
reset_button = ttk.Button(text="Reset", width=15, command=lambda:reset()).place(x=160, y=185)

def loadFile():
    filename = tk.filedialog.askopenfilename(title="Open File")
    file.set(str(os.path.basename(filename)))
    global current_file
    current_file = str(os.path.basename(filename))

def reset():
    file.set("None")
    ert_model.set("None")
    ert_entry.delete(0, 'end')

def mapERTNumber(ert_number):
    try:
        ert_number = int(ert_number)
    except ValueError:
        return "Invalid Value"
    if ert_number < 1400000:
        return('ERT number too small')
    elif ert_number >= 14000000 and ert_number < 16149999:
        return '40W'
    elif ert_number >= 16150000 and ert_number < 16273848:
        return '60W'
    elif ert_number >= 16500000 and ert_number < 18999998:
        return '40W'
    elif ert_number >= 18999999 and ert_number < 19999999:
        return '60W'
    elif ert_number >= 20000000 and ert_number < 20206987:
        return '40W'
    elif ert_number >= 202206988 and ert_number < 20851501:
        return '40W/50W'
    elif ert_number >= 21029490 and ert_number < 22909999:
        return '50W'
    elif ert_number >= 23000000 and ert_number < 23164999:
        return '50W'
    elif ert_number >= 23165000 and ert_number < 23499999:
        return '60W'
    elif ert_number >= 23500000 and ert_number < 25999999:
        return '40W/50W'
    elif ert_number >= 26000000 and ert_number < 31999999:
        return '60W'
    elif ert_number >= 32000000 and ert_number < 32499999:
        return '100W Phase 2'
    elif ert_number >= 32500000 and ert_number < 32999999:
        return 'Reserved for 100W Phase 2'
    elif ert_number >= 33000000 and ert_number < 33197976:
        return '100W Phase 3 (x.16 and older firmware)'    
    elif ert_number >= 33197977 and ert_number < 34099999:
        return '100W Phase 3 (x.17 and older firmware)'
    elif ert_number >= 34100000 and ert_number < 46000000:
        return '100W Phase 3.5'
    elif ert_number >= 46000001 and ert_number < 46499999:
        return '100W w/Leak Sensor Phase 2'
    elif ert_number >= 46500000 and ert_number < 46505670:
        return '100W w/Leak Sensor Phase 3 (x.16 and older firmware)'
    elif ert_number >= 46505671 and ert_number < 53899999:
        return '100W w/Leak Sensor Phase 3 (x.17 and newer firmware)'
    elif ert_number >= 53900000 and ert_number < 55999999:
        return '60W'
    elif ert_number >= 56000000 and ert_number < 57649999:
        return '50W'
    elif ert_number >= 57650000 and ert_number < 57999999:
        return '60W'
    elif ert_number >= 66000000 and ert_number < 66249999:
        return '50W'
    elif ert_number >= 67108700 and ert_number < 67349999:
        return 'Reserved for 100W phase 3.5'
    elif ert_number >= 67350000 and ert_number < 67399999:
        return 'Reserved for 100W phase 3.5LS'
    elif ert_number >= 67400000 and ert_number < 69499999:
        return '100W Phase 4'
    elif ert_number >= 69500000 and ert_number < 69749999:
        return '100W Phase 4 w/LS'
    elif ert_number >= 70000000 and ert_number < 78999999:
        return '100W Phase 4'
    elif ert_number >= 79000000 and ert_number < 79999999:
        return '100W Phase 4 w/LS'
    elif ert_number >79999999:
        return("ERT number too large")

def mapMultiple(filename):
    built_line = ''
    try:
        with open(filename, 'r') as openfile:
            with open('ERT Models.txt', 'w') as builtfile:
                builtfile.write("ERT# \tERT Model\n")
                builtfile.write("---------------------\n")
                for line in openfile:
                    built_line = str(line.strip())+'\t'+str(mapERTNumber(line))+'\n'
                    builtfile.write(built_line)
    except FileNotFoundError:
        print("Error: File Not Found")

if __name__=='__main__':
    window.mainloop()