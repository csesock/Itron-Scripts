import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry('360x240+500+500')
window.title('P Comp Calculator v0.3')
window.resizable(False, False)
s = ttk.Style().theme_use('xpnative')

TAB_CONTROL = ttk.Notebook(window)
tabSensus = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(tabSensus, text="Sensus")
tabAmerican = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(tabAmerican, text="American")
TAB_CONTROL.pack(expand=1, fill="both")

gear_ratio_label = ttk.Label(tabSensus, text='Gear Ratio:').place(x=20, y=30)
drive_rate_label = ttk.Label(tabSensus, text='Test Hand:').place(x=20, y=55)
lowest_billing_hand_label = ttk.Label(tabSensus, text='Lowest Billing Hand:').place(x=20, y=80)

gear_ratio_entry = ttk.Entry(tabSensus, width=30)
gear_ratio_entry.place(x=150, y=30)
gear_ratio_entry.insert(0, '300.78')

drive_rate_entry = ttk.Entry(tabSensus, width=30)
drive_rate_entry.place(x=150, y=55)
drive_rate_entry.insert(0, '2.00')

lowest_billing_hand_entry = ttk.Entry(tabSensus, width=30)
lowest_billing_hand_entry.place(x=150, y=80)
lowest_billing_hand_entry.insert(0, '1000')

calculate_button = ttk.Button(tabSensus, text='Calculate', width=10, command=lambda:calculate_pcomp()).place(x=100, y=170)
reset_button = ttk.Button(tabSensus, text='Reset', width=10, command=lambda:reset()).place(x=180, y=170)

actual_pcomp_label = ttk.Label(tabSensus, text='Actual P Comp:').place(x=20, y=110)
rounded_pcomp_label = ttk.Label(tabSensus, text='Rounded P Comp:').place(x=20, y=135)

actual_pcomp_text = tk.StringVar()
actual_pcomp_text.set('0')
rounded_pcomp_text = tk.StringVar()
rounded_pcomp_text.set('0')

actual_pcomp_value = ttk.Label(tabSensus, textvariable=actual_pcomp_text, foreground='#0317fc').place(x=150, y=110)
rounded_pcomp_value = ttk.Label(tabSensus, textvariable=rounded_pcomp_text, foreground='#0317fc').place(x=150, y=135)

#temp = ttk.Label(tabAmerican, text="I haven't figured out how to do these yet   :(").place(x=50, y=50)
part_number_entry_label = ttk.Label(tabAmerican, text="Part #:").place(x=20, y=30)
part_number_entry = ttk.Entry(tabAmerican, width=30)
part_number_entry.place(x=150, y=30)

cf_label = ttk.Label(tabAmerican, text="Cubic Feet:").place(x=20, y=60)
cf = ('1', '2', '5', '10')
cf_selected = tk.StringVar()
cf_combo = ttk.Combobox(tabAmerican, textvariable=cf_selected)
cf_combo['values']=cf
cf_combo['state']='readonly'
cf_combo.place(x=150, y=60)

actual_pcomp_label2 = ttk.Label(tabAmerican, text='Actual P Comp:').place(x=20, y=110)
rounded_pcomp_label2 = ttk.Label(tabAmerican, text='Rounded P Comp:').place(x=20, y=135)

actual_pcomp_text2 = tk.StringVar()
actual_pcomp_text2.set('0')
rounded_pcomp_text2 = tk.StringVar()
rounded_pcomp_text2.set('0')

actual_pcomp_value2 = ttk.Label(tabAmerican, textvariable=actual_pcomp_text, foreground='#0317fc').place(x=150, y=110)
rounded_pcomp_value2 = ttk.Label(tabAmerican, textvariable=rounded_pcomp_text, foreground='#0317fc').place(x=150, y=135)

calculate_button2 = ttk.Button(tabAmerican, text='Calculate', width=10, command=lambda:calculate_pcomp()).place(x=100, y=170)
reset_button2 = ttk.Button(tabAmerican, text='Reset', width=10, command=lambda:reset()).place(x=180, y=170)

def calculate_pcomp():
    p_comp = float(lowest_billing_hand_entry.get())/(float(gear_ratio_entry.get())*float(drive_rate_entry.get()))
    actual_pcomp_text.set(str(p_comp))
    rounded_pcomp_text.set(str(round(p_comp, 4)))

def map_part_number():
    return

def reset():
    gear_ratio_entry.delete(0, 'end')
    drive_rate_entry.delete(0, 'end')
    lowest_billing_hand_entry.delete(0, 'end')
    actual_pcomp_text.set('0')
    rounded_pcomp_text.set('0')
    
if __name__ == '__main__':
    window.mainloop()
