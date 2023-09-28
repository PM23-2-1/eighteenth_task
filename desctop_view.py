import tkinter as tk
import db_names
import db

# main window
class main_window:
    def __init__(self, master):
        self.master = master
        self.new_db_frame = tk.Frame(self.master)
        self.buttons_frame = tk.Frame(self.master)

        # button and text to create new db
        self.button1 = tk.Button(self.new_db_frame, text = 'New database/\nConnnect', width = 10, command = self.new_database)
        self.button1.pack(side=tk.LEFT)

        self.name_db = tk.Text(self.new_db_frame, width=25, height=1)
        self.name_db.pack(side=tk.LEFT)

        self.lbl = tk.Label(self.buttons_frame, text ='')
        self.lbl.pack()

        # button to view window with databases
        self.button_view_db = tk.Button(self.buttons_frame, text = 'View databases', width = 10, command = self.new_view_db)
        self.button_view_db.pack()

        # button to view window with tables
        self.button_view_tables = tk.Button(self.buttons_frame, text = 'View tables', width = 10, command = self.new_view_tables)
        self.button_view_tables.pack()

        # frames packing
        self.new_db_frame.pack()
        self.buttons_frame.pack()

    # create new database/connect
    def new_database(self):
        name = db_names.DB_names()
        name.set_name(self.name_db.get(1.0, 'end-1c'))
        db_get_names = db.Databases()
        names = db_get_names.create_database()
        if names != None:
            self.lbl.config(text=f'Done {name.get_name()}')
            self.master.title(name.get_name())
        
    # create window to view databases
    def new_view_db(self, ):
        self.newWindow = tk.Toplevel(self.master)
        self.view = Data_bases(self.newWindow)

    # create window to view tables
    def new_view_tables(self, ):
        self.newWindow = tk.Toplevel(self.master)
        self.view = view_tables(self.newWindow)



# window to view db
class Data_bases:
    def __init__(self, master):
        self.master = master
        self.master.title('Databases')
        self.frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)

        # update button
        self.button1 = tk.Button(self.frame, text = 'Update', width = 8, command = self.update)
        self.button1.pack(side=tk.LEFT)

        # all databases
        db_get_names = db.Databases()
        names = db_get_names.get_databases()
        self.lbl = tk.Label(self.frame, text = '')
        self.lbl.pack(side=tk.LEFT)
        if names != None:
            self.lbl.config(text='\n'.join([i['Database'] for i in names]))
        

        # Quit button
        self.quitButton = tk.Button(self.bot_frame, text = 'Quit', width = 15, command = self.close_windows)
        self.quitButton.pack()

        # frames packing
        self.frame.pack()
        self.bot_frame.pack()

    # update databases
    def update(self, ):
        db_get_names = db.Databases()
        names = db_get_names.get_databases()
        if names != None:
            self.lbl.config(text='\n'.join([i['Database'] for i in names]))

    # close window
    def close_windows(self):
        self.master.destroy()




class view_tables:
    def __init__(self, master):
        self.master = master
        self.master.title('Tables')
        self.frame = tk.Frame(self.master)
        self.new_table_frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)

        # update button
        self.button1 = tk.Button(self.frame, text = 'Update', width = 8, command = self.update)
        self.button1.pack(side=tk.LEFT)

        # all tables
        db_get_names = db.Tables_in_db()
        names = db_get_names.get_tables()
        self.lbl = tk.Label(self.frame, text = '')
        self.lbl.pack(side=tk.LEFT)
        if names != None:
            self.lbl.config(text='\n'.join([list(i.values())[0] for i in names]))
        
        # Create table button
        self.create_table_button = tk.Button(self.new_table_frame, text = 'Create table', width = 15, command = self.create_table)
        self.create_table_button.pack(side=tk.LEFT)

        self.name_db_table = tk.Text(self.new_table_frame, width=25, height=1)
        self.name_db_table.pack(side=tk.LEFT)

        self.lbl_done = tk.Label(self.bot_frame, text ='')
        self.lbl_done.pack()

        # Quit button
        self.quitButton = tk.Button(self.bot_frame, text = 'Quit', width = 15, command = self.close_windows)
        self.quitButton.pack()

        # frames packing
        self.frame.pack()
        self.new_table_frame.pack()
        self.bot_frame.pack()

    # update databases
    def update(self, ):
        db_get_names = db.Tables_in_db()
        names = db_get_names.get_tables()
        if names != None:
            self.lbl.config(text='\n'.join([list(i.values())[0] for i in names]))

    def create_table(self, ):
        name = db_names.DB_names()
        if len(self.name_db_table.get(1.0, 'end-1c')) != 0:
            name.set_name_table(self.name_db_table.get(1.0, 'end-1c'))
            db_create_table = db.Tables_in_db()
            if db_create_table.create_table():
                self.update()
                self.lbl_done.config(text=f'Done {name.get_name_table()}')


    # close window
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = main_window(root)
    root.mainloop()

if __name__ == '__main__':
    main()