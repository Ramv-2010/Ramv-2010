#The Prerequisites to run my program are:
#Must have tkcalendar module installed ahead of running the program


import random
import tkinter as tk
from json import JSONDecodeError
from tkinter import ttk
from tkcalendar import Calendar
import datetime
import json

root = tk.Tk()
root.title("Bytes and Bolts Tech Hire")
root.geometry("700x600")
root.configure(bg = "#D7E9FA")

receipt_numbers_in_use= []  # go into user data later  (wont work cause list resets everytime program run)
items_available_list =["Computer", "Mouse", "PC","Laptop","Keyboard"]

# i used thi type of structure for my program because it enabled me to esaily add it to the json fiel and was easy to acces woth name
#user_valid_non_vald_items = {user_name :{"user_receipt_number": 0, "user_vald_status": False, "user_hire_item": "", "user_hire_qty": 0, "user_hire_date" : datetime.datetime.today()}}
#structure is gonna be like this : user_valid_non_vald_items = {user_name:{vald_status: val, value: val}}
#prototype


def check_and_gen_vald_receipt_num ():
    while True:
        receipt_num = random.randint(a=100000, b=999999)
        if not receipt_num in receipt_numbers_in_use:
            receipt_numbers_in_use.append(receipt_num) # wont work
            return receipt_num

def confirm_inputs_vald():
    user_inputs_validity_dict = {}

# hire name validation
    user_confirmed_name = name_entry.get()
    if not user_confirmed_name.isalpha( ):
        if user_confirmed_name == "":
            print("You have left the name input empty, please reenter this field and resubmit your entry")
        else:
            print("Please enter a valid name (No Special Characters or Numbers)")
    else:
        user_inputs_validity_dict["user_name"] = user_confirmed_name

    # Error 1 i had a error when i tried to chnage my key as when what i did was chnage the key of the dictinary which
    # didnt have username as a key therefore I got a key Value error to fix this i had to chnaage my statement so that instead i
    # removed it altogether because having a gobal dcitinary was quite complicated and messy

# hire item validation
    user_confirmed_hiring_item = hire_item_combo_box.get()
    if not user_confirmed_hiring_item in items_available_list:
        print("Please enter the a item that we have you have entered an item not in our system please tryagain and submit")
    else:
        user_inputs_validity_dict["user_hire_item"] = user_confirmed_hiring_item

# hire qty validation
    try:
        user_confirmed_hiring_quantity = int(hire_quantity_spinbox.get())
        if  user_confirmed_hiring_quantity <=  1 or user_confirmed_hiring_quantity >= 20:
            print("Please enter a valid number (Between 1 and 20)")
        else:
            user_inputs_validity_dict["user_hire_qty"] = user_confirmed_hiring_quantity

    except ValueError:
        print("Please enter a number (only digits)")

# User Receipt Number
    user_inputs_validity_dict["user_receipt_num"] = int(receipt_number_label["text"].replace(" Receipt Number : ", ""))
    print(receipt_number_label["text"])

# hire date
    user_inputs_validity_dict["user_hire_date"] = date_hire_gui_calendar.get_date()

    store_data(user_vals_dict = user_inputs_validity_dict)

def store_data(user_vals_dict):
    while True:
        new_users_data_dict = {user_vals_dict["user_name"]: {"user_receipt_num": user_vals_dict["user_receipt_num"],"user_hire_item": user_vals_dict["user_hire_item"],"user_hire_qty": user_vals_dict["user_hire_qty"],"user_hire_date": user_vals_dict["user_hire_date"]}}
        print(new_users_data_dict)
        try:
            with open(file= "users_data.json",mode = "r") as data_file:
                prev_users_data_dict = json.load(data_file)
                prev_users_data_dict.update(new_users_data_dict)
            with open(file= "users_data.json", mode = "w") as write_data_file:
                json.dump(obj= prev_users_data_dict ,fp= write_data_file, indent = 4)
                print(prev_users_data_dict)
                break

        except FileNotFoundError:
            with open(file="users_data.json", mode="w") as new_data_file:
                json.dump(obj= new_users_data_dict ,fp= new_data_file, indent = 4)
                print(new_users_data_dict)
                break

        except JSONDecodeError:
            standard_backup_user_info = {'test_user': {'user_receipt_num': 000000, 'user_hire_item': 'Nothing', 'user_hire_qty': 1, 'user_hire_date': '00/00/0000'}}
            with open(file= "users_data.json",mode = "w") as empty_data_file:
                json.dump(standard_backup_user_info, fp=empty_data_file, indent= 4)

#jst placing and simple logic after this :




#Main Title Frame
title_frame = tk.Frame(root, bg= "#102542", pady = 20)
title_frame.place(x= 0, y = 0, width= 700)

#actual Main Title
title_label = tk.Label(title_frame, text = "⚡ BYTES & BOLTS TECH HIRE ⚡", font= ("Arial",22, "bold"), bg = "#102542")
title_label.pack()

hire_menu_label = tk.Label(text= "Hire A Item!!!", bg = "#D7E9FA", fg = "Black", font = ("Arial", 20, "bold"))
hire_menu_label.place(x=300, y =100)

hire_widgets_frame = tk.Frame(root, bg = "White")
hire_widgets_frame.place(x= 100, y=150, width=500, height = 415)

user_current_r_num  = check_and_gen_vald_receipt_num() # this wont work cause new user needs new user r num
receipt_number_label = tk.Label(hire_widgets_frame,text= f" Receipt Number : {user_current_r_num}")
receipt_number_label.place(x = 175, y = 15)

name_entry_label = tk.Label(hire_widgets_frame, text = "Name", bg = "white", fg= "black")
name_entry_label.place(x = 60, y = 55)
name_entry = tk.Entry(hire_widgets_frame, width=30)
name_entry.place(x = 150, y = 55)

hire_item_label = tk.Label(hire_widgets_frame, text= "Hire Item", bg = "white", fg= "black")
hire_item_label.place(x = 60, y = 100)

hire_item_combo_box = ttk.Combobox(hire_widgets_frame,values=items_available_list)
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

confirm_hire_button = tk.Button(hire_widgets_frame, text= "Hire Item", background= "white", height= 2, width= 8, command= lambda: confirm_inputs_vald())
confirm_hire_button.place(x = 200, y = 365)

root.mainloop()