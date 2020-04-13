#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import *
from tkinter import messagebox

#def
a = []
with open("new_to_do_list.json","w") as file:
                    file.write('')
def click_order():
    with open("new_to_do_list.json","w") as file:
                    file.write(str(a))
    messagebox.showinfo( 'Success', 'Задания отправлены')
    text.delete(1.0,'end')
def click_add():
    if (task.get() == '') or (category.get() == '') or (time.get() == '') :
        messagebox.showerror( 'Warning', 'Заполните все поля')
    else:
        name = task.get()
        cat = category.get()
        deadline = time.get()
        a.append({"Задача": name,"Категория": cat, "Дата": deadline})
        task.delete(0,'end')
        category.delete(0,'end')
        time.delete(0,'end')
        messagebox.showinfo( 'Success', 'Задания добавлены')

def out():
    text.delete(1.0,'end')
    text.insert(1.0, str(a).replace('[','').replace(']','').replace('{','').replace('}','').replace('\'','')
            )
#window    
window = Tk()
window.title("Менеджер задач")
window.geometry('640x480')
window.resizable( width = False, height = False )
window[ 'bg' ] = '#ccc'
window.iconbitmap( 'ico.ico' )
#frame

frame_bottom = Frame(window, bg = '#ccc')
frame_right = Frame(window,bg = '#ccc')
frame_left = Frame(window,bg = '#ccc')
frame1 =  Frame(frame_left,bg = '#ccc')
frame2 =  Frame(frame_left,bg = '#ccc')
frame3 =  Frame(frame_left,bg = '#ccc')
frame4 = Frame(frame_bottom,bg = '#ccc',width = '10')

#event
text_task = Label( frame1, text = 'Задача', font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc',
                 width = '8' 
               )

task = Entry( frame1, font = 'Consolas 15',
             fg = '#eff5c9',
             bg = '#48494f',
             relief = 'solid',
             justify = 'left')

text_category = Label(frame2, text = 'Категория', font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc',
                     width = '8' )

category = Entry( frame2, font = 'Consolas 15',
             fg = '#eff5c9',
             bg = '#48494f',
             relief = 'solid',
             justify = 'left')

text_time = Label( frame3,text = 'Время', font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc',
                 width = '8' )

time = Entry( frame3, font = 'Consolas 15',
             fg = '#eff5c9',
             bg = '#48494f',
             relief = 'solid',
             justify = 'left')

button_order = Button(frame4, text = 'Заказать', font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73',
                     width = '10',
                     command = click_order)
button_order_add = Button(frame4, text = 'Добавить', font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73',
                     width = '10',
                         command = click_add)
button_task_list = Button(frame_bottom, text = 'Список задач', font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73',
                     width = '22',
                         command = out)
button_exit = Button(frame_bottom,text = 'Выход', font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73',
                     width = '22',
                    command = window.destroy)

label_out = Label(frame_right, bg = '#ccc',
                 justify = 'center',
                 height = '10',
                 width = '15')
text = Text(label_out, bg = 'white',
           width = '32',
           height = '10',
           wrap = 'word',
            fg = 'black',
             relief = 'solid',
           font = 'Comfortaa 10'
             
          )
#pack

frame_bottom.pack(side = 'bottom')
frame_right.pack(fill = 'both',expand = True, side = 'right')
label_out.pack(fill = 'x',expand = True)
frame_left.pack(side = 'left')
frame1.pack(fill = 'both', expand = True)
frame2.pack(fill = 'both', expand = True)
frame3.pack(fill = 'both', expand = True)
text_task.pack(side = 'left', padx = 5 , pady = 5)
task.pack(fill = 'x',expand = True, padx = 10 , pady = 5)
text_category.pack(side = 'left', padx = 5 , pady = 5)
category.pack(fill = 'x',expand = True, padx = 10 , pady = 5)
text_time.pack(side = 'left', padx = 5 , pady = 5)
time.pack(fill = 'x',expand = True, padx = 10 , pady = 5)

button_order.pack(side = 'right',padx = 5,pady = 10)
button_order_add.pack(side = 'left',padx = 5, pady = 10)
button_exit.pack(side = 'bottom',pady = 10)
button_task_list.pack(side = 'bottom',pady = 10)

frame4.pack(side = 'bottom')

text.pack()

window.mainloop()


# In[ ]:




