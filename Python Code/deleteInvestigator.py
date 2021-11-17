from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()

data = []


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
                                    width=12)
        self.return_button.grid(row=0, column=0, padx=2)

        self.del_button = Button(self.button_frame,
                                 text="Delete\nInvestigator",
                                 width=12, command=self.delete)
        self.del_button.grid(row=0, column=1, padx=2)

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BD App")
    root.resizable(width=False, height=False)
    something = DelInvestigator(root)
    root.mainloop()
