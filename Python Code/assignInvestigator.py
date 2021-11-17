from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()

data = []


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
                                    width=12)
        self.return_button.grid(row=0, column=0, padx=2)

        self.del_button = Button(self.button_frame,
                                 text="Update\nInvestigator",
                                 width=12, command=self.upt_inv)
        self.del_button.grid(row=0, column=1, padx=2)

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
    something = UptInvestigator(root)
    root.mainloop()
