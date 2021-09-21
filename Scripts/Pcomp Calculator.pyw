import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry('350x220+500+500')
window.title('P Comp Calculator v0.01')
window.resizable(False, False)
s = ttk.Style().theme_use('xpnative')

gear_ratio_label = ttk.Label(text='Gear Ratio:').place(x=20, y=30)
drive_rate_label = ttk.Label(text='Test Hand:').place(x=20, y=55)
lowest_billing_hand_label = ttk.Label(text='Lowest Billing Hand:').place(x=20, y=80)

gear_ratio_entry = ttk.Entry(width=30)
gear_ratio_entry.place(x=150, y=30)
gear_ratio_entry.insert(0, '300.78')

drive_rate_entry = ttk.Entry(width=30)
drive_rate_entry.place(x=150, y=55)
drive_rate_entry.insert(0, '2.00')

lowest_billing_hand_entry = ttk.Entry(width=30)
lowest_billing_hand_entry.place(x=150, y=80)
lowest_billing_hand_entry.insert(0, '1000')

calculate_button = ttk.Button(text='Calculate', width=10, command=lambda:calculate_pcomp()).place(x=100, y=170)
reset_button = ttk.Button(text='Reset', width=10, command=lambda:reset()).place(x=180, y=170)

actual_pcomp_label = ttk.Label(text='Actual P Comp:').place(x=20, y=110)
rounded_pcomp_label = ttk.Label(text='Rounded P Comp:').place(x=20, y=135)

actual_pcomp_text = tk.StringVar()
actual_pcomp_text.set('0')
rounded_pcomp_text = tk.StringVar()
rounded_pcomp_text.set('0')

actual_pcomp_value = ttk.Label(textvariable=actual_pcomp_text).place(x=150, y=110)
rounded_pcomp_value = ttk.Label(textvariable=rounded_pcomp_text).place(x=150, y=135)

def calculate_pcomp():
    p_comp = float(lowest_billing_hand_entry.get())/(float(gear_ratio_entry.get())*float(drive_rate_entry.get()))
    actual_pcomp_text.set(str(p_comp))
    rounded_pcomp_text.set(str(round(p_comp, 4)))

def reset():
    gear_ratio_entry.delete(0, 'end')
    drive_rate_entry.delete(0, 'end')
    lowest_billing_hand_entry.delete(0, 'end')
    actual_pcomp_text.set('0')
    rounded_pcomp_text.set('0')

if __name__ == '__main__':
    window.mainloop()
