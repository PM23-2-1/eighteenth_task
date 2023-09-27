import tkinter as tk
import db_names

class main_window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.button1 = tk.Button(self.frame, text = 'New database', width = 25, command = self.new_database)
        self.button1.pack()

        self.name_db = tk.Text(self.frame)
        self.name_db.pack()

        self.lbl = tk.Label(self.frame, text = "")
        self.lbl.pack()

        self.frame.pack()

        self.newWindow = tk.Toplevel(self.master)
        self.app = Data_bases(self.newWindow)

    def new_database(self):
        name = db_names.DB_names()
        name.set_name(self.name_db.get(1.0, 'end-1c'))
        self.lbl.config(text = self.name_db.get(1.0, 'end-1c'))

class Data_bases:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.button1 = tk.Button(self.frame, text = 'Update', width = 25, command = self.update)
        self.button1.pack()

        name = db_names.DB_names()
        self.lbl = tk.Label(self.frame, text = name.get_name())
        self.lbl.pack()

        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def update(self, ):
        name = db_names.DB_names()
        self.lbl.config(text=name.get_name())

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = main_window(root)
    root.mainloop()

if __name__ == '__main__':
    main()