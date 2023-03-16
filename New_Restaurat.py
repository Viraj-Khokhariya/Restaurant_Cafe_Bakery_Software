import random
import time
import datetime
import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1250x750+0+0")
root.title("BILLING SOFTWARE")
root.configure(background= 'powder blue')

Tops= Frame(root, bg='Cadet Blue', bd=20, pady =5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle =Label(Tops, font=('arial',30,'bold'),width=48,text='BILLING SOFTWARE',bd=20,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F= Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame= Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)

Drink_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drink_F.pack(side=TOP)

Drink_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drink_F.pack(side=LEFT)
Chickdish_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Chickdish_F.pack(side=RIGHT)

#===========================================Variables==============================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()

DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofDishes= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

E_BathSoap=StringVar()
E_FaceCream=StringVar()
E_Champagne=StringVar()
E_Bira=StringVar()
E_Corona=StringVar()
E_Budweiser=StringVar()
E_Hoegaarden=StringVar()
E_Heineken=StringVar()

E_CocaCola=StringVar()
E_Sprite=StringVar()
E_Pepsi=StringVar()
E_MountainDew=StringVar()
E_Fanta=StringVar()
E_Mirinda=StringVar()
E_SevenUp=StringVar()
E_Maaza=StringVar()

E_Roganjosh=StringVar()
E_Butterchicken=StringVar()
E_Tikkamasala=StringVar()
E_Bhuna=StringVar()
E_Hybiryani=StringVar()
E_Dumbiryani=StringVar()
E_Kadhai=StringVar()
E_Chefspecial=StringVar()

E_BathSoap.set("0")
E_FaceCream.set("0")
E_Champagne.set("0")
E_Bira.set("0")
E_Corona.set("0")
E_Budweiser.set("0")
E_Hoegaarden.set("0")
E_Heineken.set("0")

E_CocaCola.set("0")
E_Sprite.set("0")
E_Pepsi.set("0")
E_MountainDew.set("0")
E_Fanta.set("0")
E_Mirinda.set("0")
E_SevenUp.set("0")
E_Maaza.set("0")

E_Roganjosh.set("0")
E_Butterchicken.set("0")
E_Tikkamasala.set("0")
E_Bhuna.set("0")
E_Hybiryani.set("0")
E_Dumbiryani.set("0")
E_Kadhai.set("0")
E_Chefspecial.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Function Declaration======================================
class funcdeclare:
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
        if iExit>0:
            root.destroy()
            return

    def Reset(self):
        E_BathSoap.set("0")
        E_FaceCream.set("0")
        E_Champagne.set("0")
        E_Bira.set("0")
        E_Corona.set("0")
        E_Budweiser.set("0")
        E_Hoegaarden.set("0")
        E_Heineken.set("0")

        E_CocaCola.set("0")
        E_Sprite.set("0")
        E_Pepsi.set("0")
        E_MountainDew.set("0")
        E_Fanta.set("0")
        E_Mirinda.set("0")
        E_SevenUp.set("0")
        E_Maaza.set("0")

        E_Roganjosh.set("0")
        E_Butterchicken.set("0")
        E_Tikkamasala.set("0")
        E_Bhuna.set("0")
        E_Hybiryani.set("0")
        E_Dumbiryani.set("0")
        E_Kadhai.set("0")
        E_Chefspecial.set("0")

        CostofDishes.set("0")
        CostofDrinks.set("0")
        ServiceCharge.set("0")
        SubTotal.set("0")
        PaidTax.set("0")
        TotalCost.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)
        var23.set(0)
        var24.set(0)

        txtBathSoap.configure(state =DISABLED)
        txtFaceCream.configure(state=DISABLED)
        txtChampagne.configure(state=DISABLED)
        txtBira.configure(state=DISABLED)
        txtCorona.configure(state=DISABLED)
        txtBudweiser.configure(state=DISABLED)
        txtHoegaarden.configure(state=DISABLED)
        txtHeineken.configure(state=DISABLED)

        txtCocaCola.configure(state =DISABLED)
        txtSprite.configure(state=DISABLED)
        txtPepsi.configure(state=DISABLED)
        txtMountainDew.configure(state=DISABLED)
        txtFanta.configure(state=DISABLED)
        txtMirinda.configure(state=DISABLED)
        txtSevenUp.configure(state=DISABLED)
        txtMaaza.configure(state=DISABLED)
        
        txtRoganjosh.configure(state=DISABLED)
        txtButterChicken.configure(state=DISABLED)
        txtTikkamasala.configure(state=DISABLED)
        txtBhuna.configure(state=DISABLED)
        txtHybiryani.configure(state=DISABLED)
        txtDumbiryani.configure(state=DISABLED)
        txtKadhai.configure(state=DISABLED)
        txtChefspecial.configure(state=DISABLED)

        txtReceipt.delete("1.0",END)

    def CostofItem(self):
        Item1=float(E_BathSoap.get())
        Item2=float(E_FaceCream.get())
        Item3=float(E_Champagne.get())
        Item4=float(E_Bira.get())
        Item5=float(E_Corona.get())
        Item6=float(E_Budweiser.get())
        Item7=float(E_Hoegaarden.get())
        Item8=float(E_Heineken.get())

        Item9=float(E_CocaCola.get())
        Item10=float(E_Sprite.get())
        Item11=float(E_Pepsi.get())
        Item12=float(E_MountainDew.get())
        Item13=float(E_Fanta.get())
        Item14=float(E_Mirinda.get())
        Item15=float(E_SevenUp.get())
        Item16=float(E_Maaza.get())

        Item17=float(E_Roganjosh.get())
        Item18=float(E_Butterchicken.get())
        Item19=float(E_Tikkamasala.get())
        Item20=float(E_Bhuna.get())
        Item21=float(E_Hybiryani.get())
        Item22=float(E_Dumbiryani.get())
        Item23=float(E_Kadhai.get())
        Item24=float(E_Chefspecial.get())

        PriceofDrinks=((Item1 * 40 ) + (Item2 * 200) + (Item3 * 40) + (Item4 * 300)+ (Item5 * 700) + (Item6 * 400) + (Item7 * 700) + (Item8 * 90))+((Item9 * 40 ) + (Item10 * 70) + (Item11 * 40) + (Item12 * 90)+ (Item13 * 80) + (Item14 * 110) + (Item15 * 105) + (Item16 * 95))
        PriceofDishes=((Item17 * 200) + (Item18 * 250) + (Item19 * 230) + (Item20 * 200) + (Item21 * 300) + (Item22 * 280) + (Item23 * 200) + (Item24 * 400))


        DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
        DishesPrice="Rs", str('%.2f'%(PriceofDishes))
        CostofDishes.set(DishesPrice)
        CostofDrinks.set(DrinksPrice)
        SC="Rs", str('%.2f'%(2.5))
        ServiceCharge.set(SC)

        SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + PriceofDishes + 2.5))
        SubTotal.set(SubTotalofITEMS)

        Tax="Rs", str('%.2f'%((PriceofDrinks + PriceofDishes + 2.5)*0.5))
        PaidTax.set(Tax)
        TT=((PriceofDrinks + PriceofDishes + 2.5) * 0.5)
        TC="Rs", str('%.2f'%(PriceofDishes + PriceofDrinks + 2.5 + TT))
        
        TotalCost.set(TC)
        


    def chkBathSoap(self):
        if(var1.get()==1):
            txtBathSoap.configure(state= NORMAL)
            txtBathSoap.focus()
            txtBathSoap.delete('0', END)
            E_BathSoap.set("")
        elif(var1.get()==0):
            txtBathSoap.configure(state= DISABLED)
            E_BathSoap.set("0")
    def chkFaceCream(self):
        if(var2.get()==1):
            txtFaceCream.configure(state= NORMAL)
            txtFaceCream.focus()
            txtFaceCream.delete('0', END)
            E_FaceCream.set("")
        elif(var2.get()==0):
            txtFaceCream.configure(state= DISABLED)
            E_FaceCream.set("0")
    def chkChampagne(self):
        if(var3.get()==1):
            txtChampagne.configure(state= NORMAL)
            txtChampagne.focus()
            txtChampagne.delete('0', END)
            E_Champagne.set("")
        elif(var3.get()==0):
            txtChampagne.configure(state= DISABLED)
            E_Champagne.set("0")
    def chkBira(self):
        if(var4.get()==1):
            txtBira.configure(state= NORMAL)
            txtBira.focus()
            txtBira.delete('0', END)
            E_Bira.set("")
        elif(var4.get()==0):
            txtBira.configure(state= DISABLED)
            E_Bira.set("0")
    def chkCorona(self):
        if(var5.get()==1):
            txtCorona.configure(state= NORMAL)
            txtCorona.focus()
            txtCorona.delete('0', END)
            E_Corona.set("")
        elif(var5.get()==0):
            txtCorona.configure(state= DISABLED)
            E_Corona.set("0")
    def chkBudweiser(self):
        if(var6.get()==1):
            txtBudweiser.configure(state= NORMAL)
            txtBudweiser.focus()
            txtBudweiser.delete('0', END)
            E_Budweiser.set("")
        elif(var6.get()==0):
            txtBudweiser.configure(state= DISABLED)
            E_Budweiser.set("0")
    def chkHoegaarden(self):
        if(var7.get()==1):
            txtHoegaarden.configure(state= NORMAL)
            txtHoegaarden.focus()
            txtHoegaarden.delete('0', END)
            E_Hoegaarden.set("")
        elif(var7.get()==0):
            txtHoegaarden.configure(state= DISABLED)
            E_Hoegaarden.set("0")
    def chkHeineken(self):
        if(var8.get()==1):
            txtHeineken.configure(state= NORMAL)
            txtHeineken.focus()
            txtHeineken.delete('0', END)
            E_Heineken.set("")
        elif(var8.get()==0):
            txtHeineken.configure(state= DISABLED)
            E_Heineken.set("0")

    def CocaCola(self):
        if(var9.get()==1):
            txtCocaCola.configure(state= NORMAL)
            txtCocaCola.focus()
            txtCocaCola.delete('0', END)
            E_CocaCola.set("")
        elif(var9.get()==0):
            txtCocaCola.configure(state= DISABLED)
            E_CocaCola.set("0")
    def Sprite(self):
        if(var10.get()==1):
            txtSprite.configure(state= NORMAL)
            txtSprite.focus()
            txtSprite.delete('0', END)
            E_Sprite.set("")
        elif(var1.get()==0):
            txtSprite.configure(state= DISABLED)
            E_Sprite.set("0")        
    def Pepsi(self):
        if(var11.get()==1):
            txtPepsi.configure(state= NORMAL)
            txtPepsi.focus()
            txtPepsi.delete('0', END)
            E_Pepsi.set("")
        elif(var11.get()==0):
            txtPepsi.configure(state= DISABLED)
            E_Pepsi.set("0")
    def MountainDew(self):
        if(var12.get()==1):
            txtMountainDew.configure(state= NORMAL)
            txtMountainDew.focus()
            txtMountainDew.delete('0', END)
            E_MountainDew.set("")
        elif(var12.get()==0):
            txtMountainDew.configure(state= DISABLED)
            E_MountainDew.set("0")
    def Fanta(self):
        if(var13.get()==1):
            txtFanta.configure(state= NORMAL)
            txtFanta.focus()
            txtFanta.delete('0', END)
            E_Fanta.set("")
        elif(var13.get()==0):
            txtFanta.configure(state= DISABLED)
            E_Fanta.set("0")
    def Mirinda(self):
        if(var14.get()==1):
            txtMirinda.configure(state= NORMAL)
            txtMirinda.focus()
            txtMirinda.delete('0', END)
            E_Mirinda.set("")
        elif(var14.get()==0):
            txtMirinda.configure(state= DISABLED)
            E_Mirinda.set("0")
    def SevenUp(self):
        if(var15.get()==1):
            txtSevenUp.configure(state= NORMAL)
            txtSevenUp.focus()
            txtSevenUp.delete('0', END)
            E_SevenUp.set("")
        elif(var15.get()==0):
            txtSevenUp.configure(state= DISABLED)
            E_SevenUp.set("0")
    def Maaza(self):
        if(var16.get()==1):
            txtMaaza.configure(state= NORMAL)
            txtMaaza.focus()
            txtMaaza.delete('0', END)
            E_Maaza.set("")
        elif(var16.get()==0):
            txtMaaza.configure(state= DISABLED)
            E_Maaza.set("0")
    
    def chkRoganjosh(self):
        if(var17.get()==1):
            txtRoganjosh.configure(state= NORMAL)
            txtRoganjosh.focus()
            txtRoganjosh.delete('0', END)
            E_Roganjosh.set("")
        elif(var17.get()==0):
            txtRoganjosh.configure(state= DISABLED)
            E_Roganjosh.set("0")
    def chkButterchicken(self):
        if(var18.get()==1):
            txtButterChicken.configure(state= NORMAL)
            txtButterChicken.focus()
            txtButterChicken.delete('0', END)
            E_Butterchicken.set("")
        elif(var18.get()==0):
            txtButterChicken.configure(state= DISABLED)
            E_Butterchicken.set("0")
    def chkTikkamasala(self):
        if(var19.get()==1):
            txtTikkamasala.configure(state= NORMAL)
            txtTikkamasala.focus()
            txtTikkamasala.delete('0', END)
            E_Tikkamasala.set("")
        elif(var19.get()==0):
            txtTikkamasala.configure(state= DISABLED)
            E_Tikkamasala.set("0")
    def chkBhuna(self):
        if(var20.get()==1):
            txtBhuna.configure(state= NORMAL)
            txtBhuna.focus()
            txtBhuna.delete('0', END)
            E_Bhuna.set("")
        elif(var20.get()==0):
            txtBhuna.configure(state= DISABLED)
            E_Bhuna.set("0")
    def chkHybiryani(self):
        if(var21.get()==1):
            txtHybiryani.configure(state= NORMAL)
            txtHybiryani.focus()
            txtHybiryani.delete('0', END)
            E_Hybiryani.set("")
        elif(var21.get()==0):
            txtHybiryani.configure(state= DISABLED)
            E_Hybiryani.set("0")
    def chkDumbiryani(self):
        if(var22.get()==1):
            txtDumbiryani.configure(state= NORMAL)
            txtDumbiryani.focus()
            txtDumbiryani.delete('0', END)
            E_Dumbiryani.set("")
        elif(var22.get()==0):
            txtDumbiryani.configure(state= DISABLED)
            E_Dumbiryani.set("0")
    def chkKadhai(self):
        if(var23.get()==1):
            txtKadhai.configure(state= NORMAL)
            txtKadhai.focus()
            txtKadhai.delete('0', END)
            E_Kadhai.set("")
        elif(var23.get()==0):
            txtKadhai.configure(state= DISABLED)
            E_Kadhai.set("0")
    def chkChefspecial(self):
        if(var24.get()==1):
            txtChefspecial.configure(state= NORMAL)
            txtChefspecial.focus()
            txtChefspecial.delete('0', END)
            E_Chefspecial.set("")
        elif(var24.get()==0):
            txtChefspecial.configure(state= DISABLED)
            E_Chefspecial.set("0")
            
    def Receipt(self):
        txtReceipt.delete("1.0",END)
        x= random.randint(10903, 609235)
        randomRef= str(x)
        Receipt_Ref.set("BILL" + randomRef)     

        txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
        txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
        txtReceipt.insert(END, 'Champagne: \t\t\t\t' + E_BathSoap.get() + "\n")
        txtReceipt.insert(END, 'Irish: \t\t\t\t' + E_FaceCream.get() + "\n")
        txtReceipt.insert(END, 'Jack Daniel: \t\t\t\t' + E_Champagne.get() + "\n")
        txtReceipt.insert(END, 'Cocktail: \t\t\t\t' + E_Bira.get() + "\n")
        txtReceipt.insert(END, 'Red Wine: \t\t\t\t' + E_Corona.get() + "\n")
        txtReceipt.insert(END, 'Scoth: \t\t\t\t' + E_Budweiser.get() + "\n")
        txtReceipt.insert(END, 'Jhonny W: \t\t\t\t' + E_Hoegaarden.get() + "\n")
        txtReceipt.insert(END, 'Red Label: \t\t\t\t' + E_Heineken.get() + "\n")

        txtReceipt.insert(END, 'CocaCola: \t\t\t\t' + E_CocaCola.get() + "\n")
        txtReceipt.insert(END, 'Sprite: \t\t\t\t' + E_Sprite.get() + "\n")
        txtReceipt.insert(END, 'Pepsi: \t\t\t\t' + E_Pepsi.get() + "\n")
        txtReceipt.insert(END, 'Mountain Dew: \t\t\t\t' + E_MountainDew.get() + "\n")
        txtReceipt.insert(END, 'Fanta: \t\t\t\t' + E_Fanta.get() + "\n")
        txtReceipt.insert(END, 'Mirinda: \t\t\t\t' + E_Mirinda.get() + "\n")
        txtReceipt.insert(END, '7 Up: \t\t\t\t' + E_SevenUp.get() + "\n")
        txtReceipt.insert(END, 'Maaza: \t\t\t\t' + E_Maaza.get() + "\n")
        
        txtReceipt.insert(END, 'Pav-Bhaji: \t\t\t\t' + E_Roganjosh.get() + "\n")
        txtReceipt.insert(END, 'Butter Bhaji: \t\t\t\t' + E_Butterchicken.get() + "\n")
        txtReceipt.insert(END, 'Special Bhaji: \t\t\t\t' + E_Tikkamasala.get() + "\n")
        txtReceipt.insert(END, 'Cheese Bhaji: \t\t\t\t' + E_Bhuna.get() + "\n")
        txtReceipt.insert(END, 'Hydera Biryani: \t\t\t\t' + E_Hybiryani.get() + "\n")
        txtReceipt.insert(END, 'Surati Locho: \t\t\t\t' + E_Dumbiryani.get() + "\n")
        txtReceipt.insert(END, 'Jira-Rice: \t\t\t\t' + E_Kadhai.get() + "\n")
        txtReceipt.insert(END, 'Kaju-curry: \t\t\t\t' + E_Chefspecial.get() + "\n")
        txtReceipt.insert(END, 'Final Total: \t\t\t' + TotalCost.get() + "\n")

