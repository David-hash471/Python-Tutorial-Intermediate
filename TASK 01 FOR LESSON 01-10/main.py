import tkinter as tk 
from tkinter import ttk
import session_func, global_func, uploadSession_func, home_func
import globals as glob



if __name__ == '__main__':

    global_func.root_setup()
    global_func.create_pages()
    global_func.show_page('home')
    glob.root.mainloop()
    