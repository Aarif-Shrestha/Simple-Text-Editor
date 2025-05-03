import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font,colorchooser,filedialog
import os


main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title("Vpad Text Editor")

#####################################----- Main Menu------------#######################################


main_menu = tk.Menu()

# for file menu  ///////////////////////////////
file_menu = tk.Menu(main_menu,tearoff=0)

# to add icons  //////////////////////////////
new_icon = tk.PhotoImage(file="icons2/new.png")                 
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")


#for edit menu /////////////////////////////////////////////////////////////////////////////
edit_menu = tk.Menu(main_menu,tearoff=0)

# to add icons   ////////////////////
copy_icon = tk.PhotoImage(file="icons2/copy.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
cut_icon = tk.PhotoImage(file="icons2/cut.png")
clear_all_icon = tk.PhotoImage(file = "icons2/clear_all.png")
find_icon = tk.PhotoImage(file="icons2/find.png")

# for view menu /////////////////////////////////
view_menu = tk.Menu(main_menu,tearoff=0)

# to add icons
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")


#for color theme /////////////////
color_theme_menu = tk.Menu(main_menu,tearoff=0)

# to add icons ////////////////////////
light_default_icon = tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
red_icon = tk.PhotoImage(file="icons2/red.png")
monokai_icon = tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons2/night_blue.png")

# to add radio button of color ////////////////////////////////
color_var = tk.StringVar()
color_icon = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict ={
    'Light Default ' : ('#000000', '#ffffff'),              
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


# to display we need to cascade
 
main_menu.add_cascade(label = "File", menu = file_menu)
main_menu.add_cascade(label = "Edit", menu = edit_menu)
main_menu.add_cascade(label = "View", menu = view_menu)
main_menu.add_cascade(label = "Color Theme", menu = color_theme_menu)



# -------------------------&&&&&&&&&&&& End Menu &&&&&&&&&---------------------------------------------




#####################################-----  Tool Bar------------#######################################



tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP , fill = tk.X)    # X for horizontal

# FONT BOX 

font_family_var = tk.StringVar()
font_family = ttk.Combobox(tool_bar_label,width = 20 , textvariable=font_family_var, state= "readonly")
font_family["values"]= tk.font.families()          # always tuple
font_family.current(font_family["values"].index('Arial'))
font_family.grid(row=0, column=0, padx=5)


# Font size box
font_size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label, width= 16, textvariable=font_size_var , state="readonly")
font_size['values'] = tuple(range(8,80,2))      # always tuple
font_size.current(0)
font_size.grid(row= 0 , column=1, padx=5 )


# for bold button 

bold_icon = tk.PhotoImage(file="icons2/bold.png")

bold_button = ttk.Button(tool_bar_label, image=bold_icon)
bold_button.grid(row=0 , column=3, padx=5)

# for italic button

italic_icon = tk.PhotoImage(file="icons2/italic.png")

italic_button = ttk.Button(tool_bar_label, image=italic_icon)
italic_button.grid(row = 0, column=4,padx=5)

# for underline button

underline_icon = tk.PhotoImage(file="icons2/underline.png")

underline_button = ttk.Button(tool_bar_label, image=underline_icon)
underline_button.grid(row = 0, column=5,padx=5)

# for font color

font_color_icon = tk.PhotoImage(file="icons2/font_color.png")

font_color_button = ttk.Button(tool_bar_label, image=font_color_icon)
font_color_button.grid(row= 0, column=6,padx=5)

# for  align

left_align_icon = tk.PhotoImage(file="icons2/align_left.png")
center_align_icon = tk.PhotoImage(file="icons2/align_center.png")
right_align_icon = tk.PhotoImage(file="icons2/align_right.png")


align_left_button = ttk.Button(tool_bar_label, image=left_align_icon)
align_left_button.grid(row = 0, column=7,padx=5)


align_center_button = ttk.Button(tool_bar_label, image=center_align_icon)
align_center_button.grid(row = 0, column=8,padx=5)

align_right_button = ttk.Button(tool_bar_label, image=right_align_icon)
align_right_button.grid(row = 0, column=9,padx=5)



# -------------------------&&&&&&&&&&&& End Tool Bar &&&&&&&&&---------------------------------------------





#####################################----- Text Editor------------#######################################


text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief = tk.FLAT)   
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT, fill= tk.Y)           # Y means vertical
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)            
text_editor.config(yscrollcommand=scroll_bar.set)       

# FUNCTIONALITY OF COMBOBOX FONTS SIZE AND FAMILY

initial_font_family = "Arial"
initial_font_size = 8




def change_font(any_argument):
    global initial_font_family,initial_font_size          
    initial_font_family = font_family_var.get()
    initial_font_size = font_size_var.get()
    text_editor.configure(font=(initial_font_family,initial_font_size))

font_family.bind("<<ComboboxSelected>>",change_font)         
font_size.bind("<<ComboboxSelected>>",change_font)

# for bold button 
  

