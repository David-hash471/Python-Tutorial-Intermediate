import globals as glob
import tkinter as tk
import session_func, global_func, uploadSession_func, home_func


def root_setup():
    
    glob.root.title("STUDY TRACKER")
    window_width = 400
    window_height = 250
    screen_width = glob.root.winfo_screenwidth() 
    screen_height = glob.root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    glob.root.resizable(False, False)
    glob.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    glob.root.iconbitmap(r'C:\Users\david\OneDrive\Documents\Personal\David\Projects\Python projects\Python Tutorial\Python-Tutorial-Intermediate\TASK 01 FOR LESSON 01-10\Assets\book_3725.ico')
    for i in range(3):
        glob.root.rowconfigure(i, weight= 1)
        glob.root.columnconfigure(i, weight= 1)

def create_pages():
    
    for name in ('session', 'home', 'upload session'):
        page = tk.Frame(glob.root)
        page.grid(row = 1, column=0, sticky= tk.NSEW)
        glob.pages[name] = [page, False]
        
        for i in range(4):
            glob.pages[name][0].rowconfigure(i, weight= 1)
            glob.pages[name][0].columnconfigure(i, weight= 1)


def show_page(page_name):
    

    match page_name:
        case 'home':
            home_func.setup_home()
            
            
        case 'session':
            if not glob.session_rvh_initialized:
                session = glob.Reset_values_holder('session')
                glob.session_rvh_initialized = True
            session_func.setup_session()
        case 'upload session':
            uploadSession_func.setup_uploadSession()
            
        case _:
            pass

    glob.pages[page_name][0].tkraise() 


 

        
        
 