from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
global f_size
global f_style
global given_title
global curr_color
global name
global fsize
global curr_style
global root0
global win
global counter
def main():
    def da_click():

        given_title = str(name.get())
        f_size = int(fsize.get())
        f_style = curr_style.get()
        f_color = curr_color.get()
        root0.destroy()
        win = Tk()
        win.title(given_title + " - WINQ-v1.0.1")
        win.geometry("1200x660+350+200")
        da_frame = tk.Frame(win, width= 400, height= 400).pack_propagate(0)
 
        da_bar = tk.Scrollbar(da_frame)
        da_bar.pack(side=RIGHT, fill=Y)

        menubar = tk.Menu(win)
        win.config(menu=menubar)
        def new_file():
            win.destroy()
            main()
        def save_file():
            text_file = filedialog.asksaveasfilename(initialfile=given_title+'.txt',title='Open File', filetypes=(("Text Files", "*.txt")))
            if text_file:
                text_file = open(text_file, 'w')
                text_file.write(text_area.get(1.0, END))
                text_file.close()
            
        def open_file():
            
            try:
                text_area.delete('1.0', END)
                text_file = filedialog.askopenfilename(title='Open File', filetypes=(("Text Files", "*.txt")))
                #win.title(text_file.replace("C:\Users\mrmeh\OneDrive\Documents", "") + " - WINQ-v1.0.0")

                text_file = open(text_file, 'r')
                thing = text_file.read()
                text_area.insert(END, thing)
                text_file.close()
                x = str(len(text_area.get('1.0', END)))
                counter.config(text="")
                counter.config(text="Characters:"+ x)
            except:
                messagebox.showwarning("Runtime error", "Some Error Occured")

        def Ultrapro():
            from TextFind import lol
            lol(text_area.get(1.0, END))

        File_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=File_menu)
        File_menu.add_command(label="New",command=new_file)
        File_menu.add_command(label="Save",command=save_file)
        File_menu.add_command(label="Open",command=open_file)
        File_menu.add_separator()
        File_menu.add_command(label="Exit",command=win.destroy)

        Edit_Menu = tk.Menu(menubar, tearoff =0)
        menubar.add_cascade(label= "Edit", menu=Edit_Menu)
        Edit_Menu.add_command(label = "Find Text", command=Ultrapro)

        text_area = tk.Text(da_frame, width=1, height=1, font=( f_style, f_size),background='white', selectforeground='yellow',selectbackground='black',foreground=f_color, wrap= WORD, undo= True, yscrollcommand=da_bar.set)
        text_area.pack(fill="both", expand=True, padx=20, pady=20)
        da_bar.config(command=text_area.yview)
        char_counter = tk.Label(win, text="")
        char_counter.pack(side="right")
        word_counter = tk.Label(win, text="")
        word_counter.pack(side = "right")
        def WordCount(arg):
            count = 0 
            length = len(arg)
            i =0
            if(arg == " "*len(arg)):
                pass
            else:
                arg = arg.strip(" ")
                while(arg[0] != '' and i < length):
                    new_str = arg[0:arg.find(" ")+1]
                    latter_str = arg[arg.find(" ")+1::]
                    arg = latter_str
                    if(new_str != ''and new_str != " "):
                        count += 1
                    else:
                        pass
                    i+=1
            return count+1
        def update(event):
            x = str(len(text_area.get('1.0', END)))
            char_counter.config(text="")
            char_counter.config(text="Characters:"+ x + " ")
            count = WordCount(text_area.get('1.0', END))
            word_counter.config(text="Words: "+str(count)+" ")
        
        text_area.bind('<KeyPress>', update)
        text_area.bind('<KeyRelease>', update)


        win.resizable(False, False)
        win.mainloop()

    root0 = Tk()
    root0.title('WINQ-v1.0.1')
    root0.geometry('600x300+700+300')

    my_label0 = tk.Label(root0, text="Enter details for ur text file!!", font=('Times New Roman', 20)).grid(row=0, column=2)
    ask_name = tk.Label(root0, text="     Give it a name:", font=('Times New Roman', 20)).grid(row=1, column=0)
    name = tk.Entry(root0, width=20, borderwidth=5, fg="blue")
    name.grid(row=1, column=1, columnspan=2)

    dash = tk.Label(root0, text=" ").grid(row=2, column=0,columnspan =3)
    ask_fsize = tk.Label(root0, text="    Enter Font Size:", font=('Times New Roman', 20)).grid(row=3, column=0)
    fsize = tk.Entry(root0, width=20, borderwidth=5)
    fsize.grid(row=3, column=1, columnspan=2)
    dash = tk.Label(root0, text=" ").grid(row=4, column=0,columnspan =3)
    ask_fstyle = tk.Label(root0, text= "   Enter Font Style:", font=('Times New Roman', 20)).grid(row=5, column=0)
    curr_style = StringVar()
    curr_style.set("Arial")
    styles = ['Arial', 'Times New Roman', 'Helvetica', 'MS Serif', 'Script', 'System', 'Courier']
    fstyle = tk.OptionMenu(root0, curr_style, *styles)
    fstyle.grid(row=5, column=2 , columnspan=2)
    dash = tk.Label(root0, text=" ").grid(row=6, column=0,columnspan =3)
    ask_fcolor = tk.Label(root0, text= "   Enter Font Color:", font=('Times New Roman', 20)).grid(row=7, column=0)
    curr_color = StringVar()
    curr_color.set("black")
    colors = ['black', 'blue', 'red', 'orange', 'yellow', 'green', 'brown', 'violet', 'grey']
    fcolor = tk.OptionMenu(root0, curr_color, *colors)
    fcolor.grid(row=7, column=2 , columnspan=2)
    bu = tk.Button(root0, text="Submit",  font=('Times New Roman', 20),command=da_click).grid(row=9, column=0, columnspan=3)


    root0.resizable(False,False)
    root0.mainloop()

main()