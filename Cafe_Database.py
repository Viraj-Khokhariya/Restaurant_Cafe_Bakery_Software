from tkinter import *
import time
import datetime
import re
import random
from PIL import ImageTk, Image

r = Tk()
r.geometry('1175x725+100+20')
r.title("Cafe Management System")

#--------------------------------------------------------------#
coverFrame = Frame(r,bd=10,pady=2,relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame(coverFrame,bd=10,pady=2,bg='cadet blue',relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame(coverMainFrame,bd=5,pady=2,relief=RIDGE)
MainFrame.grid()

tops = Frame(MainFrame,bd=10,width=1000,height=50,bg='cadet blue',relief=SUNKEN)
tops.grid(row=0, column=0)

top2 = Frame(MainFrame,bd=10,width=1000,height=700,bg='cadet blue',relief=SUNKEN)
top2.grid(row=1, column=0)

f1 = Frame(top2,width=700,height=600,bd=10,relief=SUNKEN)
f1.grid(row=0, column=0)

f1a = Frame(f1,width=700,height=600,bd=10,relief=SUNKEN,bg='white')
f1a.grid(row=0, column=0)
f1b = Frame(f1,width=700,height=150,bd=10,relief=SUNKEN,bg='grey20')
f1b.grid(row=1, column=0)

f2 = Frame(top2,width=300,height=700,bd=10,relief=SUNKEN,bg='grey20')
f2.grid(row=0, column=1)
#--------------------------------------------------------------#

image = Image.open("rest.jpg")
tk_img = ImageTk.PhotoImage(image.resize((210,150)))
l1 = Label(tops,font=('Comic Sans MS',40,'bold'),text="TBJ's Cafe",
           image=tk_img,fg='white',bg='grey20',width=1090,compound='left')
l1.grid(row=0,column=0)

#--------------------------------------------------------------#

expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    txt = t2.get()
    t2.delete(first=len(txt)-1,last="end")
    
def ref():
    x = random.randint(000,999)
    randRef = str(x)
    rand.set(randRef)

    CoT = float(Tea.get())
    CoD = float(Drinks.get())
    CoI = float(Ice.get())
    CoB = float(Burger.get())
    CoS = float(Sandwich.get())

    CostofTea   = CoT * 8
    CostofDrinks= CoD * 18
    CostofIce   = CoI * 38
    CostBurger  = CoB * 109
    CostSandwich= CoS * 49

    CostofMeal= "Rs.", str('%.2f' %(CostofTea+CostofDrinks+CostofIce+CostBurger+CostSandwich))
    COM = CostofTea+CostofDrinks+CostofIce+CostBurger+CostSandwich
    TotalCost =(CostofTea+CostofDrinks+CostofIce+CostBurger+CostSandwich)
    cgstCost  = TotalCost * 0.18
    cgstflot = "Rs.", str('%.2f' %(cgstCost))
    sgstCost  = TotalCost * 0.18
    sgstflot = "Rs.", str('%.2f' %(cgstCost))
    subTotal1 = "Rs.", str('%.2f' %(CostofTea+CostofDrinks+CostofIce+CostBurger+CostSandwich+cgstCost+sgstCost))
    SOM = CostofTea+CostofDrinks+CostofIce+CostBurger+CostSandwich+cgstCost+sgstCost
    
    costmeal.set(CostofMeal)
    cgst.set(cgstflot)
    sgst.set(sgstflot)
    subTotal.set(subTotal1)

    print(COM)
    print(cgstCost)
    print(sgstCost)
    print(SOM)
#--------------------------------------------------------------#
    #def database():
    import mysql.connector
    pb = mysql.connector.connect(
        host='localhost',
        username='root',
        password='',
        database='jonty'
        )

    mycursor = pb.cursor()

    sql ="insert into cafe(order_no,tea,drinks,ice_cream,burger,sandwich,cost_meal,cgst,sgst,total)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (ordernoT.get(),teaT.get(),drinkT.get(),iceT.get(),burgerT.get(),
            sandT.get(),COM,cgstCost,sgstCost,SOM)

    mycursor.execute(sql,val)
    pb.commit()
    print(mycursor.rowcount,"Record Inserted")

def view():
    import mysql.connector
    import tkinter  as tk 
     
    my_w = tk.Tk()
    my_w.geometry("900x400") 
    my_connect = mysql.connector.connect(
      host="localhost",
      user="root", 
      passwd="",
      database="jonty"
    )
    my_conn = my_connect.cursor()

    my_conn.execute("SELECT * FROM cafe")
    e=Label(my_w,width=10,text='Order No.', relief='ridge',bg='powder blue')
    e.grid(row=0,column=0)
    e=Label(my_w,width=10,text='Tea',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=1)
    e=Label(my_w,width=10,text='Drinks',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=2)
    e=Label(my_w,width=10,text='Ice Cream',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=3)
    e=Label(my_w,width=10,text='Burger',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=4)
    e=Label(my_w,width=10,text='Sandwich',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=5)
    e=Label(my_w,width=10,text='Cost of Meal',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=6)
    e=Label(my_w,width=10,text='CGST',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=7)
    e=Label(my_w,width=10,text='SGST',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=8)
    e=Label(my_w,width=10,text='Total',borderwidth=2, relief='ridge',bg='powder blue')
    e.grid(row=0,column=9)

    i=0 
    for student in my_conn: 
        for j in range(len(student)):
            e = Entry(my_w, width=12, fg='blue') 
            e.grid(row=i+1, column=j) 
            e.insert(END, student[j])
        i=i+1
    my_w.mainloop()

def Database():
    import mysql.connector
    pb = mysql.connector.connect(
        host='localhost',
        username='root',
        password='',
        database='jonty'
        )

    mycursor = pb.cursor()

    mycursor.execute()
    pb.commit()
    print(mycursor.rowcount,"Record Inserted")

def dell():
    import mysql.connector
    from tkinter import messagebox
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jonty"
    )
    mycursor=mydb.cursor()
    r2=Tk()
    r2.title("Cafe Data")
    r2.geometry("400x200")

    label0=Label(r2,text="Enter the Order Number to Delete the Record",font=(15),width=40,height=2).grid(columnspan=2)
    label1=Label(r2,text="Order No.",width=20,height=2,bg="pink").grid(row=1,column=0)
    
    e1=Entry(r2,width=30)
    e1.grid(row=1,column=1)

    def Delete():
        O_No=e1.get()
        Delete="delete from cafe where order_no='%s'" %(O_No)
        mycursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")
        e1.delete(0,END)

    button2=Button(r2,text="Delete",width=10,height=2,command=Delete).grid(row=7,column=1)
    r2.mainloop()