obj=funcdeclare()

#===========================================Drinks===================================================

BathSoap=Checkbutton(Drinks_F, text='Champagne', variable=var1, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkBathSoap).grid(row=0,sticky=W)
FaceCream=Checkbutton(Drinks_F, text='Irish', variable=var2, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkFaceCream).grid(row=1,sticky=W)
Champagne=Checkbutton(Drinks_F, text='Jack Daniel', variable=var3, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkChampagne).grid(row=2,sticky=W)
Bira=Checkbutton(Drinks_F, text='Cocktail', variable=var4, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkBira).grid(row=3,sticky=W)
Corona=Checkbutton(Drinks_F, text='Red Wine', variable=var5, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkCorona).grid(row=4,sticky=W)
Budweiser=Checkbutton(Drinks_F, text='Scoth', variable=var6, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkBudweiser).grid(row=5,sticky=W)
Hoegaarden=Checkbutton(Drinks_F, text='Jhonny W', variable=var7, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkHoegaarden).grid(row=6,sticky=W)
Heineken=Checkbutton(Drinks_F, text='Red Label', variable=var8, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkHeineken).grid(row=7,sticky=W)


#===========================================Entry Box for Drinks===========================================================

txtBathSoap= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_BathSoap)
txtBathSoap.grid(row=0,column=1)

