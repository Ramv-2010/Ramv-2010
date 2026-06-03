import random
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime

root = tk.Tk()
root.title("Bytes and Bolts Tech Hire")
root.geometry("600x600")   # MAKE SCREEN BiGGER
root.configure(bg = "#DCEEFF")

def gen_vald_receipt_num ():
    while True:
        new_receipt_num = random.randint(a=100000, b = 999999)
        current_reciept_nums_in_use_list = [] # go into user data later
        if new_receipt_num in current_reciept_nums_in_use_list:
            pass
        else:
            return new_receipt_num

#Main Title Frame
title_frame = tk.Frame(root, bg = "#102542", pady = 20)
title_frame.place(x = 0, y = 0, width = 600)

#actual Main Title
title_label = tk.Label(title_frame, text = "⚡ BYTES & BOLTS TECH HIRE ⚡", font= ("Arial",22, "bold"), bg = "#102542")
title_label.pack()

hire_menu_label = tk.Label(text= "Hire A Item!!!", bg = "#DCEEFF", fg = "Black", font = ("Arial", 18, "bold"))
hire_menu_label.place(x=240, y = 115)



hire_widgets_frame = tk.Frame(root, bg = "White")
hire_widgets_frame.place(x= 50, y=160, width= 500, height = 380)

user_current_r_num  = gen_vald_receipt_num()
receipt_number_label = tk.Label(hire_widgets_frame,text = f" Receipt Number : {user_current_r_num}")
receipt_number_label.place(x = 175, y = 15)

name_entry_label = tk.Label(hire_widgets_frame, text = "Name", bg = "white", fg= "black")
name_entry_label.place(x = 60, y = 55)
name_entry = tk.Entry(hire_widgets_frame, width=30)
name_entry.place(x = 150, y = 55)

hire_item_label = tk.Label(hire_widgets_frame, text = "Hire Item", bg = "white", fg= "black")
hire_item_label.place(x = 60, y = 100)
hire_item_combo_box = ttk.Combobox(hire_widgets_frame,values=["Computer", "Mouse", "PC", "Laptop","Keyboard"])
hire_item_combo_box.place(x = 150, y = 100)

hire_quantity_label = tk.Label(hire_widgets_frame, text= "Hire Quantity", bg = "white", fg= "black")
hire_quantity_label.place(x = 60, y = 150)
quantities_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
hire_quantity_spinbox = tk.Spinbox(hire_widgets_frame, values=quantities_list)
hire_quantity_spinbox.place(x = 150, y = 150)

date_hire_cal_label = tk.Label(hire_widgets_frame, text = "Date Hire", bg = "white", fg= "black")
date_hire_cal_label.place(x = 60, y = 190)

date_hire_gui_calendar = Calendar(hire_widgets_frame, mindate= datetime.date.today(), background="#4A90E2",foreground="white",selectbackground="#FF6B6B", selectforeground="white",  weekendbackground="#F0F0F0", weekendforeground="red",)
date_hire_gui_calendar.place(x = 150, y = 190)

date_hire_gui_calendar.get_date()
root.mainloop()