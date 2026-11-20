import globals as glob
import global_func
from tkinter import ttk
import tkinter as tk



def setup_home():
    ttk.Button(glob.pages['home'][0], text= 'Start a session', command= lambda: global_func.show_page('session')).place(x=0, y=0, width= 400, height= 50)


