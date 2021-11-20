from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()

data = []


class AssInvestigator:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"

        # Assignment Frame
        ass_frame = Frame(width=50,
                          bg=background_color,
                          pady=10)
        ass_frame.grid()

        add_heading_label = Label(ass_frame,
                                  text="Close Case",
                                  font="Arial 15 bold",
                                  bg=background_color,
                                  padx=0,
                                  pady=10)
        add_heading_label.grid(row=0, column=0)

        # Combo Frame (Row 1 of Assignment Frame)
        combo_frame = Frame(ass_frame,
                            bg=background_color)
        combo_frame.grid(row=1, padx=15)

        combo_label = Label(combo_frame,
                            font=main_font,
                            text="Cases",
                            width=14,
                            bg=background_color,
                            anchor="e")
        combo_label.grid(row=0, column=0)

        self.combo_box = ttk.Combobox(combo_frame,
                                      width=46)
        self.combo_box.grid(row=0, column=1, pady=10)
        self.combo_box['value'] = self.dropdown()
        self.combo_box['state'] = 'readonly'
        self.combo_box.current()
        self.combo_box.bind("<<ComboboxSelected>>", self.showinfo)

        # ID Frame (Row 2 of Assignment Frame)
        id_frame = Frame(ass_frame)
        id_frame.grid(row=2, pady=10, padx=30)

        id_label = Label(id_frame,
                         font=main_font,
                         text="ID",
                         width=11,
                         bg=background_color)
        id_label.grid(row=0, column=0)

        self.ID_entry = Entry(id_frame,
                              width=31,
                              state=DISABLED)
        self.ID_entry.grid(row=0, column=1)

        # Last Frame (Row 3 of Assignment Frame)
        description_frame = Frame(ass_frame)
        description_frame.grid(row=3, pady=0, padx=30)

        description_label = Label(description_frame,
                                  font=main_font,
                                  text="Description",
                                  width=11,
                                  bg=background_color)
        description_label.grid(row=0, column=0)

        self.description_entry = Entry(description_frame,
                                       width=31,
                                       state=DISABLED)
        self.description_entry.grid(row=0, column=1)

        date_frame = Frame(ass_frame)
        date_frame.grid(row=4, pady=10)

        date_label = Label(date_frame,
                           font=main_font,
                           text="Start Date",
                           width=11,
                           bg=background_color)
        date_label.grid(row=1, column=0)

        self.date_entry = Entry(date_frame,
                                width=31,
                                state=DISABLED)
        self.date_entry.grid(row=1, column=1)

        # Button Frame (Row 5 of Assignment Frame)
        button_frame = Frame(ass_frame,
                             bg=background_color)
        button_frame.grid(row=5, pady=15)

        self.return_button = Button(button_frame,
                                    text="Return\nto Menu",
                                    width=12)
        self.return_button.grid(row=0, column=0, padx=2)

        self.close_button = Button(button_frame,
                                   text="Close\nCase",
                                   width=12,
                                   command=self.clo_cas,
                                   state=DISABLED)
        self.close_button.grid(row=0, column=1, padx=2)

    def dropdown(self):
        global data
        payed_cases = []
        data = []
        cursor.execute("SELECT CaseID FROM PAYMENTS")
        for row in cursor.fetchall():
            payed_cases.append(f"{row[0]}")
        cases_string = ' '.join(map(str, payed_cases))

        cursor.execute("SELECT CaseID, caseDescription FROM CASES WHERE CaseID=? AND status=?", (cases_string, "Billed"))
        for row in cursor.fetchall():
            data.append(f"{row[0]}, {row[1]}")
        return data

    def showinfo(self, parent):
        selected_case = self.combo_box.get()
        selected_split = selected_case.split(",")
        case_id = selected_split[0]

        cursor.execute("SELECT * FROM CASES WHERE CaseID=?", (case_id,))
        for row in cursor.fetchall():
            case_description = row[2]
            date = row[3]

        self.ID_entry.config(state=NORMAL)
        self.ID_entry.delete(0, 'end')
        self.ID_entry.insert(0, case_id)
        self.ID_entry.config(state=DISABLED)

        self.description_entry.config(state=NORMAL)
        self.description_entry.delete(0, 'end')
        self.description_entry.insert(0, case_description)
        self.description_entry.config(state=DISABLED)

        self.date_entry.config(state=NORMAL)
        self.date_entry.delete(0, 'end')
        self.date_entry.insert(0, date)
        self.date_entry.config(state=DISABLED)

        self.close_button.config(state=NORMAL)

    def clo_cas(self):
        selected_case = self.combo_box.get()
        selected_split = selected_case.split(",")
        case_id = selected_split[0]
        price_amount = 0
        # cases_string = ' '.join(map(str, payed_cases))

        cursor.execute("SELECT * FROM EXPENDITURES WHERE CaseID=?", (case_id,))
        for row in cursor.fetchall():
            expense_id = row[2]
            amount = []
            amount = row[3]

            cursor.execute("SELECT * FROM EXPENSE WHERE ExpenseID=?", (expense_id,))
            for row in cursor.fetchall():
                cost = []
                cost = row[2]
                total_cost = cost*amount
                price_amount = price_amount+total_cost

            continue

        print(price_amount)

        cursor.execute("SELECT * FROM ASSIGNMENT WHERE CaseID=?", (case_id,))
        for row in cursor.fetchall():
            inv_id = row[2]
            inv_hours = row[3]

            cursor.execute("SELECT * FROM INVESTIGATOR WHERE InvestigatorID=?", (inv_id,))
            for row in cursor.fetchall():
                hourly_rate = []
                hourly_rate = row[3]
                hourly_total = hourly_rate * inv_hours
                price_amount = price_amount + hourly_total

        print(price_amount)

        cursor.execute("SELECT * FROM PAYMENTS WHERE CaseID=?", (case_id,))
        for row in cursor.fetchall():
            payment = []
            payment = row[2]
            price_amount = price_amount - payment

        print(price_amount)
        print(case_id)

        if price_amount == 0:
            client = []
            cursor.execute("SELECT * FROM CASES WHERE CaseID=?", (case_id,))
            for row in cursor.fetchall():
                client.append(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}")
                continue
            client_string = ' '.join(map(str, client))
            client_split = client_string.split(",")
            client_id = client_split[1]
            description = client_split[2]
            date = client_split[3]
            case_type = client_split[4]

            cursor.execute("INSERT OR REPLACE INTO CASES(CaseID,ClientID,caseDescription,startDate,caseType,status)"
                           "VALUES(?,?,?,?,?,?)",(case_id,client_id,description,date,case_type,"Closed"))
            db.commit()
            messagebox.showinfo("Success", "Case Closed Successfully")

            self.ID_entry.config(state=NORMAL)
            self.ID_entry.delete(0, 'end')
            self.ID_entry.config(state=DISABLED)

            self.description_entry.config(state=NORMAL)
            self.description_entry.delete(0, 'end')
            self.description_entry.config(state=DISABLED)

            self.date_entry.config(state=NORMAL)
            self.date_entry.delete(0, 'end')
            self.date_entry.config(state=DISABLED)

            self.combo_box.set('')
            self.combo_box['value'] = self.dropdown()

            self.close_button.config(state=DISABLED)

        else:
            txt = "There is ${unpaid:.2f} left unpaid"
            messagebox.showerror("Failure", txt.format(unpaid=price_amount))

            self.ID_entry.config(state=NORMAL)
            self.ID_entry.delete(0, 'end')
            self.ID_entry.config(state=DISABLED)

            self.description_entry.config(state=NORMAL)
            self.description_entry.delete(0, 'end')
            self.description_entry.config(state=DISABLED)

            self.date_entry.config(state=NORMAL)
            self.date_entry.delete(0, 'end')
            self.date_entry.config(state=DISABLED)

            self.combo_box.set('')
            self.combo_box['value'] = self.dropdown()

            self.close_button.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BD App")
    root.resizable(width=False, height=False)
    something = AssInvestigator(root)
    root.mainloop()
