import globals as glob
import tkinter as tk
import session_func, global_func, uploadSession_func, home_func


def root_setup():
    
    glob.root.title("STUDY TRACKER")
    window_width = 400
    window_height = 200
    screen_width = glob.root.winfo_screenwidth() 
    screen_height = glob.root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    glob.root.resizable(False, False)
    glob.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    glob.root.iconbitmap(r'C:\Users\david\OneDrive\Documents\Personal\David\Projects\Python projects\Python Tutorial\Python-Tutorial-Intermediate\TASK 01 FOR LESSON 01-10\Assets\book_3725.ico')
    

def create_pages():
    
    for name in ('session', 'home', 'upload session'):
        page = tk.Frame(glob.root)
        page.place(width= 400, height= 200)
        glob.pages[name] = [page, False]
        



def show_page(page_name):
    

    match page_name:
        case 'home':
            home_func.setup_home()
            glob.pages[page_name][0].tkraise()
            
        case 'session':
            session_func.reset_set_choice()
            if not glob.pages['session'][1]:
                session = glob.Widget_container('session')
                session_st = glob.Task('session_st')
                glob.pages['session'][1] = True
            else:
                pass
            if glob.return_obj(glob.st_objs, 'session_st').return_st() == 0:
                session_func.setup_session()
                glob.return_obj(glob.st_objs,'session_st').change_st()
                glob.pages[page_name][0].tkraise()
            elif glob.return_obj(glob.st_objs, 'session_st').return_st() == 1:
                glob.pages[page_name][0].tkraise() #change state in functionality
            elif glob.return_obj(glob.st_objs, 'session_st').return_st() == 2:
                session_func.clear_session()
                glob.return_obj(glob.st_objs, 'session_st').change_st()
                
                show_page(page_name)

        case 'upload session':
            uploadSession_func.setup_uploadSession()
            glob.pages[page_name][0].tkraise()

        case _:
            pass

     


 

        
        
 