def bold_func():
    text_property = tk.font.Font(font= text_editor['font'])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font=(initial_font_family,initial_font_size,"bold"))
    
    elif text_property.actual()["weight"] == "bold":
        text_editor.configure(font=(initial_font_family,initial_font_size,"normal"))



bold_button.configure(command= bold_func)   


# for italic button



def italic_func():
    text_property2 = tk.font.Font(font = text_editor["font"])
    if text_property2.actual()["slant"] == "roman":
        text_editor.configure(font=(initial_font_family,initial_font_size,"italic"))
    if text_property2.actual()["slant"] == "italic":
        text_editor.configure(font=(initial_font_family,initial_font_size,"roman"))
    
italic_button.configure(command= italic_func)    


# for underline button 

def underline_func():
    text_property3 = tk.font.Font(font= text_editor['font'])
    if text_property3.actual()["underline"] == 0:
        text_editor.configure(font=(initial_font_family,initial_font_size,"underline"))
    if text_property3.actual()["underline"] == 1:
        text_editor.configure(font=(initial_font_family,initial_font_size,"normal"))


underline_button.config(command=underline_func)


# for font_color button

def color_func():
    color = tk.colorchooser.askcolor()
    text_editor.configure(fg=color[1])         

font_color_button.configure(command = color_func) 

# for left align

def left_func():
    text_content = text_editor.get(1.0, "end")    #Retrieve Text from the Text Editor:
    text_editor.tag_config('left', justify="left")    #  (justify="left"): Each line of text starts from the left side of the widget.
    text_editor.delete(1.0, "end")
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_button.configure(command=left_func)


# for right align
def right_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config("right",justify="right")
    text_editor.delete(1.0 , 'end')
    text_editor.insert(tk.INSERT , text_content,'right')

align_right_button.configure(command=right_func)


# for center align
def center_func():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center',justify="center")
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_button.configure(command=center_func)



text_editor.configure(font=('Arial',8))     
# -------------------------&&&&&&&&&&&& End Text Editor &&&&&&&&&---------------------------------------------




#####################################----- Main Status Bar------------#######################################

status_bar = ttk.Label(main_application, text="Status Bar")
status_bar.pack(side = tk.BOTTOM)


# for functionality of status bar


text_change = False   

def status_func(any_argument):
    global text_change
    if text_editor.edit_modified():         # checks whether the text has been modified since the last time the modified flag was reset.
        text_change = True              #end-1c means to exclude the last character, which is typically a newline.
        words=len(text_editor.get(1.0 ,'end-1c').split())    
                                                           
        characters = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f"Chracters:{characters}, Words:{words}")  
                                                                  
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", status_func)

# -------------------------&&&&&&&&&&&& End main Status Bar &&&&&&&&&---------------------------------------------




#####################################----- Main Menu Functionality------------#######################################

# to add file commands
url = ""

# functionality of new button

def new_file(event=None):      
    global url                  
    text_editor.delete(1.0 , tk.END)


file_menu.add_command(label="New", image=new_icon , compound=tk.LEFT, accelerator='CTRL + N', command = new_file)

main_application.bind("<Control-n>",new_file)          # bind shortcut key

#functionality of open button

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(('Text files','*.txt'),('All files','*.*')))
    try:
        with open(url, 'r') as f:               
            text_editor.delete(1.0, tk.END)         
            text_editor.insert(1.0, f.read())
            
           
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
file_menu.add_command(label='Open', image=open_icon , compound=tk.LEFT , accelerator="CTRL + O", command=open_file)

main_application.bind("<Control-o>",open_file)

# functionality of save button

def save(event= None):
    global url
    try:
        if url:
            content = text_editor.get(1.0, tk.END)
            with open(url,'w') as f:          
                f.write(content)
                
        else:      
            url = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension='.txt', filetypes=(('Text files','*.txt'),('All files','*.*')))    
            with open(url,'w') as f:
                f.write(text_editor.get(1.0, tk.END))
    except:
        return



file_menu.add_command(label='Save', image=save_icon , compound=tk.LEFT , accelerator="CTRL + S",command=save)

main_application.bind("<Control-s>",save)
 
# functionality of save as button

def save_as(event=None):
    global url
    url = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension='.txt', filetypes=(('Text files','*.txt'),('All files','*.*')))    
    try:
        with open(url,'w') as f:
            f.write(text_editor.get(1.0, 'end-1c'))
    except:
        pass

file_menu.add_command(label='Save as', image=save_as_icon , compound=tk.LEFT , accelerator="CTRL + ALT + S", command=save_as)

main_application.bind("<Control-Alt-s>",save_as)

# functionality of exit button
def exit(event=None):
    global url,text_change
    try:
        if text_change:   
            msg = messagebox.askyesnocancel('Exit','Do you want to save?') 
            if msg is True: 
                if url:       # true means yes
                    with open(url,'w') as f:
                        f.write(text_editor.get(1.0,tk.END))
                        main_application.destroy()
                else:
                    url = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension='.txt',filetypes=(('Text files','*.txt'),     ('All files','*.*')))
                    with open(url,'w') as f:
                        f.write(text_editor.get(1.0,tk.END))
                        main_application.destroy()
            elif msg is False:            # false means no
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        pass

file_menu.add_command(label='Exit', image=exit_icon , compound=tk.LEFT , accelerator="CTRL + Q",command=exit)

main_application.bind("<Control-q>",exit)

# to add edit commands

edit_menu.add_command(label="Copy", image=copy_icon, compound=tk.LEFT , accelerator="CTRL + C  ", command=lambda:text_editor.event_generate('<Control c>'))
edit_menu.add_command(label="Paste", image=paste_icon, compound=tk.LEFT , accelerator="CTRL + V",command=lambda:text_editor.event_generate('<Control v>'))
edit_menu.add_command(label="Cut", image=cut_icon, compound=tk.LEFT , accelerator="CTRL + X",command=lambda:text_editor.event_generate('<Control x>'))
edit_menu.add_command(label="Clear All", image=clear_all_icon, compound=tk.LEFT , accelerator="CTRL + ALT + C",command=lambda:text_editor.delete(1.0,tk.END))

# for functionality of find button
def find(event=None):
    find_box = tk.Toplevel()
    find_box.geometry('450x250+500+200')
    find_box.title('Find')
    find_box.resizable(0,0)           

    find_frame = tk.LabelFrame(find_box, text="Find/Replace")
    find_frame.pack(pady = 5)

    find_label = tk.Label(find_frame,text = 'Find :')
    find_label.grid(row=0, column=0 )

    replace_label = tk.Label(find_frame, text="Replace : ")
    replace_label.grid(row= 1, column=0)

    find_entry = tk.Entry(find_frame, width=30)
    find_entry.grid(row= 0 ,column=1,padx =4 ,pady= 4)

    replace_entry = tk.Entry(find_frame, width= 30)
    replace_entry.grid(row = 1, column= 1 ,padx=4, pady=4 )

    def find_words(event=None): 
        word = find_entry.get()
        text_editor.tag_remove('highlight',1.0,tk.END)       # removes any highlight in the text editor
        if word:                             
            starting_pos = '1.0'
            while True:              # Find the next occurrence of the word
                starting_pos = text_editor.search(word, starting_pos, stopindex=tk.END)       
                if not starting_pos:            
                    break
                ending_pos = f'{starting_pos}+{len(word)}c'   
                text_editor.tag_add('highlight',starting_pos,ending_pos)        
                starting_pos=ending_pos             #
        text_editor.tag_config('highlight',foreground='red', background='yellow')
                


    find_button = tk.Button(find_frame, text="Find",command = find_words)
    find_button.grid(row = 2, column=0, padx=8 , pady=4)


    def replace_words(event=None):
        word = find_entry.get()
        replace_word = replace_entry.get()
        content = text_editor.get(1.0,tk.END)
        content_replaced = content.replace(word,replace_word)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0 ,content_replaced)

    replace_button = tk.Button(find_frame, text="Replace", command = replace_words)
    replace_button.grid(row = 2, column=1,padx=8, pady=4)




    find_box.mainloop()
edit_menu.add_command(label="Find", image=find_icon, compound=tk.LEFT , accelerator="CTRL + F", command=find)

main_application.bind("<Control-f>",find)

# to add view  checkbutton

view_toolbar = tk.BooleanVar()
view_toolbar.set(True)
view_statusbar = tk.BooleanVar()
view_statusbar.set(True)


def t_bar_func():
    global view_toolbar
    if view_toolbar:          
        tool_bar_label.pack_forget()
        view_toolbra = False                     
    else:
        text_editor.pack_forget()          
        status_bar.pack_forget()           
        tool_bar_label.pack(side = tk.TOP, fill= tk.X)     
        text_editor.pack(fill=tk.BOTH, expand=True)       
        status_bar.pack(side=tk.BOTTOM)            
        view_toolbar = True

def status_bar_func():
    global view_statusbar
    if view_statusbar:
        status_bar.pack_forget()
        view_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)         
        view_statusbar = True


view_menu.add_checkbutton(label="Tool bar",image=tool_bar_icon,onvalue=True, offvalue=False , variable=view_toolbar, compound=tk.LEFT,command = t_bar_func)     

view_menu.add_checkbutton(label="Status bar",image=status_bar_icon,onvalue=True, offvalue=False,variable=view_statusbar, compound=tk.LEFT,command=status_bar_func)

# to add radio button for color using loop

def color():
    color_select = color_var.get()      
    color_tuple = color_dict.get(color_select)      
    fg,bg = color_tuple[0],color_tuple[1]           
    text_editor.config(background=bg , foreground=fg)


count=0
for i in color_dict:
    color_theme_menu.add_radiobutton(label=i, image=color_icon[count], variable=color_var, compound=tk.LEFT,command = color)
    count =count+1


# -------------------------&&&&&&&&&&&& End Main Menu Functionality &&&&&&&&&---------------------------------------------



main_application.config(menu=main_menu)        # to call menubar

main_application.mainloop() 