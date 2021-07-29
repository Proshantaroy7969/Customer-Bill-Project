from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billig Software")
        bg_color ="#074463"
        title = Label(self.root, text="Billing Software",bd=12,relief=GROOVE,bg=bg_color ,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #===========Variables==========
        #===========Cosmetics==========
        self.bath_soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #============grocery============
        self.rice=IntVar()
        self.food_Oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #===========Cold Drinks=========
        self.cocacola=IntVar()
        self.sprite=IntVar()
        self.fanta=IntVar()
        self.pepsi=IntVar()
        self.juice=IntVar()
        self.sevenup=IntVar()
        #===Total product Price & Tax variable====
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #==========Customer========
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #================Customer Detail Frame==============
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=85,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=12,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=5)

#=====================Cosmetics Frame========#
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=2,y=180,width=340,height=417)

        Bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bath_txt=Entry(F2,width=10,textvariable=self.bath_soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_gell_lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_gell_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_loshan_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_loshan_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#=====================Grocery Frame========#
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=350,y=180,width=340,height=417)

        Rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Food_Oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Food_Oil_txt=Entry(F3,width=10,textvariable=self.food_Oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_wash_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#=====================Cold Drinks Frame========#
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=698,y=180,width=340,height=417)

        Cocacola_lbl=Label(F4,text="Cocacola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Cocacola_txt=Entry(F4,width=10,textvariable=self.cocacola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Fanta_lbl=Label(F4,text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Fanta_txt=Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Pepsi_lbl=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Pepsi_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Juice_lbl=Label(F4,text="Juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Juice_txt=Entry(F4,width=10,textvariable=self.juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Seven_Up_lbl=Label(F4,text="Seven Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Seven_Up_txt=Entry(F4,width=10,textvariable=self.sevenup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

 #=============Bill Area================

        F5 = Frame(self.root, bd=10, relief=GROOVE, )
        F5.place(x=1046, y=180, width=485, height=417)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient= VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

#===============Button Frame============
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=600,relwidth=1,height=150)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=3,sticky="w")
        m1_txt=Entry(F6,width=20,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=3)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=3,sticky="w")
        m2_txt=Entry(F6,width=20,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=3)

        m3_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=3,sticky="w")
        m3_txt=Entry(F6,width=20,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=3)