txtFaceCream= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_FaceCream)
txtFaceCream.grid(row=1,column=1)

txtChampagne= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Champagne)
txtChampagne.grid(row=2,column=1)

txtBira= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Bira)
txtBira.grid(row=3,column=1)

txtCorona= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Corona)
txtCorona.grid(row=4,column=1)

txtBudweiser= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Budweiser)
txtBudweiser.grid(row=5,column=1)

txtHoegaarden= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Hoegaarden)
txtHoegaarden.grid(row=6,column=1)

txtHeineken= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Heineken)
txtHeineken.grid(row=7,column=1)


#===========================================Drinks2===================================================

CocaCola=Checkbutton(Drink_F, text='CocaCola', variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.CocaCola).grid(row=0,column=2,sticky=W)
Sprite=Checkbutton(Drink_F, text='Sprite', variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.Sprite).grid(row=1,column=2,sticky=W)
Pepsi=Checkbutton(Drink_F, text='Pepsi', variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.Pepsi).grid(row=2,column=2,sticky=W)
MountainDew=Checkbutton(Drink_F, text='Mountain Dew', variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.MountainDew).grid(row=3,column=2,sticky=W)
Fanta=Checkbutton(Drink_F, text='Fanta', variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.Fanta).grid(row=4,column=2,sticky=W)
Mirinda=Checkbutton(Drink_F, text='Mirinda', variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.Mirinda).grid(row=5,column=2,sticky=W)
SevenUp=Checkbutton(Drink_F, text='7 Up', variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.SevenUp).grid(row=6,column=2,sticky=W)
Maaza=Checkbutton(Drink_F, text='Maaza', variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.Maaza).grid(row=7,column=2,sticky=W)