def update():
    import mysql.connector
    from tkinter import messagebox
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="jonty"
    )
    mycursor=mydb.cursor()
    r2=Tk()
    r2.title("Cafe Data")
    r2.geometry("400x200")

    label0=Label(r2,text="Enter the Modified Detail to update the Record",font=(15),width=40,height=2).grid(columnspan=2)
    label1=Label(r2,text="Order No.",width=20,height=2,bg="pink").grid(row=1,column=0)
    
    e1=Entry(r2,width=30)
    e1.grid(row=1,column=1)

    def Delete():
        O_No=e1.get()
        Delete="delete from cafe where order_no='%s'" %(O_No)
        mycursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")
        e1.delete(0,END)

    button2=Button(r2,text="Delete",width=10,height=2,command=Delete).grid(row=7,column=1)
    r2.mainloop()
    

#--------------------------------------------------------------#   
def qExit():
    r.destroy()

def Reset():
    rand.set("")
    Tea.set("0")
    Drinks.set("0")
    Ice.set("0")
    Burger.set("0")
    Sandwich.set("0")
    cgst.set("")
    sgst.set("")
    costmeal.set("")
    subTotal.set("")

def price():
    roo = Tk()
    roo.geometry("460x300")
    roo.title("Price List")
    roo.configure(background='grey20')
    Lbl = Label(roo, font=('Comic Sans MS', 25, 'bold'), text="Products", bg="grey20", fg="white", bd=5)
    Lbl.grid(row=0, column=0,sticky=W)
    Lbl = Label(roo, font=('Comic Sans MS', 25,'bold'), text="________", bg="grey20",fg="white", anchor=W)
    Lbl.grid(row=0, column=2)
    Lbl = Label(roo, font=('Comic Sans MS', 25, 'bold'), text="Price",bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=0, column=3,sticky=E)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="Tea", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=1, column=0,sticky=W)
    Lbl = Label(roo, font=('Comic Sans MS', 22,'bold'), text="________", bg="grey20",fg="white", anchor=W)
    Lbl.grid(row=1, column=2)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="8/-", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=1, column=3,sticky=E)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="Drinks", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=2, column=0,sticky=W)
    Lbl = Label(roo, font=('Comic Sans MS', 22,'bold'), text="________", bg="grey20",fg="white", anchor=W)
    Lbl.grid(row=2, column=2)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="18/-", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=2, column=3,sticky=E)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="Ice-Cream", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=3, column=0,sticky=W)
    Lbl = Label(roo, font=('Comic Sans MS', 22,'bold'), text="________", bg="grey20",fg="white", anchor=W)
    Lbl.grid(row=3, column=2)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="38/-", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=3, column=3,sticky=E)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="Burger", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=4, column=0,sticky=W)
    Lbl = Label(roo, font=('Comic Sans MS', 22,'bold'), text="________", bg="grey20",fg="white", anchor=W)
    Lbl.grid(row=4, column=2)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="109/-", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=4, column=3,sticky=E)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="Sandwitch", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=5, column=0,sticky=W)
    Lbl = Label(roo, font=('Comic Sans MS', 22,'bold'), text="________", bg="grey20",fg="white", anchor=W)
    Lbl.grid(row=5, column=2)
    Lbl = Label(roo, font=('Comic Sans MS', 22, 'bold'), text="49/-", bg="grey20", fg="white", anchor=W)
    Lbl.grid(row=5, column=3,sticky=E)
    roo.mainloop()
  
