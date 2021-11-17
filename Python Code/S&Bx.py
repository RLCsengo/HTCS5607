self.combo_box = ttk.Combobox(self.combo_frame,
                              width=20)
self.combo_box.grid(row=0, column=1)

self.combo_box['value'] = self.dropdown()

self.combo_box['state'] = 'readonly'

def dropdown(self):
    cursor.execute("SELECT lastName, firstName FROM INVESTIGATOR")
    data = []
    for row in cursor.fetchall():
        data.append(row[1])
    return data