#===========================================Entry Box for Drinks2===========================================================

txtCocaCola= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_CocaCola)
txtCocaCola.grid(row=0,column=3)

txtSprite= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sprite)
txtSprite.grid(row=1,column=3)

txtPepsi= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Pepsi)
txtPepsi.grid(row=2,column=3)

txtMountainDew= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_MountainDew)
txtMountainDew.grid(row=3,column=3)

txtFanta= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Fanta)
txtFanta.grid(row=4,column=3)

txtMirinda= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Mirinda)
txtMirinda.grid(row=5,column=3)

txtSevenUp= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_SevenUp)
txtSevenUp.grid(row=6,column=3)

txtMaaza= Entry(Drink_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Maaza)
txtMaaza.grid(row=7,column=3)



#===========================================Dishes=================================================================

Roganjosh=Checkbutton(Chickdish_F, text='Pav-Bhaji', variable=var17, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkRoganjosh).grid(row=0,sticky=W)
ButterChicken=Checkbutton(Chickdish_F, text='Butter Bhaji', variable=var18, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkButterchicken).grid(row=1,sticky=W)
Tikkamasala=Checkbutton(Chickdish_F, text='Special Bhaji', variable=var19, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue",command=obj.chkTikkamasala).grid(row=2,sticky=W)
Bhuna=Checkbutton(Chickdish_F, text='Cheese Bhaji', variable=var20, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkBhuna).grid(row=3,sticky=W)
Hybiryani=Checkbutton(Chickdish_F, text='Hydera Biryani', variable=var21, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkHybiryani).grid(row=4,sticky=W)
Dumbiryani=Checkbutton(Chickdish_F, text='Surati Locho', variable=var22, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkDumbiryani).grid(row=5,sticky=W)
Kadhai=Checkbutton(Chickdish_F, text='Jira-Rice', variable=var23, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkKadhai).grid(row=6,sticky=W)
Chefspecial=Checkbutton(Chickdish_F, text='Kaju-curry', variable=var24, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkChefspecial).grid(row=7,sticky=W)


#===========================================Entry Box for Dishes===================================================

txtRoganjosh= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Roganjosh)
txtRoganjosh.grid(row=0,column=1)
txtButterChicken= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Butterchicken)
txtButterChicken.grid(row=1,column=1)
txtTikkamasala= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Tikkamasala)
txtTikkamasala.grid(row=2,column=1)
txtBhuna= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Bhuna)
txtBhuna.grid(row=3,column=1)
txtHybiryani= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Hybiryani)
txtHybiryani.grid(row=4,column=1)
txtDumbiryani= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Dumbiryani)
txtDumbiryani.grid(row=5,column=1)
txtKadhai= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Kadhai)
txtKadhai.grid(row=6,column=1)
txtChefspecial= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Chefspecial)
txtChefspecial.grid(row=7,column=1)

