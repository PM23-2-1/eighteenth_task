import tkinter as tk
import desctop_view

def main(): 
    root = tk.Tk()
    app = desctop_view.main_window(root)
    root.mainloop()

if __name__ == '__main__':
    main()