#===============Tax==============
        t1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=3,sticky="w")
        t1_txt=Entry(F6,width=20,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=3)

        t2_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=3,sticky="w")
        t2_txt=Entry(F6,width=20,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=3)

        t3_lbl=Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=3,sticky="w")
        t3_txt=Entry(F6,width=20,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=3)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=790,width=700,height=110)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,padx=45,pady=20).grid(row=0,column=0,padx=20,pady=12)
        genrate_bill=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,padx=40,pady=20).grid(row=0,column=1,padx=20,pady=12)
        clear=Button(btn_F,text="Clear",bg="cadetblue",command=self.clear_data,fg="white",bd=5,padx=40,pady=20).grid(row=0,column=2,padx=20,pady=12)
        exit= Button(btn_F, text="Exit", bg="cadetblue",command=self.Exit_app, fg="white",bd=5, padx=40, pady=20).grid(row=0, column=3,padx=20, pady=12)
        self.welcome_bill()

    def total(self):
        self.c_soap_price=self.bath_soap.get()*40
        self.c_face_cream_price=self.face_cream.get()*120
        self.c_face_wash_price=self.face_wash.get()*60
        self.c_spray_price=self.spray.get()*180
        self.c_gell_price=self.gell.get()*140
        self.c_loshan_price=self.loshan.get()*180
        self.total_cosmetic_price=float(
                                    self.c_soap_price+
                                    self.c_face_cream_price+
                                    self.c_face_wash_price+
                                    self.c_spray_price+
                                    self.c_gell_price+
                                    self.c_loshan_price
                                )
        self.cosmetic_price.set("Tk "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Tk "+str(self.c_tax))

        self.g_rice_price=self.rice.get() * 40
        self.g_food_oil_price=self.food_Oil.get() * 120
        self.g_daal_price=self.daal.get() * 60
        self.g_wheat_price=self.wheat.get() * 180
        self.g_sugar_price=self.sugar.get() * 140
        self.g_tea_price=self.tea.get() * 180

        self.total_grocery_price=float(
                                    self.g_rice_price +
                                    self.g_food_oil_price +
                                    self.g_daal_price +
                                    self.g_wheat_price +
                                    self.g_sugar_price +
                                    self.g_tea_price
                                    )
        self.grocery_price.set("Tk "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Tk "+str(self.g_tax))

        self.co_cocacola_price=self.cocacola.get() * 40
        self.co_sprite_price=self.sprite.get() * 120
        self.co_fanta_price=self.fanta.get() * 60
        self.co_pepsi_price=self.pepsi.get() * 180
        self.co_juice_price=self.juice.get() * 140
        self.co_sevenup_price=self.sevenup.get() * 180

        self.total_cold_drink_price=float(
                                        self.co_cocacola_price +
                                        self.co_sprite_price +
                                        self.co_fanta_price +
                                        self.co_pepsi_price +
                                        self.co_juice_price +
                                        self.co_sevenup_price
                                        )
        self.cold_drink_price.set("Tk "+str(self.total_cold_drink_price))
        self.cold_tax=round((self.total_cold_drink_price*0.05),2)
        self.cold_drink_tax.set("Tk "+str(self.cold_tax))

        self.Total_bill=float(self.total_cosmetic_price+
                            self.total_grocery_price+
                            self.total_cold_drink_price+
                            self.c_tax+
                            self.g_tax+
                            self.cold_tax
                            )
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t   Welcome to Roys Shop\n")
        self.txtarea.insert(END, f"\n  Bill Number :{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n  Customer Name :{self.c_name.get()}")
        self.txtarea.insert(END, f"\n  Phone Number :{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=======================================================")
        self.txtarea.insert(END, f"\n Products\t\t\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n=======================================================")


    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must.")
        elif self.cosmetic_price.get()=="Tk 0.0" and self.grocery_price.get()=="Tk 0.0" and self.cold_drink_price.get()=="Tk 0.0" :
            messagebox.showerror("Error", "No product purchased.")
        else:
            self.welcome_bill()
            #==========Cosmetics============
            if self.bath_soap.get()!=0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t\t\t{self.bath_soap.get()}\t\t{self.c_soap_price}")

            if self.face_cream.get()!=0:
                self.txtarea.insert(END, f"\n Face Cream\t\t\t\t{self.face_cream.get()}\t\t{self.c_face_cream_price}")

            if self.face_wash.get()!=0:
                self.txtarea.insert(END, f"\n Face Wash\t\t\t\t{self.face_wash.get()}\t\t{self.c_face_wash_price}")

            if self.spray.get()!=0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t\t\t{self.spray.get()}\t\t{self.c_spray_price}")

            if self.gell.get()!=0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t\t\t{self.gell.get()}\t\t{self.c_gell_price}")

            if self.loshan.get()!=0:
                self.txtarea.insert(END, f"\n Body Loshan\t\t\t\t{self.loshan.get()}\t\t{self.c_loshan_price}")

            #============Grocery==============
            if self.rice.get()!=0:
                self.txtarea.insert(END, f"\n Rice \t\t\t\t{self.rice.get()}\t\t{self.g_rice_price}")

            if self.food_Oil.get()!=0:
                self.txtarea.insert(END, f"\n Food Oil\t\t\t\t{self.food_Oil.get()}\t\t{self.g_food_oil_price}")

            if self.daal.get()!=0:
                self.txtarea.insert(END, f"\n Daal\t\t\t\t{self.daal.get()}\t\t{self.g_daal_price}")

            if self.wheat.get()!=0:
                self.txtarea.insert(END, f"\n Wheat\t\t\t\t{self.wheat.get()}\t\t{self.g_wheat_price}")

            if self.sugar.get()!=0:
                self.txtarea.insert(END, f"\n Sugar\t\t\t\t{self.sugar.get()}\t\t{self.g_sugar_price}")

            if self.tea.get()!=0:
                self.txtarea.insert(END, f"\n Tea\t\t\t\t{self.tea.get()}\t\t{self.g_tea_price}")

            #==============Cold Drinks===========
            if self.cocacola.get()!=0:
                self.txtarea.insert(END, f"\n Cocacola\t\t\t\t{self.cocacola.get()}\t\t{self.co_cocacola_price}")

            if self.sprite.get()!=0:
                self.txtarea.insert(END, f"\n Sprite\t\t\t\t{self.sprite.get()}\t\t{self.co_sprite_price}")

            if self.fanta.get()!=0:
                self.txtarea.insert(END, f"\n Fanta\t\t\t\t{self.fanta.get()}\t\t{self.co_fanta_price}")

            if self.pepsi.get()!=0:
                self.txtarea.insert(END, f"\n Pepsi\t\t\t\t{self.pepsi.get()}\t\t{self.co_pepsi_price}")

            if self.juice.get()!=0:
                self.txtarea.insert(END, f"\n Juice\t\t\t\t{self.juice.get()}\t\t{self.co_juice_price}")

            if self.sevenup.get()!=0:
                self.txtarea.insert(END, f"\n Seven Up\t\t\t\t{self.sevenup.get()}\t\t{self.co_sevenup_price}")

            self.txtarea.insert(END, f"\n-------------------------------------------------------")
            if self.cosmetic_tax.get()!="Tk 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Tk 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!= "Tk 0.0":
                self.txtarea.insert(END, f"\n Colod Drink Tax\t\t\t\t\t{self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill :\t\t\t\t\tTk {self.Total_bill}")
            self.txtarea.insert(END, f"\n-------------------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data= self.txtarea.get('1.0',END)
            f1=open("Customer_Bill_List/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data )
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfully.")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("Customer_Bill_List/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Customer_Bill_List/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to clear data?")
        if op > 0:
            #===========Cosmetics==========
            self.bath_soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            #============grocery============
            self.rice.set(0)
            self.food_Oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #===========Cold Drinks=========
            self.cocacola.set(0)
            self.sprite.set(0)
            self.fanta.set(0)
            self.pepsi.set(0)
            self.juice.set(0)
            self.sevenup.set(0)
            #===Total product Price & Tax variable====
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #==========Customer========
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()