rand = StringVar()
Tea = StringVar()
Drinks = StringVar()
Ice = StringVar()
Burger = StringVar()
Sandwich = StringVar()
cgst = StringVar()
sgst = StringVar()
costmeal = StringVar()
subTotal =StringVar()

equation = StringVar()

Tea.set("0")
Drinks.set("0")
Ice.set("0")
Burger.set("0")
Sandwich.set("0")

t1 = Label(f2,text='Calculate your bill here!',width=15,font=('Arial 12 bold'),bd=10,bg='grey20',fg='white')
t1.grid(columnspan=4,ipadx=20)
t2 = Entry(f2,width=11,textvariable=equation,font=('Arial 15'),bd=10)
t2.grid(columnspan=4, ipadx=80)

button1 = Button(f2,text=' 1 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(1),height=0,width=5)
button1.grid(row=5, column=0)
button2 = Button(f2,text=' 2 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(2),height=0,width=5)
button2.grid(row=5, column=1)
button3 = Button(f2,text=' 3 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(3),height=0,width=5)
button3.grid(row=5, column=2)

button4 = Button(f2,text=' 4 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(4),height=1,width=5)
button4.grid(row=4, column=0)
button5 = Button(f2,text=' 5 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(5),height=1,width=5)
button5.grid(row=4, column=1)
button6 = Button(f2,text=' 6 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(6),height=1,width=5)
button6.grid(row=4, column=2)

button7 = Button(f2,text=' 7 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(7),height=1,width=5)
button7.grid(row=3, column=0)
button8 = Button(f2,text=' 8 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(8),height=1,width=5)
button8.grid(row=3, column=1)
button9 = Button(f2,text=' 9 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(9),height=1, width=5)
button9.grid(row=3, column=2)

button0 = Button(f2,text=' 0 ',fg='black',bg='powder blue',bd=5,
                 font=('Comic Sans MS',15,'bold'),command=lambda: press(0),height=1,width=5)
button0.grid(row=6, column=1)

plus = Button(f2,text=' + ',fg='black',bg='powder blue',bd=5,
              font=('Comic Sans MS',15,'bold'),command=lambda: press('+'),height=1,width=5)
plus.grid(row=5, column=3)

minus = Button(f2,text=' - ',fg='black',bg='powder blue',bd=5,
               font=('Comic Sans MS',15,'bold'),command=lambda: press('-'),height=1,width=5)
minus.grid(row=4, column=3)

multiply = Button(f2,text=' * ',fg='black', bg='powder blue',
                  bd=5,font=('Comic Sans MS',15,'bold'),command=lambda: press('*'),height=1,width=5)
multiply.grid(row=3, column=3)

divide = Button(f2,text=' / ', fg='black', bg='powder blue',bd=5,
                font=('Comic Sans MS',15,'bold'),command=lambda: press('/'),height=1,width=5)
divide.grid(row=2, column=3)

equal = Button(f2,text=' = ',fg='black',bg='powder blue',bd=5,
               font=('Comic Sans MS',15,'bold'),command=equalpress,height=1,width=5)
equal.grid(row=6, column=3)

clear = Button(f2,text='Clear',fg='black',bg='powder blue',bd=5,
               font=('Comic Sans MS',15,'bold'), command=clear,height=1,width=5)
clear.grid(row=6, column=0)

Decimal= Button(f2,text='.',fg='black',bg='powder blue',bd=5,
                font=('Comic Sans MS',15,'bold'),command=lambda: press('.'),height=1,width=5)
Decimal.grid(row=2, column=0)

delete = Button(f2,text='Del',fg='black',bg='powder blue',bd=5,
                font=('Comic Sans MS',15,'bold'),command=delete,height=1,width=5)
delete.grid(row=6, column=2)

module = Button(f2,text='%',fg='black',bg='powder blue',bd=5,
                font=('Comic Sans MS',15,'bold'),command=lambda: press('%'),height=1,width=5)
module.grid(row=2, column=1)
hash1 = Button(f2,text='#',fg='black',bg='powder blue',bd=5,
               font=('Comic Sans MS',15,'bold'),command=lambda: press('#'),height=1,width=5)
hash1.grid(row=2, column=2)

#------------------------------------------------------------------#
teaL = Label(f1a,text='Tea:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
teaL.grid(row=2, column=0, sticky=W)
teaT = Entry(f1a,width=19,bd=5,textvariable=Tea,font=('Comic Sans MS',15,'bold'),justify='center')
teaT.grid(row=2, column=1)

drinkL = Label(f1a,text='Drinks:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
drinkL.grid(row=3, column=0, sticky=W)
drinkT = Entry(f1a,width=19,bd=5,textvariable=Drinks,font=('Comic Sans MS',15,'bold'),justify='center')
drinkT.grid(row=3, column=1)

iceL = Label(f1a,text='Ice-Cream:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
iceL.grid(row=4, column=0, sticky=W)
iceT = Entry(f1a,width=19,bd=5,textvariable=Ice,font=('Comic Sans MS',15,'bold'),justify='center')
iceT.grid(row=4, column=1)

burgerL = Label(f1a,text='Burger:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
burgerL.grid(row=5, column=0, sticky=W)
burgerT = Entry(f1a,width=19,bd=5,textvariable=Burger,font=('Comic Sans MS',15,'bold'),justify='center')
burgerT.grid(row=5, column=1)

sandL = Label(f1a,text='Sandwich:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
sandL.grid(row=6, column=0, sticky=W)
sandT = Entry(f1a,width=19,bd=5,textvariable=Sandwich,font=('Comic Sans MS',15,'bold'),justify='center')
sandT.grid(row=6, column=1)

#------------------------------------------------------------------#
x = datetime.datetime.now()
y = x.strftime("%x")
z = x.strftime("%X")
dateL = Label(f1a,text='Date:',font=('Comic Sans MS',15,'bold'),fg='black',bg='white')
dateL.grid(row=1, column=2, sticky=W)
dateT = Label(f1a,width=19,bd=5,text = y,font=('Comic Sans MS',12,'bold'),justify='center',fg='black',bg='white')
dateT.grid(row=1, column=3)

timeL = Label(f1a,text='Time:',font=('Comic Sans MS',15,'bold'),fg='black',bg='white')
timeL.grid(row=1, column=0, sticky=W)
timeT = Label(f1a,width=19,bd=5,text = z,font=('Comic Sans MS',12,'bold'),justify='center',fg='black',bg='white')
timeT.grid(row=1, column=1)

ordernoL = Label(f1a,text='Order No.:',font=('Comic Sans MS',15,'bold'),fg='black',bg='white')
ordernoL.grid(row=2, column=2, sticky=W)
ordernoT = Entry(f1a,width=19,bd=5,textvariable=rand,font=('Comic Sans MS',15,'bold'),justify='center',fg='white',bg='grey')
ordernoT.grid(row=2, column=3)

costMealL = Label(f1a,text='Cost of Meal:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
costMealL.grid(row=3, column=2, sticky=W)
costMealT = Entry(f1a,width=19,bd=5,textvariable=costmeal,font=('Comic Sans MS',15,'bold'),justify='center')
costMealT.grid(row=3, column=3)

cgstL = Label(f1a,text='CGST@18%:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
cgstL.grid(row=4, column=2, sticky=W)
cgstT = Entry(f1a,width=19,bd=5,textvariable=cgst,font=('Comic Sans MS',15,'bold'),justify='center')
cgstT.grid(row=4, column=3)

sgstL = Label(f1a,text='SGST@18%:',font=('Comic Sans MS',15,'bold'),bg='white',fg='black')
sgstL.grid(row=5, column=2, sticky=W)
sgstT = Entry(f1a,width=19,bd=5,textvariable=sgst,font=('Comic Sans MS',15,'bold'),justify='center')
sgstT.grid(row=5, column=3)

totalL = Label(f1a,text='Total Cost:',font=('Comic Sans MS',15,'bold'),fg='red',bg='white')
totalL.grid(row=6, column=2, sticky=W)
totalT = Entry(f1a,width=19,bd=5,textvariable=subTotal,font=('Comic Sans MS',15,'bold'),justify='center',fg='red')
totalT.grid(row=6, column=3)
#------------------------------------------------------------------------#
plist = Button(f1b,padx=10,pady= 8,fg='black',bd=5,width=9,height=0,command=price,text='Price List',
               font=('Comic Sans MS',16,'bold'),bg='powder blue')
plist.grid(row=0, column=0,padx=5,pady= 5)
total = Button(f1b,padx=10,pady= 8,fg='black',bd=5,width=9,command=ref,text='Total&Insert',
               font=('Comic Sans MS',16,'bold'),bg='powder blue')
total.grid(row=0, column=1,padx=5,pady= 5)
reset = Button(f1b,padx=10,pady= 8,fg='red',bd=5,width=9,command=Reset,text='Reset',
               font=('Comic Sans MS',16,'bold'),bg='powder blue')
reset.grid(row=0, column=2,padx=5,pady= 5)
view = Button(f1b,padx=10,pady= 8,fg='black',bd=5,width=9,text='View',command=view,
               font=('Comic Sans MS',16,'bold'),bg='powder blue')
view.grid(row=1, column=0,padx=5,pady= 5)
delete1 = Button(f1b,padx=10,pady= 8,fg='black',bd=5,width=9,text='Delete record',command=dell,
               font=('Comic Sans MS',16,'bold'),bg='powder blue')
delete1.grid(row=1, column=1,padx=5,pady= 5)
exit1 = Button(f1b,padx=10,pady= 8,fg='black',bd=5,width=9,command=qExit,text='Exit',
               font=('Comic Sans MS',16,'bold'),bg='powder blue')
exit1.grid(row=1, column=2,padx=5,pady= 5)

r.mainloop()

