import tkinter.tix
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()

data = []
inv = []
cases_with = []


class RemInvestigator:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"

        ass_frame = Frame(width=50,
                          bg=background_color,
                          pady=10)
        ass_frame.grid()

        add_heading_label = Label(ass_frame,
                                  text="Assign Investigator",
                                  font="Arial 15 bold",
                                  bg=background_color,
                                  padx=0,
                                  pady=10)
        add_heading_label.grid(row=0, column=0)

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

        last_frame = Frame(ass_frame)
        last_frame.grid(row=4, pady=10)

        last_label = Label(last_frame,
                           font=main_font,
                           text="Last Name",
                           width=11,
                           bg=background_color)
        last_label.grid(row=1, column=0)

        self.last_entry = Entry(last_frame,
                                width=31,
                                state=DISABLED)
        self.last_entry.grid(row=1, column=1)

        first_frame = Frame(ass_frame)
        first_frame.grid(row=5, pady=0)

        first_label = Label(first_frame,
                            font=main_font,
                            text="First Name",
                            width=11,
                            bg=background_color)
        first_label.grid(row=1, column=0)

        self.first_entry = Entry(first_frame,
                                 width=31,
                                 state=DISABLED)
        self.first_entry.grid(row=1, column=1)

        inv_frame = Frame(ass_frame,
                          bg=background_color)
        inv_frame.grid(row=6, pady=0)

        inv_label = Label(inv_frame,
                          font=main_font,
                          text="Investigators",
                          width=14,
                          anchor="e",
                          bg=background_color)
        inv_label.grid(row=0, column=0)

        self.inv_combo = ttk.Combobox(inv_frame,
                                      width=32,
                                      state=DISABLED)
        self.inv_combo.grid(row=0, column=1, pady=10, padx=10)
        self.inv_combo.current()
        self.inv_combo.bind("<<ComboboxSelected>>", self.enable)

        button_frame = Frame(ass_frame,
                             bg=background_color)
        button_frame.grid(row=8, pady=15)

        self.return_button = Button(button_frame,
                                    text="Return\nto Menu",
                                    width=12)
        self.return_button.grid(row=0, column=0, padx=2)

        self.rem_button = Button(button_frame,
                                 text="Remove\nInvestigator",
                                 width=12,
                                 command=self.rem_inv,
                                 state=DISABLED)
        self.rem_button.grid(row=0, column=1, padx=2)

    def dropdown(self):
        global data
        data = []
        cursor.execute("SELECT DISTINCT CaseID FROM ASSIGNMENT")
        for row in cursor.fetchall():
            caid = row[0]
            cursor.execute("SELECT * FROM CASES WHERE CaseID=? AND status=?", (caid, "Current"))
            for row in cursor.fetchall():
                data.append(f"{row[1]}, {row[2]}")
                continue
        return data

    def enable(self, parent):
        self.rem_button.config(state=NORMAL)

    def investigators(self):
        global data
        data = []
        case_id = self.ID_entry.get()
        cursor.execute("SELECT * FROM ASSIGNMENT WHERE CaseID=?", (case_id,))
        for row in cursor.fetchall():
            id = row[2]
            hours = str(row[3])
            hours = "Hours: " + hours
            cursor.execute("SELECT * FROM INVESTIGATOR WHERE InvestigatorID=?", (id,))
            for row in cursor.fetchall():
                data.append(f"{row[0]}, {row[1]},{row[2]} {hours}")

        return data

    def showinfo(self, parent):
        selected_list = self.combo_box.get()
        selected_split = selected_list.split(",")
        case_id = selected_split[0]
        case = []

        cursor.execute("SELECT * FROM CASES WHERE CaseID=?", (case_id,))
        for row in cursor.fetchall():
            case.append(f"{row[1]}, {row[2]}")
            continue

        case_string = ' '.join(map(str, case))
        case_split = case_string.split(",")
        client_id = case_split[0]
        client = []

        cursor.execute("SELECT * FROM CLIENT WHERE ClientID=?", (client_id,))
        for row in cursor.fetchall():
            client.append(f"{row[1]}, {row[2]}")
            continue

        client_string = ' '.join(map(str, client))
        client_split = client_string.split(",")
        last = client_split[0]
        first = client_split[1]
        description = case_split[1]

        self.ID_entry.config(state=NORMAL)
        self.ID_entry.delete(0, 'end')
        self.ID_entry.insert(0, case_id)
        self.ID_entry.config(state=DISABLED)

        self.description_entry.config(state=NORMAL)
        self.description_entry.delete(0, 'end')
        self.description_entry.insert(0, description)
        self.description_entry.config(state=DISABLED)

        self.first_entry.config(state=NORMAL)
        self.first_entry.delete(0, 'end')
        self.first_entry.insert(0, first)
        self.first_entry.config(state=DISABLED)

        self.last_entry.config(state=NORMAL)
        self.last_entry.delete(0, 'end')
        self.last_entry.insert(0, last)
        self.last_entry.config(state=DISABLED)

        self.inv_combo['state'] = 'readonly'
        self.inv_combo.config(value=self.investigators())

    def rem_inv(self):
        selected_list = self.inv_combo.get()
        selected_split = selected_list.split(",")
        inv_id = selected_split[0]
        if inv_id == "":
            messagebox.showerror("Failure", "Please select an investigator")
        else:
            cursor.execute("DELETE FROM ASSIGNMENT WHERE InvestigatorID=?", (inv_id,))
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
            self.description_entry.config(state=NORMAL)
            self.description_entry.delete(0, 'end')
            self.description_entry.config(state=DISABLED)

            self.combo_box.set('')
            self.combo_box['value'] = self.dropdown()

            self.inv_combo.set('')
            self.inv_combo['value'] = self.investigators()
            messagebox.showinfo("Success", "Investigator Deleted Successfully")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BD App")
    root.resizable(width=False, height=False)
    something = RemInvestigator(root)
    root.mainloop()
