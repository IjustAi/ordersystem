from os import name
from random import sample
import random
import tkinter as tk
import time
from tkinter.constants import BOTTOM
from turtle import update
from typing import Final


def show_frame(frame):
    frame.tkraise()
window = tk.Tk()
window.geometry('550x650')
window.title('Cafe Kiosk')

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
# frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window)
frame6 = tk.Frame(window) #payment system
frame7= tk.Frame(window)  # recomend menu
frame8 = tk.Frame(window) 
frame9 = tk.Frame(window) 
frame10 = tk.Frame(window)

for frame in (frame1, frame2,frame4,frame5,frame6,frame7,frame8, frame9, frame10):
    frame.grid(row=0, column=0, sticky='nsew')
my_order = {}
temp_order = {}
number_order = 1
# Command for updating view order
def updating_view ():
    frame_2_textbox.delete(1.0,tk.END)
    frame_10_textbox.delete(1.0,tk.END)
    for i in my_order.keys():
        if my_order[i]["Type"] == "Drinks":
            Order_text = i +": "+"Temperature: "+ str(my_order[i]["Temperature"])+" Size: "+str(my_order[i]["Size"])+" Quantity: "+str(my_order[i]["Quantity"])+" Price:"+str(my_order[i]["F_Price"])
            frame_2_textbox.insert(tk.END,Order_text)
            frame_2_textbox.insert(tk.END,"\n")
            frame_10_textbox.insert(tk.END,Order_text)
            frame_10_textbox.insert(tk.END,"\n")
        elif my_order[i]["Type"] == "Food":
            Order_text = i +": "+"Size: "+str(my_order[i]["Size"])+" Quantity: "+str(my_order[i]["Quantity"])+" Price:"+str(my_order[i]["F_Price"])
            frame_2_textbox.insert(tk.END,Order_text)
            frame_2_textbox.insert(tk.END,"\n")
            frame_10_textbox.insert(tk.END,Order_text)
            frame_10_textbox.insert(tk.END,"\n")
