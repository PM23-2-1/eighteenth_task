import tkinter as tk
import db_names
import db

class main_window:
    def __init__(self, master):
        self.master = master
        self.new_db_frame = tk.Frame(self.master)
        self.buttons_frame = tk.Frame(self.master)

        self.button1 = tk.Button(self.new_db_frame, text = 'New database', width = 10, command = self.new_database)
        self.button1.pack(side=tk.LEFT)

        self.name_db = tk.Text(self.new_db_frame, width=25, height=1)
        self.name_db.pack(side=tk.LEFT)

        self.lbl = tk.Label(self.buttons_frame, text = "")
        self.lbl.pack()

        self.button_view_db = tk.Button(self.buttons_frame, text = 'View database', width = 10, command = self.new_view_db)
        self.button_view_db.pack()

        self.new_db_frame.pack()
        self.buttons_frame.pack()

        self.newWindow = tk.Toplevel(self.master)
        self.app = Data_bases(self.newWindow)

    def new_database(self):
        name = db_names.DB_names()
        name.set_name(self.name_db.get(1.0, 'end-1c'))
        self.lbl.config(text = self.name_db.get(1.0, 'end-1c'))

    def new_view_db(self, ):
        self.newWindow = tk.Toplevel(self.master)
        self.view = Data_bases(self.newWindow)

class Data_bases:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)

        self.button1 = tk.Button(self.frame, text = 'Update', width = 8, command = self.update)
        self.button1.pack(side=tk.LEFT)

        name = db_names.DB_names()
        self.lbl = tk.Label(self.frame, text = '')
        self.lbl.pack(side=tk.LEFT)

        self.quitButton = tk.Button(self.bot_frame, text = 'Quit', width = 15, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        self.bot_frame.pack()

    def update(self, ):
        db_get_names = db.Databases()
        self.lbl.config(text='\n'.join([i['Database'] for i in db_get_names.get_databases()]))

    def close_windows(self):
        self.master.destroy()

class view_db:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

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