#=======================================================Total Cost=========================================================
lblCostofDrinks =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Drinks\t',bg='Powder Blue',fg='black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks= Entry(Cost_F, width=28, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblCostofDishes =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Dishes\t',bg='Powder Blue',fg='black')
lblCostofDishes.grid(row=1,column=0, sticky=W)
txtCostofDishes= Entry(Cost_F, width=28, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=CostofDishes)
txtCostofDishes.grid(row=1, column=1)

lblServiceCharge =Label(Cost_F, font=('arial',14,'bold'),text='Service Charge\t',bg='Powder Blue',fg='black')
lblServiceCharge.grid(row=2,column=0, sticky=W)
lblServiceCharge= Entry(Cost_F, bg='white',width=28, bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=ServiceCharge)
lblServiceCharge.grid(row=2, column=1)

#=======================================================Payment Information================================================
lblPaidTax =Label(Cost_F, font=('arial',14,'bold'),text='\tPaid Tax',bg='Powder Blue',fg='black')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax= Entry(Cost_F, width=27, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal =Label(Cost_F, font=('arial',14,'bold'),text='\tSub Total',bg='Powder Blue',fg='black')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal= Entry(Cost_F, width=27, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost =Label(Cost_F, font=('arial',14,'bold'),text='\tTotal Cost',bg='Powder Blue',fg='black')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost= Entry(Cost_F, width=27, bg='white', bd=7, font=('arial',10,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)


#=======================================================Receipt============================================================

txtReceipt= Text(Receipt_F, width=40, height=6.7, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#=======================================================Buttons============================================================

btnTotal=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Total", bg="Powder Blue", command=obj.CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Receipt", bg="Powder Blue", command=obj.Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Reset", bg="Powder Blue", command=obj.Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="Exit", bg="Powder Blue", command=obj.iExit).grid(row=0,column=3)

#=======================================================Calculator Display=================================================

class calcfunc:
    def btnClick(self,numbers):
        global operator
        operator= operator + str(numbers)
        text_Input.set(operator)

    def btnClear(self):
        global operator
        operator = ""
        text_Input.set("")

    def btnEquals(self):
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

    txtDisplay= Entry(Cal_F, width=40, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable= text_Input)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
    txtDisplay.insert(0,"0")

obj1=calcfunc()

#=======================================================Calculator Buttons=================================================

btn7=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="7", bg="Powder Blue", command=lambda:obj1.btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="8", bg="Powder Blue", command=lambda:obj1.btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="9", bg="Powder Blue", command=lambda:obj1.btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="+", bg="Powder Blue", command=lambda:obj1.btnClick("+")).grid(row=2,column=3)

#=======================================================Calculator Buttons=================================================

btn4=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="4", bg="Powder Blue", command=lambda:obj1.btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="5", bg="Powder Blue", command=lambda:obj1.btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="6", bg="Powder Blue", command=lambda:obj1.btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="-", bg="Powder Blue", command=lambda:obj1.btnClick("-")).grid(row=3,column=3)

#=======================================================Calculator Buttons=================================================

btn1=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="1", bg="Powder Blue", command=lambda:obj1.btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="2", bg="Powder Blue", command=lambda:obj1.btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="3", bg="Powder Blue", command=lambda:obj1.btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="*", bg="Powder Blue", command=lambda:obj1.btnClick("*")).grid(row=4,column=3)

#=======================================================Calculator Buttons=================================================

btn0=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="0", bg="Powder Blue", command=lambda:obj1.btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="C", bg="Powder Blue", command=obj1.btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="=", bg="Powder Blue", command=obj1.btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=3, text="/", bg="Powder Blue", command=lambda:obj1.btnClick("/")).grid(row=5,column=3)


root.mainloop()
