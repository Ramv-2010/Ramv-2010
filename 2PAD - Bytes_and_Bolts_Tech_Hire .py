import random
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime

root = tk.Tk()
root.title("Bytes and Bolts Tech Hire")
root.geometry("700x600")
root.configure(bg = "#DCEEFF")

current_reciept_nums_in_use_list = []  # go into user data later
hire_items_avaliable_list = ["Computer", "Mouse", "PC", "Laptop","Keyboard"]
valid_items_user_dict = {}
non_valid_items = []

def check_and_gen_vald_receipt_num ():
    while True:
        user_receipt_num = random.randint(a=100000, b=999999)
        if user_receipt_num in current_reciept_nums_in_use_list:
            current_reciept_nums_in_use_list.remove(user_receipt_num)

        else:
            current_reciept_nums_in_use_list.append(user_receipt_num)
            valid_items_user_dict["user_receipt_number"] = user_receipt_num
            return user_receipt_num


def confirm_hire_vald():
    user_confirmed_name = name_entry.get()
    if not user_confirmed_name.isalpha():
        if user_confirmed_name == "":
            print("You have left the name field empty, please reenter this field and resubmit your entry")
        else:
            print("Please enter a valid name (No Special Characters or Numbers)")
    else:
        valid_items_user_dict["user_name"] = user_confirmed_name
        print(valid_items_user_dict)


    user_confirmed_hiring_item = hire_item_combo_box.get()
    if not user_confirmed_hiring_item in hire_items_avaliable_list:
        print("Please enter the a item that we have you have entered an item not in our system please tryagain and submit")
    else:
        valid_items_user_dict["user_hire_item "] = user_confirmed_hiring_item
        print(valid_items_user_dict)

    try:
        user_confirmed_hiring_quantity = int(hire_quantity_spinbox.get())
        if  user_confirmed_hiring_quantity <  1 or user_confirmed_hiring_quantity > 20:
            print("Please enter a valid number (Between 1 and 20)")
        else:
            valid_items_user_dict["user_hire_qty"] = user_confirmed_hiring_quantity
            print(valid_items_user_dict)

    except ValueError:
        print("Please enter a number (only digits)")

    valid_items_user_dict["user_hire_date"] = date_hire_gui_calendar.get_date()
    print(valid_items_user_dict)

def store_data(user_name, user_hire_item, user_hire_qty, user_hire_date):

    while True:
        try:
            with open(file= "users_data.json", mode = "r") as data_file:
                users_data_list = data_file.readlines()
                print(users_data_list)
            with open(file= "users_data.json", mode = "W") as write_data_file:
                users_data_list.append(valid_items_user_dict)
                write_data_file.write(users_data_list)

        except FileNotFoundError:
            with open(file="users_data.json", mode="w") as new_data_file:
                new_data_file.write(f"{valid_items_user_dict}")

#Main Title Frame
title_frame = tk.Frame(root, bg = "#102542", pady = 20)
title_frame.place(x = 0, y = 0, width = 700)

#actual Main Title
title_label = tk.Label(title_frame, text = "⚡ BYTES & BOLTS TECH HIRE ⚡", font= ("Arial",22, "bold"), bg = "#102542")
title_label.pack()

hire_menu_label = tk.Label(text= "Hire A Item!!!", bg = "#DCEEFF", fg = "Black", font = ("Arial", 20, "bold"))
hire_menu_label.place(x=300, y = 100)

hire_widgets_frame = tk.Frame(root, bg = "White")
hire_widgets_frame.place(x= 100, y=150, width= 500, height = 415)

user_current_r_num  = check_and_gen_vald_receipt_num()
receipt_number_label = tk.Label(hire_widgets_frame,text = f" Receipt Number : {user_current_r_num}")
receipt_number_label.place(x = 175, y = 15)

name_entry_label = tk.Label(hire_widgets_frame, text = "Name", bg = "white", fg= "black")
name_entry_label.place(x = 60, y = 55)
name_entry = tk.Entry(hire_widgets_frame, width=30)
name_entry.place(x = 150, y = 55)

hire_item_label = tk.Label(hire_widgets_frame, text = "Hire Item", bg = "white", fg= "black")
hire_item_label.place(x = 60, y = 100)

hire_item_combo_box = ttk.Combobox(hire_widgets_frame,values=hire_items_avaliable_list)
hire_item_combo_box.place(x = 150, y = 100)

hire_quantity_label = tk.Label(hire_widgets_frame, text= "Hire Quantity", bg = "white", fg= "black")
hire_quantity_label.place(x = 60, y = 150)
quantities_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
hire_quantity_spinbox = tk.Spinbox(hire_widgets_frame, values=quantities_list)
hire_quantity_spinbox.place(x = 150, y = 150)

date_hire_cal_label = tk.Label(hire_widgets_frame, text = "Date Hire", bg = "white", fg= "black")
date_hire_cal_label.place(x = 60, y = 240)
date_hire_gui_calendar = Calendar(hire_widgets_frame, mindate= datetime.date.today(), background="#4A90E2",foreground="white",selectbackground="#FF6B6B", selectforeground="white",  weekendbackground="#F0F0F0", weekendforeground="red",)
date_hire_gui_calendar.place(x = 150, y = 190)

confirm_hire_button = tk.Button(hire_widgets_frame, text= "Hire Item", background= "white", height= 2, width= 8, command= lambda: confirm_hire_vald())
confirm_hire_button.place(x = 200, y = 365)

root.mainloop()