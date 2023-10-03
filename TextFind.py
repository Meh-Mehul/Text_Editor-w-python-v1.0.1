# ultimate goal is to make MS word becoz no money
from tkinter import *
global yo
global yo0
global start_pos
global end_pos
def lol(data):
    def da_click():
        yo = entry0.get('1.0', 'end-1c')

        yo0 = str(entry1.get())
        m =0
        k = len(yo)
        j = len(yo0)
        
        for i in range(k-j+1 ):
            for x in range(j):
                a = yo[i:i+j]
                if(a==yo0):
                    m=m+1
                    for l in range(1,entry0.count('1.0', 'end', 'displaylines')[0]+1):
                        start_pos= entry0.search(yo0, l/10, stopindex='end-1c')
                        end_pos = '{}+{}c'.format(start_pos, len(yo0))
                        entry0.tag_add("start",start_pos, end_pos)
                        entry0.tag_configure("start", background="OliveDrab1", foreground="Black")
                        for f in range(73):
                            try:
                                start_pos= entry0.search(yo0, end_pos, stopindex='end-1c')
                                end_pos ='{}+{}c'.format(start_pos, len(yo0))
                                entry0.tag_add("start",start_pos, end_pos)
                                entry0.tag_configure("start", background="OliveDrab1", foreground="Black")

                                
                            except:
                                pass
                        
                    break
        finallabel = Label(win_dow, text=m, font=('Arial', 15, 'bold')).grid(row=6, column=1)




    win_dow = Tk()
    win_dow.title("Text Find")
    win_dow.geometry("600x500+750+300")
    label0 = Label(win_dow, text="Enter text to be checked:", font=('Arial', 15, 'bold')).grid(row=0, column=0, columnspan=3)
    entry0 = Text(win_dow, width = 73, height = 15, wrap = WORD, padx = 10, pady = 10)
    entry0.grid(row=1,column=0,columnspan=3)
    entry0.insert(END, str(data))
    label1 = Label(win_dow, text=" Enter word/phrase to be counted:", font=('Arial', 15, 'bold')).grid(row=2, column = 0, columnspan=3)
    entry1 = Entry(win_dow,width=25, borderwidth=5 )
    entry1.grid(row=3,column=1)
    bu = Button(win_dow, text="Count!", font=('Arial',15,'bold'),command=da_click)
    bu.grid(row=4, column=1)


    win_dow.mainloop()
lol(" ")