#Ordering
def ordering (name,types,s_prices,l_prices):
    Order_Choice = {name:{"Type":types,"Size":"S","Quantity":1,"Price":s_prices}}
    temp_order.update(Order_Choice)
    window.withdraw()
    order_menu = tk.Toplevel()
    order_menu.geometry('550x650')
    order_menu.title('Cafe Kiosk')
    price_insert_total = temp_order[name]["Price"]*temp_order[name]["Quantity"]
    Final_Price = "¥"+str(price_insert_total)
    def update_order_price():
        Price_Text.delete('1.0',tk.END)
        price_insert_new = temp_order[name]["Price"]*temp_order[name]["Quantity"]
        Price_Text.insert(tk.END,"¥"+str(price_insert_new))
    def change_value(Variable,Value,C_price):
        temp_order[name][Variable] = Value
        temp_order[name]["Price"] = C_price
        update_order_price()
    def submitting_quantity(value_quantity):
        try:
            Option3_Message.config(text="")
            int(value_quantity)
            temp_order[name]["Quantity"] = int(value_quantity)
            update_order_price()
        except ValueError:
            Option3_Message.config(text="Please Enter a Number")
    def Cancel():
        temp_order.clear()
        window.deiconify()
        order_menu.destroy()
    def Confirm():
        global number_order
        Final_Price_Dic = {"F_Price":(temp_order[name]["Price"]*temp_order[name]["Quantity"])}
        temp_order[name].update(Final_Price_Dic)
        if name in my_order:
            if temp_order[name]["Type"] == "Drinks":
                if (my_order[name]["Size"] == temp_order[name]["Size"]) and (my_order[name]["Temperature"] == temp_order[name]["Temperature"]):
                    my_order[name]["Quantity"] = my_order[name]["Quantity"]+temp_order[name]["Quantity"]
                    my_order[name]["F_Price"] = my_order[name]["F_Price"]+temp_order[name]["F_Price"]
                else:
                    temp_order[name+"("+str(number_order)+")"] = temp_order.pop(name)
                    my_order.update(temp_order)
                    number_order += 1
            elif temp_order[name]["Type"] == "Food":
                if (my_order[name]["Size"] == temp_order[name]["Size"]):
                    my_order[name]["Quantity"] = my_order[name]["Quantity"]+temp_order[name]["Quantity"]
                    my_order[name]["F_Price"] = my_order[name]["F_Price"]+temp_order[name]["F_Price"]
                elif my_order[name].items() != temp_order[name].items():
                    temp_order[name+"("+str(number_order)+")"] = temp_order.pop(name)
                    my_order.update(temp_order)
                    number_order += 1
        else:
            my_order.update(temp_order)
        temp_order.clear()
        updating_view()
        window.deiconify()
        order_menu.destroy()
        
    if types == "Drinks":
        Order_menu_title = tk.Label(order_menu, text=name+': choose size and quantity ', font='times 20')
        Order_menu_title.pack(fill='both', side='top')
        background= tk.PhotoImage(file='background.png')
        label=tk.Label(order_menu,image=background)
        label.pack(fill='both')
        label.image=background
        Option1_Frame = tk.Frame(order_menu)
        Option1_Frame.pack(side="top",anchor="w")
        Option1_Label = tk.Label(Option1_Frame,text="Temperature")
        Option1_Label.pack(anchor="w",side="top")
        option_1_added = {"Temperature":"Hot"}
        temp_order[name].update(option_1_added)
        def change_temp(value):
            option_1_added = {"Temperature":value}
            temp_order[name].update(option_1_added)
        
        temperature = tk.StringVar()
        temperature.set("Hot")
        Option1_1 = tk.Radiobutton(Option1_Frame, text="Hot",variable=temperature,value="Hot",command=lambda: change_temp(temperature.get())).pack(side="left")
        Option1_2 = tk.Radiobutton(Option1_Frame, text = "Ice",variable=temperature,value="Ice",command=lambda: change_temp(temperature.get())).pack(side="left")
        Option2_Frame = tk.Frame(order_menu)
        Option2_Frame.pack(side="top",anchor="w")
        Option2_Label = tk.Label(Option2_Frame,text="Size")
        Option2_Label.pack(anchor="w",side="top")
        Size = tk.StringVar()
        Size.set("S")

        Option2_1 = tk.Radiobutton(Option2_Frame, text="Small",variable=Size,value="S",command=lambda: change_value("Size",Size.get(),s_prices)).pack(side="left")
        Option2_2 = tk.Radiobutton(Option2_Frame, text = "Large",variable=Size,value="L",command=lambda: change_value("Size",Size.get(),l_prices)).pack(side="left")
        Option3_Frame = tk.Frame(order_menu)
        Option3_Frame.pack(side="top",anchor="w")
        Option3_Label = tk.Label(Option3_Frame,text="Quantity")
        Option3_Label.pack(anchor="w",side="top")
        Option3_Entry = tk.Entry(Option3_Frame)
        Option3_Entry.insert(tk.END,1)
        Option3_Entry.pack(side="left",padx=5)
        Option3_Button = tk.Button(Option3_Frame,text="Submit",command=lambda:submitting_quantity(Option3_Entry.get()))
        Option3_Button.pack(side="left")
        Option3_Message = tk.Label(Option3_Frame,text = "")
        Option3_Message.pack(side="left")
        Price_Frame = tk.Frame(order_menu)
        Price_Frame.pack(side="top",anchor="e")
        Price_Text = tk.Text(Price_Frame,width=10,height=1)
        Price_Text.insert(tk.END,Final_Price)
        Price_Text.pack(side="right")
        Price_Label = tk.Label(Price_Frame,text= "Price")
        Price_Label.pack(side="right")
        Last_Frame = tk.Frame(order_menu)
        Last_Frame.pack(side="bottom",anchor="e",padx=5,pady=5)
        Order_Cancel_Button = tk.Button(Last_Frame,text="Cancel",command=lambda:Cancel())
        Order_Cancel_Button.pack(side="right")
        Order_Confirm_Button = tk.Button(Last_Frame,text="Confirm",command=lambda:Confirm())
        Order_Confirm_Button.pack(side="right")
        
       
       
    elif types == "Food":
        Order_menu_title = tk.Label(order_menu, text=name+': choose size and quantity ', font='times 20')
        Order_menu_title.pack(fill='both', side='top')
        background= tk.PhotoImage(file='background.png')
        label=tk.Label(order_menu,image=background)
        label.pack(fill='both')
        label.image=background
        Option2_Frame = tk.Frame(order_menu)
        Option2_Frame.pack(side="top",anchor="w")
        Option2_Label = tk.Label(Option2_Frame,text="Size")
        Option2_Label.pack(anchor="w",side="top")
        Size = tk.StringVar()
        Size.set("S")

        Option2_1 = tk.Radiobutton(Option2_Frame, text="Small",variable=Size,value="S",command=lambda: change_value("Size",Size.get(),s_prices)).pack(side="left")
        Option2_2 = tk.Radiobutton(Option2_Frame, text = "Large",variable=Size,value="L",command=lambda: change_value("Size",Size.get(),l_prices)).pack(side="left")
        Option3_Frame = tk.Frame(order_menu)
        Option3_Frame.pack(side="top",anchor="w")
        Option3_Label = tk.Label(Option3_Frame,text="Quantity")
        Option3_Label.pack(anchor="w",side="top")
        Option3_Entry = tk.Entry(Option3_Frame)
        Option3_Entry.insert(tk.END,1)
        Option3_Entry.pack(side="left",padx=5)
        Option3_Button = tk.Button(Option3_Frame,text="Submit",command=lambda:submitting_quantity(Option3_Entry.get()))
        Option3_Button.pack(side="left")
        Option3_Message = tk.Label(Option3_Frame,text = "")
        Option3_Message.pack(side="left")
        Price_Frame = tk.Frame(order_menu)
        Price_Frame.pack(side="top",anchor="e")
        Price_Text = tk.Text(Price_Frame,width=10,height=1)
        Price_Text.insert(tk.END,Final_Price)
        Price_Text.pack(side="right")
        Price_Label = tk.Label(Price_Frame,text= "Price")
        Price_Label.pack(side="right")
        Last_Frame = tk.Frame(order_menu)
        Last_Frame.pack(side="bottom",anchor="e",padx=5,pady=5)
        Order_Cancel_Button = tk.Button(Last_Frame,text="Cancel",command=lambda:Cancel())
        Order_Cancel_Button.pack(side="right")
        Order_Confirm_Button = tk.Button(Last_Frame,text="Confirm",command=lambda:Confirm())
        Order_Confirm_Button.pack(side="right")

#Canceling Order
def cancelling_orders():
    cancel_window = tk.Toplevel(window)
   
    for i in my_order.keys():
        tk.Button(cancel_window,text="cancel "+str(i),command= lambda i=i: [deleting_orders(i),closing_cancel_window()]).pack()
   
    def closing_cancel_window(): 
        cancel_window.destroy()
def deleting_orders(j):
    del my_order[j]
    updating_view()
#Clear Orders
def clear_all():
    my_order.clear()
    updating_view()


# Frame7 code(recommended menu)

frame7_title = tk.Label(frame7,text="Here is today's Recommended Menu",font='times 20')
frame7_title.pack(fill='x',side='top')

food_list=['Café Latte','Espresso','Americano','Cappuccino','Café Mocha','Lemon Soda','Peach Soda','Apple Juice',
                'Orange Juice','Plain Bagel','Blueberry Bagel','Plain Waffle','Ham Sandwich','Pound Cake',
                'Strawberry Shortcake','Red Velvet ', 'Tiramisu','Chocolate Cake']

Order_Menu={'Café Latte':{"Type":"Drinks","P1":250,"P2":400},
            'Espresso':{"Type":"Drinks","P1":200,"P2":380},
            'Americano':{"Type":"Drinks","P1":200,"P2":380},
            'Cappuccino':{"Type":"Drinks","P1":200,"P2":400},
            'Café Mocha':{"Type":"Drinks","P1":300,"P2":500},
            'Lemon Soda':{"Type":"Drinks","P1":250,"P2":450},
            'Peach Soda':{"Type":"Drinks","P1":250,"P2":450},
            'Apple Juice':{"Type":"Drinks","P1":200,"P2":300},
            'Orange Juice':{"Type":"Drinks","P1":200,"P2":300},
            'Plain Bagel':{"Type":"Food","P1":400,"P2":600},
            'Blueberry Bagel':{"Type":"Food","P1":500,"P2":700},
            'Plain Waffle':{"Type":"Food","P1":400,"P2":700},
            'Ham Sandwich':{"Type":"Food","P1":400,"P2":600},
            'Pound Cake':{"Type":"Food","P1":300,"P2":500},
            'Strawberry shortcake':{"Type":"Food","P1":650,"P2":850},
            'Red Velvet':{"Type":"Food","P1":700,"P2":900},
            'Tiramisu':{"Type":"Food","P1":800,"P2":1000},
            'Chocolate Cake':{"Type":"Food","P1":500,"P2":700}}

j=sample(food_list,1) #avoid the repeat
Strj = "".join(j)
food_list.remove(Strj)
y=sample(food_list,1)
Stry="".join(y)
frame7_btn3=tk.Button(frame7,text='Next',command=lambda:show_frame(frame2))
frame7_btn3.pack(fill='x', side='bottom')
frame7_btn = tk.Button(frame7, text=Strj, command=lambda: ordering(Strj,Order_Menu[Strj]["Type"],Order_Menu[Strj]["P1"],Order_Menu[Strj]["P2"]))
frame7_btn.pack()
frame7_btn.place(x=365,y=200)
frame7_btn2 = tk.Button(frame7, text=Stry, command=lambda: ordering(Stry,Order_Menu[Stry]["Type"],Order_Menu[Stry]["P1"],Order_Menu[Stry]["P2"]))
frame7_btn2.pack()
frame7_btn2.place(x=100,y=200)
photo8 = tk.PhotoImage(file="coffee.png")
imgLabel8 = tk.Label(frame7, image=photo8)
imgLabel8.pack()  # 自动对齐
imgLabel8.place(x=90,y=50)
photo17 = tk.PhotoImage(file="coffee.png")
imgLabel17 = tk.Label(frame7, image=photo17)
imgLabel17.pack()
imgLabel17.place(x=360,y=50)
background= tk.PhotoImage(file='background.png')
label=tk.Label(frame7,image=background)
label.pack(side='bottom')
label.image=background

# ==================Frame 1 code
frame1_title = tk.Label(frame1, text='Welcome to Cafe Kiosk.', font='times 20')
frame1_title.pack(fill='x',side='top')
frame1_btn = tk.Button(frame1, text='Take out', command=lambda: show_frame(frame7))
frame1_btn.pack(fill='x', side='bottom')
frame1_btn2 = tk.Button(frame1,text='Dine in',command=lambda:show_frame(frame7))
frame1_btn2.pack(fill='x',side='bottom')
background= tk.PhotoImage(file='background.png')
label=tk.Label(frame1,image=background)
label.pack(fill='both')
label.image=background

# ==================Frame 2 code

        

frame2_title = tk.Label(frame2, text=' Drink Menu', font='times 20')
frame2_title.pack(fill='x', side='top')
frame2_btn = tk.Button(frame2, text='Café Latte', command=lambda: [ordering("Café Latte","Drinks",250,400)])
frame2_btn.pack()
frame2_btn.place(x=230,y=160)
frame2_btn2=tk.Button(frame2,text='Espresso',command=lambda:[ordering("Espresso","Drinks",200,380)])
frame2_btn2.pack()
frame2_btn2.place(x=58,y=160)
frame2_btn = tk.Button(frame2, text='Americano', command=lambda: [ordering("Americano","Drinks",200,380)])
frame2_btn.pack()
frame2_btn.place(x=410,y=160)
frame2_btn2=tk.Button(frame2,text='Cappuccino',command=lambda:[ordering("Cappuccino","Drinks",250,400)])
frame2_btn2.pack()
frame2_btn2.place(x=50,y=310)
frame2_btn2=tk.Button(frame2,text='Café Mocha',command=lambda:[ordering("Café Mocha","Drinks",300,500)])
frame2_btn2.pack()
frame2_btn2.place(x=225,y=310)
frame2_btn2=tk.Button(frame2,text='Peach Soda',command=lambda:[ordering("Peach Soda","Drinks",250,450)])
frame2_btn2.pack()
frame2_btn2.place(x=410,y=310)
frame2_btn2=tk.Button(frame2,text='Lemon Soda',command=lambda:[ordering("Lemon Soda","Drinks",250,450)])
frame2_btn2.pack()
frame2_btn2.place(x=47,y=460)
frame2_btn2=tk.Button(frame2,text='Apple Juice',command=lambda:[ordering("Apple Juice","Drinks",200,300)])
frame2_btn2.pack()
frame2_btn2.place(x=225,y=460)
frame2_btn2=tk.Button(frame2,text='Orange Juice',command=lambda:[ordering("Orange Juice","Drinks",200,300)])
frame2_btn2.pack()
frame2_btn2.place(x=405,y=460)


photo = tk.PhotoImage(file="coffee.png")
imgLabel = tk.Label(frame2, image=photo)
imgLabel.pack()
imgLabel.place(x=35,y=50)
imgLabel1 = tk.Label(frame2, image=photo)
imgLabel1.pack()
imgLabel1.place(x=210,y=50)
imgLabel2 = tk.Label(frame2, image=photo)
imgLabel2.pack()
imgLabel2.place(x=395,y=50)
imgLabel3 = tk.Label(frame2, image=photo)
imgLabel3.pack()
imgLabel3.place(x=35,y=200)
imgLabel4 = tk.Label(frame2, image=photo)
imgLabel4.pack()
imgLabel4.place(x=210,y=200)
imgLabel5= tk.Label(frame2, image=photo)
imgLabel5.pack()
imgLabel5.place(x=395,y=200)
imgLabel6 = tk.Label(frame2, image=photo)
imgLabel6.pack()  # 自动对齐
imgLabel6.place(x=35,y=350)
imgLabel7 = tk.Label(frame2, image=photo)
imgLabel7.pack()
imgLabel7.place(x=210,y=350)
imgLabel8 = tk.Label(frame2, image=photo)
imgLabel8.pack()
imgLabel8.place(x=395,y=350)

#Frame for bottom commands
frame2_bottom_frame = tk.Frame(frame2)
frame2_bottom_frame.pack(side="bottom",anchor="e",padx=30,pady=5)
frame2_btn_np=tk.Button(frame2_bottom_frame,text='Next Page',command=lambda:show_frame(frame10))
frame2_btn_np.pack(fill='x', side='right')
frame2_btn_GC=tk.Button(frame2_bottom_frame,text='Go To Check Out',command=lambda:show_frame(frame4))
frame2_btn_GC.pack(fill='x', side='right')
frame2_btn_CL=tk.Button(frame2_bottom_frame,text='Clear all',command=lambda:clear_all())
frame2_btn_CL.pack(fill='x', side='right')
frame2_btn_CO=tk.Button(frame2_bottom_frame,text='Cancel Order',command=lambda:cancelling_orders())
frame2_btn_CO.pack(fill='x', side='right')
#Displaying Orders
frame2_2 = tk.Frame(frame2)
frame2_2.pack(side="bottom")
frame2_2_Label = tk.Label(frame2_2,text="My Order")
frame2_2_Label.pack(anchor="w")
frame_2_Messagescroll = tk.Scrollbar(frame2_2)
frame_2_Messagescroll.pack(side="right",fill="y")
frame_2_textbox = tk.Text(frame2_2,height=6,width=70,yscrollcommand=frame_2_Messagescroll.set)
frame_2_textbox.pack(side="left",fill="x")
frame_2_Messagescroll.config(command=frame_2_textbox.yview)



#Frame 10 food menu
frame10_title = tk.Label(frame10, text=' Food Menu', font='times 20')
frame10_title.pack(fill='x', side='top')
frame10_btn = tk.Button(frame10, text='Plain Bagel', command=lambda: [ordering("Plain bagel","Food",400,600)])
frame10_btn.pack()
frame10_btn.place(x=230,y=160)
frame10_btn2=tk.Button(frame10,text='Blueberry Bagel',command=lambda:[ordering("Blueberry Bagel","Food",500,700)])
frame10_btn2.pack()
frame10_btn2.place(x=42,y=160)
frame10_btn = tk.Button(frame10, text='Tiramisu', command=lambda: [ordering("Tiramisu","Food",800,1000)])
frame10_btn.pack()
frame10_btn.place(x=418,y=160)
frame10_btn2=tk.Button(frame10,text='Plain Waffle',command=lambda:[ordering("Plain Waffle","Food",400,700)])
frame10_btn2.pack()
frame10_btn2.place(x=48,y=310)
frame10_btn2=tk.Button(frame10,text='Ham Sandwich',command=lambda:[ordering("Ham Sandwich","Food",400,600)])
frame10_btn2.pack()
frame10_btn2.place(x=213,y=310)
frame10_btn2=tk.Button(frame10,text='Pound Cake',command=lambda:[ordering("Pound Cake","Food",300,500)])
frame10_btn2.pack()
frame10_btn2.place(x=410,y=310)
frame10_btn2=tk.Button(frame10,text='Red Velvet',command=lambda:[ordering("Red Velvet","Food",700,900)])
frame10_btn2.pack()
frame10_btn2.place(x=55,y=460)
frame10_btn2=tk.Button(frame10,text='Strawberry Shortcake',command=lambda:[ordering("Strawberry Shortcake","Food",650,850)])
frame10_btn2.pack()
frame10_btn2.place(x=200,y=460)
frame10_btn2=tk.Button(frame10,text='Chocolate Cake',command=lambda:[ordering("Chocolate Cake","Food",500,700)])
frame10_btn2.pack()
frame10_btn2.place(x=400,y=460)


photo1 = tk.PhotoImage(file="cake.png")


imgLabel = tk.Label(frame10, image=photo1)
imgLabel.pack()
imgLabel.place(x=35,y=50)
imgLabel1 = tk.Label(frame10, image=photo1)
imgLabel1.pack()
imgLabel1.place(x=210,y=50)
imgLabel2 = tk.Label(frame10, image=photo1)
imgLabel2.pack()
imgLabel2.place(x=395,y=50)
imgLabel3 = tk.Label(frame10, image=photo1)
imgLabel3.pack()
imgLabel3.place(x=35,y=200)
imgLabel4 = tk.Label(frame10, image=photo1)
imgLabel4.pack()
imgLabel4.place(x=210,y=200)
imgLabel5= tk.Label(frame10, image=photo1)
imgLabel5.pack()
imgLabel5.place(x=395,y=200)
imgLabel6 = tk.Label(frame10, image=photo1)
imgLabel6.pack()  # 自动对齐
imgLabel6.place(x=35,y=350)
imgLabel7 = tk.Label(frame10, image=photo1)
imgLabel7.pack()
imgLabel7.place(x=210,y=350)
imgLabel8 = tk.Label(frame10, image=photo1)
imgLabel8.pack()
imgLabel8.place(x=395,y=350)
#Frame for bottom commands
frame10_bottom_frame = tk.Frame(frame10)
frame10_bottom_frame.pack(side="bottom",anchor="e",padx=30,pady=5)
frame10_btn_pp=tk.Button(frame10_bottom_frame,text='Previous page',command=lambda:show_frame(frame2))
frame10_btn_pp.pack(fill='x', side='right')
frame10_btn_GC=tk.Button(frame10_bottom_frame,text='Go To Check Out',command=lambda:show_frame(frame4))
frame10_btn_GC.pack(fill='x', side='right')
frame10_btn_CL=tk.Button(frame10_bottom_frame,text='Clear all',command=lambda:clear_all())
frame10_btn_CL.pack(fill='x', side='right')
frame10_btn_CO=tk.Button(frame10_bottom_frame,text='Cancel Order',command=lambda:cancelling_orders())
frame10_btn_CO.pack(fill='x', side='right')
#Displaying Orders
frame10_2 = tk.Frame(frame10)
frame10_2.pack(side="bottom")
frame10_2_Label = tk.Label(frame10_2,text="My Order")
frame10_2_Label.pack(anchor="w")
frame_10_Messagescroll = tk.Scrollbar(frame10_2)
frame_10_Messagescroll.pack(side="right",fill="y")
frame_10_textbox = tk.Text(frame10_2,height=6,width=70,yscrollcommand=frame_10_Messagescroll.set)
frame_10_textbox.pack(side="left",fill="x")
frame_10_Messagescroll.config(command=frame_10_textbox.yview)




#Frame 4 code
frame4_title = tk.Label(frame4, text='Would you like to see our seasonal limited menu?', font='times 20')
frame4_title.pack(fill='both', side='top')
frame4_btn=tk.Button(frame4,text='No',command=lambda:show_frame(frame6))
frame4_btn.pack(fill='x',side='bottom')
frame4_btn2 = tk.Button(frame4,text='Yes',command=lambda:show_frame(frame5))
frame4_btn2.pack(fill='x',side='bottom')
background2= tk.PhotoImage(file='season.png')
label00=tk.Label(frame4,image=background2)
label00.pack(fill='both')
label00.image=background2

# Frame 5 code which is limited menu
timeInfo = time.localtime(time.time())
if(timeInfo[1] == 12 or timeInfo[1] == 1 or timeInfo[1] == 2):
    frame5_title = tk.Label(frame5, text='Winter Limited Menu', font='times 20')
    frame5_title.pack(fill='x', side='top')
    frame5_btn = tk.Button(frame5, text='Ginger Tea', command=lambda: ordering("Ginger Tea","Food",200,400))
    frame5_btn.pack()
    frame5_btn.place(x=400, y=160)
    frame5_btn2 = tk.Button(frame5, text='Strawberry Hot Chocolate', command=lambda: ordering("Strawberry Hot Chocolate","Food",550,650))
    frame5_btn2.pack()
    frame5_btn2.place(x=20, y=160)
    frame5_bottom_frame = tk.Frame(frame5)
    frame5_bottom_frame.pack(side="bottom",anchor="e",padx=70)
    frame5_btn3 = tk.Button(frame5_bottom_frame, text='Go to check out ', command=lambda: show_frame(frame6))
    frame5_btn3.pack(side="right")
    frame5_btn4 = tk.Button(frame5_bottom_frame, text='Previous Page ', command=lambda: show_frame(frame10))
    frame5_btn4.pack(side="right")
    imgLabel3 = tk.Label(frame5, image=photo)
    imgLabel3.pack()  # 自动对齐
    imgLabel3.place(x=50, y=50)

    imgLabel4 = tk.Label(frame5, image=photo)
    imgLabel4.pack()
    imgLabel4.place(x=380, y=50)
    background = tk.PhotoImage(file='background.png')
    label = tk.Label(frame5, image=background)
    label.pack(side='bottom')
    label.image = background
elif(timeInfo[1]==3or timeInfo[1]==4 or timeInfo[1]==5):
    frame5_title = tk.Label(frame5, text='Spring Limited Menu', font='times 20')
    frame5_title.pack(fill='x', side='top')
    frame5_btn = tk.Button(frame5, text='Strawberry waffle 450/750¥', command=lambda: ordering("Strawberry waffle","Food",450,750))
    frame5_btn.pack()
    frame5_btn.place(x=400, y=150)
    frame5_btn2 = tk.Button(frame5, text='Strawberry juice 240/340¥', command=lambda: ordering("Strawberry juice","Food",240,340))
    frame5_btn2.pack()
    frame5_btn2.place(x=60, y=150)
    frame5_btn3 = tk.Button(frame5, text='Go to check out ', command=lambda: show_frame(frame6))
    frame5_btn3.pack(fill='x', side='bottom')
    frame5_bottom_frame = tk.Frame(frame5)
    frame5_bottom_frame.pack(side="bottom",anchor="e",padx=70)
    frame5_btn3 = tk.Button(frame5_bottom_frame, text='Go to check out ', command=lambda: show_frame(frame6))
    frame5_btn3.pack(side="right")
    frame5_btn4 = tk.Button(frame5_bottom_frame, text='Previous Page ', command=lambda: show_frame(frame10))
    frame5_btn4.pack(side="right")

    imgLabel3 = tk.Label(frame5, image=photo)
    imgLabel3.pack()  #
    imgLabel3.place(x=50, y=50)

    photo4 = tk.PhotoImage(file="b.png")
    imgLabel4 = tk.Label(frame5, image=photo)
    imgLabel4.pack()
    imgLabel4.place(x=380, y=50)
    background = tk.PhotoImage(file='background.png')
    label = tk.Label(frame5, image=background)
    label.pack(side='bottom')
    label.image = background
elif(timeInfo[1]==6or timeInfo[1]==7or timeInfo[1]==8):
    frame5_title = tk.Label(frame5, text='Summer Limited Menu', font='times 20')
    frame5_title.pack(fill='x', side='top')
    frame5_btn = tk.Button(frame5, text='Mango juice 240/340¥', command=lambda: ordering("Mango juice","Food",240,340))
    frame5_btn.pack()
    frame5_btn.place(x=400, y=150)
    frame5_btn2 = tk.Button(frame5, text='Peach Sandwich 430/730¥', command=lambda: ordering("Peach Sandwich","Food",430,730))
    frame5_btn2.pack()
    frame5_btn2.place(x=60, y=150)
    frame5_btn3 = tk.Button(frame5, text='Go to check out', command=lambda: show_frame(frame6))
    frame5_btn3.pack(fill='x', side='bottom')
    frame5_bottom_frame = tk.Frame(frame5)
    frame5_bottom_frame.pack(side="bottom",anchor="e",padx=70)
    frame5_btn3 = tk.Button(frame5_bottom_frame, text='Go to check out ', command=lambda: show_frame(frame6))
    frame5_btn3.pack(side="right")
    frame5_btn4 = tk.Button(frame5_bottom_frame, text='Previous Page ', command=lambda: show_frame(frame10))
    frame5_btn4.pack(side="right")
    imgLabel3 = tk.Label(frame5, image=photo)
    imgLabel3.pack()  # 自动对齐
    imgLabel3.place(x=50, y=50)

    imgLabel4 = tk.Label(frame5, image=photo)
    imgLabel4.pack()
    imgLabel4.place(x=380, y=50)
    background = tk.PhotoImage(file='background.png')
    label = tk.Label(frame5, image=background)
    label.pack(side='bottom')
    label.image = background
else:
    frame5_title = tk.Label(frame5, text='Fall Limited Menu', font='times 20')
    frame5_title.pack(fill='x', side='top')
    frame5_btn = tk.Button(frame5, text=' Chestnut Praline Drink 350/500¥', command=lambda: ordering("Chestnut Praline Drink","Food",350,500))
    frame5_btn.pack()
    frame5_btn.place(x=400, y=150)
    frame5_btn2 = tk.Button(frame5, text='Fig Sandwich 200/350¥', command=lambda: ordering("Strawberry juice","Food",200,350))
    frame5_btn2.pack()
    frame5_btn2.place(x=60, y=150)
    frame5_btn3 = tk.Button(frame5, text='Go to check out ', command=lambda: show_frame(frame6))
    frame5_btn3.pack(fill='x', side='bottom')
    frame5_bottom_frame = tk.Frame(frame5)
    frame5_bottom_frame.pack(side="bottom",anchor="e",padx=70)
    frame5_btn3 = tk.Button(frame5_bottom_frame, text='Go to check out ', command=lambda: show_frame(frame6))
    frame5_btn3.pack(side="right")
    frame5_btn4 = tk.Button(frame5_bottom_frame, text='Previous Page ', command=lambda: show_frame(frame10))
    frame5_btn4.pack(side="right")
    imgLabel3 = tk.Label(frame5, image=photo)
    imgLabel3.pack()  # 自动对齐
    imgLabel3.place(x=50, y=50)

    imgLabel4 = tk.Label(frame5, image=photo)
    imgLabel4.pack()
    imgLabel4.place(x=380, y=50)
    background = tk.PhotoImage(file='background.png')
    label = tk.Label(frame5, image=background)
    label.pack(side='bottom')
    label.image = background





#frame 6 code: PAYMENT AND CHECKOUT

#Use Coupon


def using_coupon():
    Use_Coupon = tk.Toplevel()
    Use_Coupon.geometry("300x200")
    Use_Coupon_Frame1 = tk.Frame(Use_Coupon)
    Use_Coupon_Frame1.pack(side="top",padx=5)
    Use_Coupon_Label = tk.Label(Use_Coupon_Frame1,text = "Enter your Phone Number")
    Use_Coupon_Label.pack(side="top",anchor="w")
    Use_Coupon_Phone = tk.Entry(Use_Coupon_Frame1)
    Use_Coupon_Phone.pack(side="left")
    


    def submitting_coupon(PN):
        count = 0
        from Coupon import Coupons
        for i in Coupons:
            if PN in i:
                count += 1
                CN = Coupons.index(i)
        def deleting_Coupons():
            del Coupons[CN]
            with open (r"Coupon.py","w") as f:
                f.write("Coupons="+str(Coupons)) 
                
        if count >= 1:    
            if TP[0] > 0:   
                discount = TP[0]*((100-Coupons[CN][2])/100) 
                Use_Coupon_Label_2.config(text = "Thank you "+ str(Coupons[CN][0])+"! We found your "+ str(Coupons[CN][2])+"% coupon! \n With your coupon the new price is  ¥"+str(discount)+"!")
                Use_Coupon_Phone_Button4.pack_forget()  
                Use_Coupon_Phone_Button2.pack(side="left")
                Use_Coupon_Phone_Button2.config(command=lambda: [Use_Coupon.destroy(),show_frame(frame8),deleting_Coupons()])
                Use_Coupon_Phone_Button3.pack(side="left")
            else:
                Use_Coupon_Label_2.config(text = "Sorry, unable to make a discount.")
                Use_Coupon_Phone_Button3.pack_forget()
                Use_Coupon_Phone_Button2.pack_forget()
                Use_Coupon_Phone_Button4.pack()
            
                     
            Coupons[CN][0]
        elif count == 0:
            Use_Coupon_Label_2.config(text = "Sorry, can't find your coupon with this number.")
            
            Use_Coupon_Phone_Button3.pack_forget()
            Use_Coupon_Phone_Button2.pack_forget()
            Use_Coupon_Phone_Button4.pack()
            
            
    
    Use_Coupon_Phone_Button = tk.Button(Use_Coupon_Frame1,text="Submit",command=lambda: submitting_coupon(str(Use_Coupon_Phone.get())))
    Use_Coupon_Phone_Button.pack(side="left")
              
    Use_Coupon_Label_2 = tk.Label(Use_Coupon,text="")
    Use_Coupon_Label_2.pack(side="top")
    Use_Coupon_Frame2 = tk.Frame(Use_Coupon)
    Use_Coupon_Frame2.pack(side="bottom")
    
    Use_Coupon_Phone_Button2 = tk.Button(Use_Coupon_Frame2,text="Purchase")
    
    Use_Coupon_Phone_Button3 = tk.Button(Use_Coupon_Frame2,text="Cancel",command=lambda: Use_Coupon.destroy())
    Use_Coupon_Phone_Button4 = tk.Button(Use_Coupon_Frame2,text="Close",command=lambda: Use_Coupon.destroy())
    



frame6_title = tk.Label(frame6, text='Checkout', font='times 20')
frame6_title.pack(fill='both', side='top')
TP = [0]
def calculate():
    total=0
    for i in my_order.keys():
        total += my_order[i]["F_Price"]

    checkout = tk.Label(frame6,
                        text= 'Your total bill is ¥' +str(total),
                        font='times 19') 
    TP[0] = total
    checkout.place (x=183, y=150) #position of the bill label
    
    checkout.after(1000, checkout.destroy)

    window.after(1000, calculate)

window.after(1000, calculate)
frame_6_bottom = tk.Frame(frame6)
frame_6_bottom.pack(side="bottom")
frame_6_GB = tk.Button(frame_6_bottom,text="Go Back",command=lambda:show_frame(frame5))
frame_6_GB.pack(side="left")
frame_6_UC = tk.Button(frame_6_bottom,text="Use Coupon",command=lambda:using_coupon())
frame_6_UC.pack(side="left")
frame_6_P = tk.Button(frame_6_bottom,text="Purchase",command=lambda:show_frame(frame8))
frame_6_P.pack(side="left")




dic ={'Cafe Latte':{'S':300,'L':500},'Espresso':{'S':200,'L':500},'Americano':{'S':200,'L':500},
      'Cappuccino':{'S':200,'L':500},'Cafe Mocha':{'S':300,'L':500},'Lemon Soda':{'S':200,'L':500},
      'Peach Soda':{'S':300,'L':500},' Apple juice':{'S':300,'L':500},'Orange Juice' :{'S':200,'L':500},
      'Plain bagel':{'S':500,'L':700},'Blueberry  Bagel':{'S':500,'L':700},'Plain Waffle':{'S':500,'L':700},
      'Ham Sandwich':{'S':500,'L':700},'Pound Cake':{'S':300,'L':500},'Strawberry Shortcake':{'S':500,'L':700},
      'Red Velvet ':{'S':700,'L':900},'Tiramisu  ':{'S':800,'L':1000},'Chocolate Cake ':{'S':500,'L':700},
      'Strawberry Hot Chocolate':{'S':500,'L':800},'Ginger Tea':{'S':300,'L':500}}


#Frame 8 Code=========

frame8_title = tk.Label(frame8, text='Thank you for ordering here at Cafe Kiosk!\nClick the button below to get a coupon!', font='times 20')

frame8_title.pack(side='top')


frame8_btn = tk.Button(frame8,text="Go to Coupon Page",command=lambda:show_frame(frame9))
frame8_btn.pack()


#Frame 9 Code ======

mat = [[1,2,3],[4,5,6],[7,8,9]]

for i in range (len(mat)):
    for j in range (len(mat[0])):
        print(mat[i][j], end=' ')

    print()
    
a=random.randint(0,2)
b=random.randint(0,2)

def saving_coupons(amount):
    from Coupon import Coupons
    temp_Coupon = ["Name","PN",amount]
    def coupon_PN_search(PN):
        count = 0
        for i in Coupons:
            if PN in i:
                count += 1
        if count >= 1:
            save_coupon_f2.pack_forget()
            save_coupon_f4.pack_forget()
            save_coupon_l3.pack()
            save_coupon_l3.config(text="Sorry, only 1 coupon per phone contact is allowed.")
        elif count == 0:
            save_coupon_l3.pack_forget()
            temp_Coupon[1] = PN
            save_coupon_f2.pack(side="top",padx=5)

    def Coupon_name(C_H):
        temp_Coupon[0] = C_H
        save_coupon_f4.pack(side="bottom")
  
    def Overwrite_Coupon_Files():
        Coupons.append(temp_Coupon)
            
        with open (r"Coupon.py","w") as f:
            f.write("Coupons="+str(Coupons))
        save_coupon.destroy()
        window.destroy()
    save_coupon =tk.Toplevel()
    save_coupon.geometry("300x200")
    save_coupon_f1 = tk.Frame(save_coupon)
    save_coupon_f1.pack(side="top",padx=5)
    save_coupon_l1 = tk.Label(save_coupon_f1,text="Your Phone Number")
    save_coupon_l1.pack()
    save_coupon_e1 = tk.Entry(save_coupon_f1)
    save_coupon_e1.pack(side="left")
    save_coupon_b1 = tk.Button(save_coupon_f1,text="search",command=lambda: coupon_PN_search(str(save_coupon_e1.get())))
    save_coupon_b1.pack(side="left")

    save_coupon_f2 = tk.Frame(save_coupon)
    
    save_coupon_l2 = tk.Label(save_coupon_f2,text="Your Name")
    save_coupon_l2.pack()
    save_coupon_e2 = tk.Entry(save_coupon_f2)
    save_coupon_e2.pack(side="left")
    save_coupon_b2 = tk.Button(save_coupon_f2,text="save",command=lambda:Coupon_name(str(save_coupon_e2.get())))
    save_coupon_b2.pack(side="left")
    save_coupon_l3 = tk.Label(save_coupon,text="")
    
    
    save_coupon_f4 = tk.Frame(save_coupon)
    

    save_coupon_b4 = tk.Button(save_coupon_f4,text="save",command=lambda:Overwrite_Coupon_Files())
    save_coupon_b4.pack(side="left")
    
    save_coupon_b5 = tk.Button(save_coupon_f4,text="Cancel",command=lambda: save_coupon.destroy())
    save_coupon_b5.pack(side="left")

if(mat[a][b]%3==0):
    frame9_frame = tk.Frame(frame9)
    frame9_frame.pack(side="bottom",pady=5)
    frame9_save = tk.Button(frame9_frame,text = "Save",command=lambda:saving_coupons(20))
    frame9_save.pack(side="left")
    frame9_close = tk.Button(frame9_frame,text = "Close",command=lambda:window.destroy())
    frame9_close.pack(side="left")
    frame9_title = tk.Label(frame9, text='20% Coupon! Congratulations!', font='times 20')

    frame9_title.pack( side='bottom')


elif(mat[a][b]%2==0):
    frame9_frame = tk.Frame(frame9)
    frame9_frame.pack(side="bottom")
    frame9_frame.pack(side="bottom",pady=5)
    frame9_save = tk.Button(frame9_frame,text = "Save",command=lambda: saving_coupons(10))
    frame9_save.pack(side="left")
    frame9_close = tk.Button(frame9_frame,text = "Close",command=lambda:window.destroy())
    frame9_close.pack(side="left")
    frame9_title1 = tk.Label(frame9, text='10% Coupon! Congratulations ', font='times 20')

    frame9_title1.pack( side='bottom')



else:
    frame9_frame = tk.Frame(frame9)
    frame9_frame.pack(side="bottom")
    frame9_close = tk.Button(frame9_frame,text = "Close",command=lambda:window.destroy())
    frame9_close.pack(side="left")
    frame9_title2 = tk.Label(frame9, text='Sorry! Hope you can get it next time!', font='times 20')

    frame9_title2.pack( side='bottom')


show_frame(frame1)
window.mainloop()
