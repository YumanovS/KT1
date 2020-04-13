#!/usr/bin/env python
# coding: utf-8

# In[31]:


from tkinter import *
from tkinter import messagebox
a = []
with open("new_to_do_list.json","w") as file:
                    file.write('')
def click_order():
    with open("new_to_do_list.json","w") as file:
                    file.write(str(a))
    messagebox.showinfo( 'Success', 'Задания отправлены')
def click_add():
    if (task.get() == '') or (category.get() == '') or (time.get() == '') :
        messagebox.showerror( 'Warning', 'Заполните все поля')
    else:
        name = task.get()
        cat = category.get()
        deadline = time.get()
        a.append({"category": cat, "name": name, "time": deadline})
        task.delete(0,'end')
        category.delete(0,'end')
        time.delete(0,'end')
        messagebox.showinfo( 'Success', 'Задания добавлены')
        
    
    
def out():
    print(str(a))
#window    
window = Tk()
window.title("Менеджер задач")
window.geometry('640x480')
window.resizable( width = False, height = False )
window[ 'bg' ] = '#ccc'
window.iconbitmap( 'ico.ico' )
#frame

frame1 =  Frame(window,bg = '#ccc')
frame2 =  Frame(window,bg = '#ccc')
frame3 =  Frame(window,bg = '#ccc')
frame4 = Frame(window,bg = '#ccc',width = '10')

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
button_task_list = Button( text = 'Список задач', font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73',
                     width = '22',
                         command = out)
button_exit = Button( text = 'Выход', font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73',
                     width = '22',
                    command = window.destroy)



#pack
frame1.pack(fill = 'both', expand = True)
frame2.pack(fill = 'both', expand = True)
frame3.pack(fill = 'both', expand = True)
text_task.pack(side = 'left', padx = 5 , pady = 5)
task.pack(fill = 'x',expand = True, padx = 10 , pady = 5)
text_category.pack(side = 'left', padx = 5 , pady = 5)
category.pack(fill = 'x',expand = True, padx = 10 , pady = 5)
text_time.pack(side = 'left', padx = 5 , pady = 5)
time.pack(fill = 'x',expand = True, padx = 10 , pady = 5)
frame4.pack(side = 'top')
button_order.pack(side = 'right',padx = 5,pady = 10)
button_order_add.pack(side = 'left',padx = 5, pady = 10)
button_task_list.pack(pady = 10)
button_exit.pack(pady = 10)

window.mainloop()


# In[ ]:




