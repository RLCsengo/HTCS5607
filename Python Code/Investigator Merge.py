from tkinter import *
from threading import Timer
import sqlite3
from tkinter import ttk
from tkinter import messagebox
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()
username = ""
data = []


class Login:

    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"
        # Login Frame
        self.login_frame = Frame(width=50,
                                 bg=background_color,
                                 pady=10)
        self.login_frame.grid()

        # Login Heading (row 0)
        self.login_heading_label = Label(self.login_frame,
                                         text="Login",
                                         font="Arial 15 bold",
                                         bg=background_color,
                                         padx=10)
        self.login_heading_label.grid(row=0)

        # User frame (row 1)
        self.user_frame = Frame(self.login_frame)
        self.user_frame.grid(row=1, pady=5, padx=30)

        self.username_label = Label(self.user_frame,
                                    font=main_font,
                                    text="Username",
                                    width=8,
                                    bg=background_color)
        self.username_label.grid(row=0, column=0)

        self.user_entry = Entry(self.user_frame,
                                width=15)
        self.user_entry.grid(row=0, column=1)

        # Pass frame (row 2)
        self.pass_frame = Frame(self.login_frame)
        self.pass_frame.grid(row=2, pady=0)

        self.pass_label = Label(self.pass_frame,
                                font=main_font,
                                text="Password",
                                width=8,
                                bg=background_color)
        self.pass_label.grid(row=1, column=0)

        self.pass_entry = Entry(self.pass_frame,
                                width=15,
                                show="*")
        self.pass_entry.grid(row=1, column=1)

        # Button frame (row 3)
        self.button_frame = Frame(self.login_frame,
                                  bg=background_color)
        self.button_frame.grid(row=3, pady=10)

        self.close_button = Button(self.button_frame,
                                   text="Close",
                                   width=8,
                                   command=quit)
        self.close_button.grid(row=0, column=0, padx=5)

        self.login_button = Button(self.button_frame,
                                   text="Login",
                                   width=8,
                                   command=self.check_login)
        self.login_button.grid(row=0, column=1, padx=5)

    def check_login(self):
        global username
        self.user_entry.config(bg="white")
        self.pass_entry.config(bg="white")
        # checks answer and configures buttons based on whether or not the answer was correct
        try:
            user_input = self.user_entry.get()
            pass_input = self.pass_entry.get()

            if user_input == "payroll":
                if pass_input == "5545":
                    username = "payroll"
                    self.login_heading_label.config(text="Logging in...")
                    self.close_button.config(state="disabled")
                    self.login_button.config(state="disabled")
                    self.user_entry.config(state="disabled")
                    self.pass_entry.config(state="disabled")
                    t = Timer(3.0, self.to_menu)
                    t.start()

                else:
                    self.login_heading_label.config(text="Wrong Password")
                    self.pass_entry.config(bg="#FF0000")
                    self.pass_entry.delete(0, 'end')

            elif user_input == "admin":
                if pass_input == "4454":
                    username = "admin"
                    self.login_heading_label.config(text="Logging in...")
                    self.close_button.config(state="disabled")
                    self.login_button.config(state="disabled")
                    self.user_entry.config(state="disabled")
                    self.pass_entry.config(state="disabled")
                    t = Timer(3.0, self.to_menu)
                    t.start()

                else:
                    self.login_heading_label.config(text="Wrong Password")
                    self.pass_entry.delete(0, 'end')
                    self.pass_entry.config(bg="#FF0000")

            else:
                self.login_heading_label.config(text="Wrong Username")
                self.user_entry.config(bg="#FF0000")
                self.user_entry.delete(0, 'end')
                self.pass_entry.delete(0, 'end')

        except ValueError:
            print("ERROR")

    def to_menu(self):
        Menu(self)
        self.login_frame.destroy()


class Menu:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"

        # Login Frame
        self.menu_frame = Frame(width=50,
                                bg=background_color,
                                pady=10)
        self.menu_frame.grid()

        # Login Heading (row 0)
        self.menu_heading_label = Label(self.menu_frame,
                                        text="Main Menu",
                                        font="Arial 15 bold",
                                        bg=background_color,
                                        padx=50)
        self.menu_heading_label.grid(row=0)

        self.button_frame = Frame(self.menu_frame,
                                  bg=background_color)
        self.button_frame.grid(row=1, pady=10, padx=10)

        self.AddInv_button = Button(self.button_frame,
                                    text="Add Investigator",
                                    width=16, command=self.to_add)
        self.AddInv_button.grid(row=0, column=0, padx=2, pady=2)

        self.UptInv_button = Button(self.button_frame,
                                    text="Update Investigator",
                                    width=16, command=self.to_upt)
        self.UptInv_button.grid(row=1, column=0, padx=2, pady=2)

        self.DelInv_button = Button(self.button_frame,
                                    text="Delete Investigator",
                                    width=16, command=self.to_del)
        self.DelInv_button.grid(row=2, column=0, padx=2, pady=2)

        self.InvRep_button = Button(self.button_frame,
                                    text="Produce Investigator\n"
                                         "Report",
                                    width=16)
        self.InvRep_button.grid(row=3, column=0, padx=2, pady=2)

        self.AssInv_button = Button(self.button_frame,
                                    text="Assign Investigator",
                                    width=16)
        self.AssInv_button.grid(row=0, column=1, padx=2, pady=2)

        self.RemInv_button = Button(self.button_frame,
                                    text="Remove Investigator",
                                    width=16)
        self.RemInv_button.grid(row=1, column=1, padx=2, pady=2)

        self.CloCas_button = Button(self.button_frame,
                                    text="Close Case",
                                    width=16)
        self.CloCas_button.grid(row=2, column=1, padx=2, pady=2)

        self.AssRep_button = Button(self.button_frame,
                                    text="Produce Assignments\n"
                                         "Report",
                                    width=16)
        self.AssRep_button.grid(row=3, column=1, padx=2, pady=2)

        self.close_button = Button(self.button_frame,
                                   text="Close",
                                   width=16,
                                   command=quit)
        self.close_button.grid(row=4, column=0, padx=5, pady=15)

        if username == "payroll":
            self.AssInv_button.config(state=DISABLED)
            self.RemInv_button.config(state=DISABLED)
            self.CloCas_button.config(state=DISABLED)
            self.AssRep_button.config(state=DISABLED)

    def to_add(self):
        AddInvestigator(self)
        self.menu_frame.destroy()

    def to_upt(self):
        UptInvestigator(self)
        self.menu_frame.destroy()

    def to_del(self):
        DelInvestigator(self)
        self.menu_frame.destroy()


