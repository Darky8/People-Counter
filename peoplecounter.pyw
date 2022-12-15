import tkinter as tk
import customtkinter as ctk

app = ctk.CTk()
app.title('People Counter')
app.geometry('300x180')
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
Label = ctk.CTkLabel
StringVar = ctk.StringVar
Font_tuple = ("Eras Bold ITC", 40)

class Counter():
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1
        counter_display.config(text=self.count)
        return self.count

    def sub(self):
        self.count -= 1
        if self.count < 0:
            self.count = 0
        counter_display.config(text=self.count)
        return self.count

    def __repr__(self):
        return str(self.count)


counter = Counter()

counter_display = tk.Label(app, text=counter, background='#242424', fg='#fcfdff')

add_one = ctk.CTkButton(
    master=app,
    text='+1',
    command=counter.add,
    height=40,
    width=80,
    font= Font_tuple

)
add_one.place(relx=0.3, rely=0.65, anchor=tk.CENTER)

sub_one = ctk.CTkButton(
    master=app,
    text='-1',
    command=counter.sub,
    height=40,
    width=80,
    font= Font_tuple
)
sub_one.place(relx=0.7, rely=0.65, anchor=tk.CENTER)

counter_display.configure(font = Font_tuple)

counter_display.pack()

app.mainloop()