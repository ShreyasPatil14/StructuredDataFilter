from tkinter import *
from tkinter import ttk
import openpyxl
import Global

# display dataset
def display(flag, file):
    
    w = None
    
    if(flag == 0):  # for input data
        Global.org_window = Toplevel()
        w = Global.org_window
        w.overrideredirect(TRUE)
        w.attributes('-topmost',True)
        w.title("input data")
        w.geometry("1020x370+20+90")
        
    else:  # for processed data
        Global.pro_window = Toplevel()
        w = Global.pro_window
        w.overrideredirect(TRUE)
        w.attributes('-topmost',True)
        w.title("processed data")
        w.geometry("1020x370+20+470")
        
    w.resizable(False,False)
    
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    
    values = list(sheet.values)
    
    cols = values[0]
    
    tree = ttk.Treeview(w, column=cols, show="headings")
    
    verScroll = Scrollbar(w, orient='vertical', command=tree.yview)
    verScroll.pack(side='right',fill='y')
    horScroll = Scrollbar(w, orient='horizontal', command=tree.xview)
    horScroll.pack(side='bottom',fill='x')
    
    tree.configure(xscrollcommand=verScroll.set)
    tree.configure(yscrollcommand=horScroll.set)
    
    for col_name in cols:
        tree.heading(col_name, text=col_name)
        
    tree.pack(side=LEFT, fill=BOTH, expand=TRUE)
    
    for value in values[1:]:
        tree.insert('', END, values=value)
    
    