class AddInvestigator:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"
        # Add Frame
        self.add_frame = Frame(width=50,
                               bg=background_color,
                               pady=10)
        self.add_frame.grid()

        # Add Heading (row 0)
        self.add_heading_label = Label(self.add_frame,
                                       text="Add Investigator",
                                       font="Arial 15 bold",
                                       bg=background_color,
                                       padx=50)
        self.add_heading_label.grid(row=0)

        self.ID_frame = Frame(self.add_frame, bg=background_color)
        self.ID_frame.grid(row=1, pady=10, padx=30)

        self.limit_label = Label(self.ID_frame,
                                 font="Arial 8",
                                 text="between 1 - 99999",
                                 width=15,
                                 bg=background_color)
        self.limit_label.grid(row=0, column=1)

        self.ID_label = Label(self.ID_frame,
                              font=main_font,
                              text="ID",
                              width=11,
                              bg=background_color)
        self.ID_label.grid(row=1, column=0)

        self.ID_entry = Entry(self.ID_frame,
                              width=15)
        self.ID_entry.grid(row=1, column=1)

        # Last Name frame (row 1)
        self.last_frame = Frame(self.add_frame)
        self.last_frame.grid(row=2, pady=0, padx=30)

        self.lastname_label = Label(self.last_frame,
                                    font=main_font,
                                    text="Last Name",
                                    width=11,
                                    bg=background_color)
        self.lastname_label.grid(row=0, column=0)

        self.last_entry = Entry(self.last_frame,
                                width=15)
        self.last_entry.grid(row=0, column=1)

        # First Name frame (row 2)
        self.first_frame = Frame(self.add_frame)
        self.first_frame.grid(row=3, pady=10)

        self.first_label = Label(self.first_frame,
                                 font=main_font,
                                 text="First Name",
                                 width=11,
                                 bg=background_color)
        self.first_label.grid(row=1, column=0)

        self.first_entry = Entry(self.first_frame,
                                 width=15,)
        self.first_entry.grid(row=1, column=1)

        # Street Address

        self.street_frame = Frame(self.add_frame)
        self.street_frame.grid(row=4, pady=0)

        self.street_label = Label(self.street_frame,
                                  font=main_font,
                                  text="Street Address",
                                  width=11,
                                  bg=background_color)
        self.street_label.grid(row=1, column=0)

        self.street_entry = Entry(self.street_frame,
                                  width=15,)
        self.street_entry.grid(row=1, column=1)

        # Suburb

        self.suburb_frame = Frame(self.add_frame)
        self.suburb_frame.grid(row=5, pady=10)

        self.suburb_label = Label(self.suburb_frame,
                                  font=main_font,
                                  text="Suburb",
                                  width=11,
                                  bg=background_color)
        self.suburb_label.grid(row=1, column=0)

        self.suburb_entry = Entry(self.suburb_frame,
                                  width=15, )
        self.suburb_entry.grid(row=1, column=1)

        # Phone Number

        self.phone_frame = Frame(self.add_frame)
        self.phone_frame.grid(row=6, pady=0)

        self.phone_label = Label(self.phone_frame,
                                 font=main_font,
                                 text="Phone Number",
                                 width=11,
                                 bg=background_color)
        self.phone_label.grid(row=1, column=0)

        self.phone_entry = Entry(self.phone_frame,
                                 width=15, )
        self.phone_entry.grid(row=1, column=1)

        # Hourly Rate

        self.rate_frame = Frame(self.add_frame, bg=background_color)
        self.rate_frame.grid(row=7, pady=0)

        self.rate_limit_label = Label(self.rate_frame,
                                      font="Arial 8",
                                      text="between 25 - 200",
                                      width=15,
                                      bg=background_color)
        self.rate_limit_label.grid(row=0, column=1)

        self.rate_label = Label(self.rate_frame,
                                font=main_font,
                                text="Hourly Rate",
                                width=11,
                                bg=background_color)
        self.rate_label.grid(row=1, column=0)

        self.rate_entry = Entry(self.rate_frame,
                                width=15, )
        self.rate_entry.grid(row=1, column=1)

        # Button frame (row 3)
        self.button_frame = Frame(self.add_frame,
                                  bg=background_color)
        self.button_frame.grid(row=8, pady=15)

        self.return_button = Button(self.button_frame,
                                    text="Return\nto Menu",
                                    width=12, command=self.to_menu)
        self.return_button.grid(row=0, column=0, padx=2)

        self.add_button = Button(self.button_frame,
                                 text="Add\nInvestigator",
                                 width=12,
                                 command=self.add_new_inv)
        self.add_button.grid(row=0, column=1, padx=2)

    def to_menu(self):
        Menu(self)
        self.add_frame.destroy()

    def add_new_inv(self):
        inv_id = self.ID_entry.get()
        lastname = self.last_entry.get()
        firstname = self.first_entry.get()
        address = self.street_entry.get()
        suburb = self.suburb_entry.get()
        phone = self.phone_entry.get()
        rate = self.rate_entry.get()
        id_list = []
        if inv_id == "" or lastname == "" or firstname == "" or address == "" \
                or suburb == "" or phone == "" or rate == "":
            messagebox.showerror("Failure", "Please fill in all entries")
        else:
            int_id = int(inv_id)
            int_rate = int(rate)
            cursor.execute("SELECT InvestigatorID FROM INVESTIGATOR")
            for row in cursor.fetchall():
                id_list.append(f"{row[0]}")

            if inv_id in id_list:
                messagebox.showerror("Failure", "ID already exists")

            else:
                if 0 < int_id < 100000:
                    if 24 < int_rate < 201:
                        cursor.execute("INSERT INTO INVESTIGATOR(InvestigatorID, lastName,firstName,hourlyRate,"
                                       "streetAddress,suburb,phoneNumber)"
                                       "VALUES(?,?,?,?,?,?,?)",
                                       (inv_id, lastname, firstname, rate, address, suburb, phone))
                        db.commit()

                        self.ID_entry.delete(0, 'end')
                        self.last_entry.delete(0, 'end')
                        self.first_entry.delete(0, 'end')
                        self.street_entry.delete(0, 'end')
                        self.suburb_entry.delete(0, 'end')
                        self.phone_entry.delete(0, 'end')
                        self.rate_entry.delete(0, 'end')
                        messagebox.showinfo("Success", "Investigator Added Successfully")
                    else:
                        messagebox.showerror("Failure", "Rate must be within range")
                else:
                    messagebox.showerror("Failure", "ID must be within range")


