from tkinter import *
from tkcalendar import *

class CalendarUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Calendar')
        self.root.iconbitmap('C:/Users/95 computer/Downloads/dew_it.jpg')
        self.root.geometry("600x400")

        self.cal = Calendar(self.root, selectmode="day", year=2023, month=9, day=29)
        self.cal.pack(pady=20)

        self.my_label = Label(self.root, text="")
        self.my_label.pack(pady=20)

        my_button = Button(self.root, text="Get Date", command=self.grab_date)
        my_button.pack(pady=20)

    def grab_date(self):
        self.my_label.config(text=self.cal.get_date())

if __name__ == "__main__":
    root = Tk()
    app = CalendarUI(root)
    root.mainloop()
