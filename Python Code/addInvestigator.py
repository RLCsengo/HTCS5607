from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()


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
                                    width=12)
        self.return_button.grid(row=0, column=0, padx=2)

        self.add_button = Button(self.button_frame,
                                 text="Add\nInvestigator",
                                 width=12,
                                 command=self.add_new_inv)
        self.add_button.grid(row=0, column=1, padx=2)

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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BD App")
    root.resizable(width=False, height=False)
    something = AddInvestigator(root)
    root.mainloop()