class DelInvestigator:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"
        # Add Frame
        self.del_frame = Frame(width=50,
                               bg=background_color,
                               pady=10)
        self.del_frame.grid()

        self.add_heading_label = Label(self.del_frame,
                                       text="Delete Investigator",
                                       font="Arial 15 bold",
                                       bg=background_color,
                                       padx=0)
        self.add_heading_label.grid(row=0, column=0)

        self.combo_frame = Frame(self.del_frame)
        self.combo_frame.grid(row=1, pady=5, padx=30)

        self.combo_label = Label(self.combo_frame,
                                 font=main_font,
                                 text="Investigators",
                                 width=11,
                                 bg=background_color)
        self.combo_label.grid(row=0, column=0)

        self.combo_box = ttk.Combobox(self.combo_frame,
                                      width=20)
        self.combo_box.grid(row=0, column=1)
        self.combo_box['value'] = self.dropdown()
        self.combo_box['state'] = 'readonly'
        self.combo_box.current()
        self.combo_box.bind("<<ComboboxSelected>>", self.showinfo)

        self.ID_frame = Frame(self.del_frame)
        self.ID_frame.grid(row=2, pady=5, padx=30)

        self.ID_label = Label(self.ID_frame,
                              font=main_font,
                              text="ID",
                              width=11,
                              bg=background_color)
        self.ID_label.grid(row=0, column=0)

        self.ID_entry = Entry(self.ID_frame,
                              width=15)
        self.ID_entry.grid(row=0, column=1)

        self.ID_entry.config(state=DISABLED)

        # Last Name frame (row 3)

        self.last_frame = Frame(self.del_frame)
        self.last_frame.grid(row=3, pady=5, padx=30)

        self.lastname_label = Label(self.last_frame,
                                    font=main_font,
                                    text="Last Name",
                                    width=11,
                                    bg=background_color)
        self.lastname_label.grid(row=0, column=0)

        self.last_entry = Entry(self.last_frame,
                                width=15)
        self.last_entry.grid(row=0, column=1)

        self.last_entry.config(state=DISABLED)

        # First Name frame (row 4)
        self.first_frame = Frame(self.del_frame)
        self.first_frame.grid(row=4, pady=5)

        self.first_label = Label(self.first_frame,
                                 font=main_font,
                                 text="First Name",
                                 width=11,
                                 bg=background_color)
        self.first_label.grid(row=1, column=0)

        self.first_entry = Entry(self.first_frame,
                                 width=15,)
        self.first_entry.grid(row=1, column=1)

        self.first_entry.config(state=DISABLED)

        # Street Address

        self.street_frame = Frame(self.del_frame)
        self.street_frame.grid(row=5, pady=5)

        self.street_label = Label(self.street_frame,
                                  font=main_font,
                                  text="Street Address",
                                  width=11,
                                  bg=background_color)
        self.street_label.grid(row=1, column=0)

        self.street_entry = Entry(self.street_frame,
                                  width=15,)
        self.street_entry.grid(row=1, column=1)

        self.street_entry.config(state=DISABLED)

        # Suburb

        self.suburb_frame = Frame(self.del_frame)
        self.suburb_frame.grid(row=6, pady=5)

        self.suburb_label = Label(self.suburb_frame,
                                  font=main_font,
                                  text="Suburb",
                                  width=11,
                                  bg=background_color)
        self.suburb_label.grid(row=1, column=0)

        self.suburb_entry = Entry(self.suburb_frame,
                                  width=15, )
        self.suburb_entry.grid(row=1, column=1)

        self.suburb_entry.config(state=DISABLED)

        # Phone Number

        self.phone_frame = Frame(self.del_frame)
        self.phone_frame.grid(row=7, pady=5)

        self.phone_label = Label(self.phone_frame,
                                 font=main_font,
                                 text="Phone Number",
                                 width=11,
                                 bg=background_color)
        self.phone_label.grid(row=1, column=0)

        self.phone_entry = Entry(self.phone_frame,
                                 width=15, )
        self.phone_entry.grid(row=1, column=1)

        self.phone_entry.config(state=DISABLED)

        # Hourly Rate

        self.rate_frame = Frame(self.del_frame)
        self.rate_frame.grid(row=8, pady=5)

        self.rate_label = Label(self.rate_frame,
                                font=main_font,
                                text="Hourly Rate",
                                width=11,
                                bg=background_color)
        self.rate_label.grid(row=1, column=0)

        self.rate_entry = Entry(self.rate_frame,
                                width=15, )
        self.rate_entry.grid(row=1, column=1)

        self.rate_entry.config(state=DISABLED)

        # Button frame (row 3)
        self.button_frame = Frame(self.del_frame,
                                  bg=background_color)
        self.button_frame.grid(row=9, pady=10)

        self.return_button = Button(self.button_frame,
                                    text="Return\nto Menu",
                                    width=12, command=self.to_menu)
        self.return_button.grid(row=0, column=0, padx=2)

        self.del_button = Button(self.button_frame,
                                 text="Delete\nInvestigator",
                                 width=12, command=self.delete)
        self.del_button.grid(row=0, column=1, padx=2)

    def to_menu(self):
        Menu(self)
        self.del_frame.destroy()

    def dropdown(self):
        global data
        data = []
        cursor.execute("SELECT InvestigatorID, lastName, firstName FROM INVESTIGATOR")
        for row in cursor.fetchall():
            data.append(f"{row[0]}, {row[1]}, {row[2]}")
        return data

    def showinfo(self, parent):
        selectedlist = self.combo_box.get()
        selectedsplit = selectedlist.split(",")
        inv_id = selectedsplit[0]
        selected = []

        cursor.execute("SELECT * FROM INVESTIGATOR WHERE InvestigatorID=?", (inv_id,))
        for row in cursor.fetchall():
            selected.append(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}")
            continue
        selected_string = ' '.join(map(str, selected))
        split = selected_string.split(",")
        first = split[2]
        last = split[1]
        rate = '$' + split[3]
        address = split[4]
        suburb = split[5]
        phone = split[6]

        self.ID_entry.config(state=NORMAL)
        self.ID_entry.delete(0, 'end')
        self.ID_entry.insert(0, inv_id)
        self.ID_entry.config(state=DISABLED)

        self.first_entry.config(state=NORMAL)
        self.first_entry.delete(0, 'end')
        self.first_entry.insert(0, first)
        self.first_entry.config(state=DISABLED)

        self.last_entry.config(state=NORMAL)
        self.last_entry.delete(0, 'end')
        self.last_entry.insert(0, last)
        self.last_entry.config(state=DISABLED)

        self.rate_entry.config(state=NORMAL)
        self.rate_entry.delete(0, 'end')
        self.rate_entry.insert(0, rate)
        self.rate_entry.config(state=DISABLED)

        self.street_entry.config(state=NORMAL)
        self.street_entry.delete(0, 'end')
        self.street_entry.insert(0, address)
        self.street_entry.config(state=DISABLED)

        self.suburb_entry.config(state=NORMAL)
        self.suburb_entry.delete(0, 'end')
        self.suburb_entry.insert(0, suburb)
        self.suburb_entry.config(state=DISABLED)

        self.phone_entry.config(state=NORMAL)
        self.phone_entry.delete(0, 'end')
        self.phone_entry.insert(0, phone)
        self.phone_entry.config(state=DISABLED)

    def delete(self):
        selected_list = self.combo_box.get()
        selected_split = selected_list.split(",")
        inv_id = selected_split[0]
        if inv_id == "":
            messagebox.showerror("Failure", "Please select an investigator")
        else:
            cursor.execute("DELETE FROM INVESTIGATOR WHERE InvestigatorID=?", (inv_id,))
            db.commit()
            self.ID_entry.config(state=NORMAL)
            self.ID_entry.delete(0, 'end')
            self.ID_entry.config(state=DISABLED)
            self.first_entry.config(state=NORMAL)
            self.first_entry.delete(0, 'end')
            self.first_entry.config(state=DISABLED)
            self.last_entry.config(state=NORMAL)
            self.last_entry.delete(0, 'end')
            self.last_entry.config(state=DISABLED)
            self.rate_entry.config(state=NORMAL)
            self.rate_entry.delete(0, 'end')
            self.rate_entry.config(state=DISABLED)
            self.street_entry.config(state=NORMAL)
            self.street_entry.delete(0, 'end')
            self.street_entry.config(state=DISABLED)
            self.suburb_entry.config(state=NORMAL)
            self.suburb_entry.delete(0, 'end')
            self.suburb_entry.config(state=DISABLED)
            self.phone_entry.config(state=NORMAL)
            self.phone_entry.delete(0, 'end')
            self.phone_entry.config(state=DISABLED)
            self.combo_box.set('')
            self.combo_box['value'] = self.dropdown()
            messagebox.showinfo("Success", "Investigator Deleted Successfully")


class UptInvestigator:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"
        # Add Frame
        self.upt_frame = Frame(width=50,
                               bg=background_color,
                               pady=10)
        self.upt_frame.grid()

        self.add_heading_label = Label(self.upt_frame,
                                       text="Update Investigator",
                                       font="Arial 15 bold",
                                       bg=background_color,
                                       padx=0, pady=10)
        self.add_heading_label.grid(row=0, column=0)

        self.combo_frame = Frame(self.upt_frame)
        self.combo_frame.grid(row=1, pady=0, padx=30)

        self.combo_label = Label(self.combo_frame,
                                 font=main_font,
                                 text="Investigators",
                                 width=11,
                                 bg=background_color)
        self.combo_label.grid(row=0, column=0)

        self.combo_box = ttk.Combobox(self.combo_frame,
                                      width=20)
        self.combo_box.grid(row=0, column=1)
        self.combo_box['value'] = self.dropdown()
        self.combo_box['state'] = 'readonly'
        self.combo_box.current()
        self.combo_box.bind("<<ComboboxSelected>>", self.showinfo)

        self.ID_frame = Frame(self.upt_frame)
        self.ID_frame.grid(row=2, pady=10, padx=30)

        self.ID_label = Label(self.ID_frame,
                              font=main_font,
                              text="ID",
                              width=11,
                              bg=background_color)
        self.ID_label.grid(row=0, column=0)

        self.ID_entry = Entry(self.ID_frame,
                              width=15)
        self.ID_entry.grid(row=0, column=1)

        self.ID_entry.config(state=DISABLED)

        # Last Name frame (row 3)
        self.last_frame = Frame(self.upt_frame)
        self.last_frame.grid(row=3, pady=0, padx=30)

        self.lastname_label = Label(self.last_frame,
                                    font=main_font,
                                    text="Last Name",
                                    width=11,
                                    bg=background_color)
        self.lastname_label.grid(row=0, column=0)

        self.last_entry = Entry(self.last_frame,
                                width=15)
        self.last_entry.grid(row=0, column=1)

        # First Name frame (row 4)
        self.first_frame = Frame(self.upt_frame)
        self.first_frame.grid(row=4, pady=10)

        self.first_label = Label(self.first_frame,
                                 font=main_font,
                                 text="First Name",
                                 width=11,
                                 bg=background_color)
        self.first_label.grid(row=1, column=0)

        self.first_entry = Entry(self.first_frame,
                                 width=15,)
        self.first_entry.grid(row=1, column=1)

        # Street Address

        self.street_frame = Frame(self.upt_frame)
        self.street_frame.grid(row=5, pady=0)

        self.street_label = Label(self.street_frame,
                                  font=main_font,
                                  text="Street Address",
                                  width=11,
                                  bg=background_color)
        self.street_label.grid(row=1, column=0)

        self.street_entry = Entry(self.street_frame,
                                  width=15)
        self.street_entry.grid(row=1, column=1)

        # Suburb

        self.suburb_frame = Frame(self.upt_frame)
        self.suburb_frame.grid(row=6, pady=10)

        self.suburb_label = Label(self.suburb_frame,
                                  font=main_font,
                                  text="Suburb",
                                  width=11,
                                  bg=background_color)
        self.suburb_label.grid(row=1, column=0)

        self.suburb_entry = Entry(self.suburb_frame,
                                  width=15)
        self.suburb_entry.grid(row=1, column=1)

        # Phone Number

        self.phone_frame = Frame(self.upt_frame)
        self.phone_frame.grid(row=7, pady=0)

        self.phone_label = Label(self.phone_frame,
                                 font=main_font,
                                 text="Phone Number",
                                 width=11,
                                 bg=background_color)
        self.phone_label.grid(row=1, column=0)

        self.phone_entry = Entry(self.phone_frame,
                                 width=15)
        self.phone_entry.grid(row=1, column=1)

        # Hourly Rate

        self.rate_frame = Frame(self.upt_frame, bg=background_color)
        self.rate_frame.grid(row=8, pady=0)

        self.rate_limit_label = Label(self.rate_frame,
                                      font="Arial 8",
                                      text="between 25 - 200",
                                      width=15,
                                      bg=background_color)
        self.rate_limit_label.grid(row=0, column=1)

        self.rate_label = Label(self.rate_frame,
                                font=main_font,
                                text="Hourly Rate",
                                width=11,
                                bg=background_color)
        self.rate_label.grid(row=1, column=0)

        self.rate_entry = Entry(self.rate_frame,
                                width=15, )
        self.rate_entry.grid(row=1, column=1)

        # Button frame (row 3)
        self.button_frame = Frame(self.upt_frame,
                                  bg=background_color)
        self.button_frame.grid(row=9, pady=15)

        self.return_button = Button(self.button_frame,
                                    text="Return\nto Menu",
                                    width=12, command=self.to_menu)
        self.return_button.grid(row=0, column=0, padx=2)

        self.del_button = Button(self.button_frame,
                                 text="Update\nInvestigator",
                                 width=12, command=self.upt_inv)
        self.del_button.grid(row=0, column=1, padx=2)

    def to_menu(self):
        Menu(self)
        self.upt_frame.destroy()

    def dropdown(self):
        global data
        data = []
        cursor.execute("SELECT InvestigatorID, lastName, firstName FROM INVESTIGATOR")
        for row in cursor.fetchall():
            data.append(f"{row[0]}, {row[1]}, {row[2]}")
        return data

    def showinfo(self, parent):
        selected_list = self.combo_box.get()
        selected_split = selected_list.split(",")
        inv_id = selected_split[0]
        selected = []

        cursor.execute("SELECT * FROM INVESTIGATOR WHERE InvestigatorID=?", (inv_id,))
        for row in cursor.fetchall():
            selected.append(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}")
            continue
        selected_string = ' '.join(map(str, selected))
        split = selected_string.split(",")
        first = split[2]
        last = split[1]
        rate = split[3]
        address = split[4]
        suburb = split[5]
        phone = split[6]

        self.ID_entry.config(state=NORMAL)
        self.ID_entry.delete(0, 'end')
        self.ID_entry.insert(0, inv_id)
        self.ID_entry.config(state=DISABLED)

        self.first_entry.delete(0, 'end')
        self.first_entry.insert(0, first)

        self.last_entry.delete(0, 'end')
        self.last_entry.insert(0, last)

        self.rate_entry.delete(0, 'end')
        self.rate_entry.insert(0, rate)

        self.street_entry.delete(0, 'end')
        self.street_entry.insert(0, address)

        self.suburb_entry.delete(0, 'end')
        self.suburb_entry.insert(0, suburb)

        self.phone_entry.delete(0, 'end')
        self.phone_entry.insert(0, phone)

    def upt_inv(self):
        selected_list = self.combo_box.get()
        selected_split = selected_list.split(",")
        inv_id = selected_split[0]
        lastname = self.last_entry.get()
        firstname = self.first_entry.get()
        address = self.street_entry.get()
        suburb = self.suburb_entry.get()
        phone = self.phone_entry.get()
        rate = self.rate_entry.get()
        if inv_id == "" or lastname == "" or firstname == "" or address == "" \
                or suburb == "" or phone == "" or rate == "":
            messagebox.showerror("Failure", "Please fill in all entries")
        else:
            int_rate = int(rate)
            if 24 < int_rate < 201:
                cursor.execute("INSERT OR REPLACE INTO INVESTIGATOR(InvestigatorID, lastName,firstName,hourlyRate,"
                               "streetAddress,suburb,phoneNumber)"
                               "VALUES(?,?,?,?,?,?,?)", (inv_id, lastname, firstname, rate, address, suburb, phone))
                db.commit()

                self.ID_entry.config(state=NORMAL)
                self.ID_entry.delete(0, 'end')
                self.ID_entry.config(state=DISABLED)
                self.first_entry.delete(0, 'end')
                self.last_entry.delete(0, 'end')
                self.rate_entry.delete(0, 'end')
                self.street_entry.delete(0, 'end')
                self.suburb_entry.delete(0, 'end')
                self.phone_entry.delete(0, 'end')
                self.combo_box.set('')
                self.combo_box['value'] = self.dropdown()
                messagebox.showinfo("Success", "Investigator Updated Successfully")
            else:
                messagebox.showerror("Failure", "Rate must be within range")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BD App")
    root.resizable(width=False, height=False)
    something = Login(root)
    root.mainloop()
