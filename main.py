from PIL import Image, ImageTk
from tkinter import messagebox
import tempfile
from tkinter import *
from tkinter import ttk
import random
import os




class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # ++++++++++++++++++++++ Variables ++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.cName = StringVar()
        self.cPhoneNumber = StringVar()
        self.billNO = StringVar()
        z=random.randint(1000, 10000)
        self.billNO.set(z)
        self.cEmail = StringVar()
        self.searchBill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()
        self.quantity =  IntVar()
        self.subtotal=StringVar()
        self.taxInput = StringVar()
        self.Total = StringVar()
        self.Tax = 1

        #Product Categories list
        self.category = ["Select Option", "Clothing", "Life Style"]

        #Sub Category Clothing
        self.subCategoryClothing = ["Pant", "T-shirt", "Shirt"]

        self.pant = ["Levis", "Mufti", "Spykar"]
        self.levis = 5000
        self.Mufti = 2000
        self.spykar = 1000

        self.tshirt = ["Polo", "Roadstar", "Jack&Jones"]
        self.polo = 1500
        self.roadstar = 1800
        self.jackjones = 1700

        self.shirt = ["Peter England", "Louis Phillips", "Park Avenue"]
        self.peter = 2100
        self.louisPhillps = 2700
        self.parkAvenue = 1740

        #Sub Category Life Style
        self.subCategoryLifeStyle = ["Bath Soap", "Face Cream", "Hair Oil"]

        self.bathSoap = ["Life Boy", "Dettol", "Dove"]
        self.lifeboy = 20
        self.dettol = 20
        self.Dove = 20
        
        self.faceCream = ["Glow & Lovely", "Himalaya", "Cold Cream"]
        self.glowLovely = 25
        self.Himalaya = 30
        self.coldCream = 50

        self.hairOil = ["Amla", "Parachute", "Jasmine"]
        self.Amla = 20
        self.Parachute = 20
        self.Jasmine = 20
        

        #image1
        img1=Image.open("images/b1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS) 
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img1=Label(self.root, image=self.photoimg1)
        label_img1.place(x=0,y=0, width=500, height=130)


        #image2
        img2=Image.open("images/girls.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_img2=Label(self.root, image=self.photoimg2)
        label_img2.place(x=500,y=0, width=500, height=130)


        #image3
        img3=Image.open("images/girl1.jpg")
        img3=img3.resize((520,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label_img3=Label(self.root, image=self.photoimg3)
        label_img3.place(x=1000,y=0, width=520, height=130)


        #LabelTitle
        labelTitle=Label(self.root,text="BILLING SOFTWARE USING PYTHON", font=("times new roman", 35,"bold"),bg="white",fg="red")
        labelTitle.place(x=0, y=130, width=1530, height=45)

        #mainframe
        mainFrame=Frame(self.root, bd=5, relief=GROOVE, bg="white")
        mainFrame.place(x=0, y=175, width=1530, height=620)
        

        #Customer Label Frame
        customerFrame=LabelFrame(mainFrame, text="Customer", font=("times new roman", 12, "bold"), bg = "white", fg="red")
        customerFrame.place(x=10, y=5, width=350, height=140)

        #Mobile Label and its entry in customer lablel
        self.labelMobile=Label(customerFrame, text="Mobile No.", font=("arial", 12, "bold"), bg = "white")
        self.labelMobile.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entryMobile=ttk.Entry(customerFrame, textvariable=self.cPhoneNumber, font=("arial", 10, "bold"), width=24)
        self.entryMobile.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        #Name Label and its entry in customer lablel
        self.labelName=Label(customerFrame, text="Name", font=("arial", 12, "bold"), bg = "white")
        self.labelName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entryName=ttk.Entry(customerFrame,textvariable=self.cName, font=("arial", 10, "bold"), width=24)
        self.entryName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #Email Label and its entry in customer lablel
        self.labelEmail=Label(customerFrame, text="E-mail", font=("arial", 12, "bold"), bg = "white")
        self.labelEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entryEmail=ttk.Entry(customerFrame, textvariable=self.cEmail, font=("arial", 10, "bold"), width=24)
        self.entryEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)





        #Product Label Frame
        productFrame=LabelFrame(mainFrame, text="Product", font=("times new roman", 12, "bold"), bg = "white", fg="red")
        productFrame.place(x=370, y=5, width=650, height=140)


        #Category
        self.labelCategory=Label(productFrame, text="Select Categories", font=("arial", 12, "bold"), bg = "white")
        self.labelCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.comboCategory=ttk.Combobox(productFrame, font=("arial", 10, "bold"), value=self.category, width=24, state="readonly")
        self.comboCategory.current(0)
        self.comboCategory.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.comboCategory.bind("<<ComboboxSelected>>", self.functionCategories)


        #Sub Category
        self.labelSubCategory=Label(productFrame, text="SubCategories", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.labelSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.comboSubCategory=ttk.Combobox(productFrame,value=[""], font=("arial", 10, "bold"), width=24, state="readonly")
        self.comboSubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.comboSubCategory.bind("<<ComboboxSelected>>", self.functionProductAdd)


        #Product Name
        self.labelProductName=Label(productFrame, text="Product Name", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.labelProductName.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.comboProductName=ttk.Combobox(productFrame, textvariable=self.product, font=("arial", 10, "bold"), width=24, state="readonly")
        self.comboProductName.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.comboProductName.bind("<<ComboboxSelected>>", self.functionPrice)


        #Price
        self.labelPrice=Label(productFrame, text="Price", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.labelPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.comboPrice=ttk.Combobox(productFrame, font=("arial", 10, "bold"), width=24, state="readonly",textvariable=self.prices)
        self.comboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)


        #Quantity
        self.labelQuantity=Label(productFrame, text="Quantity", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.labelQuantity.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.comboQuantity=ttk.Entry(productFrame, textvariable=self.quantity, font=("arial", 10, "bold"), width=24)
        self.comboQuantity.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #Middle Frame
        middleFrame=Frame(mainFrame, bd=10)
        middleFrame.place(x = 10, y = 150, width = 1010, height = 340)

        #image12
        img12=Image.open("images/good.jpg")
        img12=img12.resize((490,340),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        label_img12=Label(middleFrame, image=self.photoimg12)
        label_img12.place(x=0,y=0, width=490, height=340)


        #image21
        img21=Image.open("images/mall.jpg")
        img21=img21.resize((490,340),Image.ANTIALIAS)
        self.photoimg21=ImageTk.PhotoImage(img21)

        label_img21=Label(middleFrame, image=self.photoimg21)
        label_img21.place(x=500,y=0, width=490, height=340)

        #Search 
        searchFrame= Frame(mainFrame, bd=2, bg="white")
        searchFrame.place(x=1030, y=15, width=500, height=40)

        self.labelBill=Label(searchFrame, text="Bill Number", font=("arial", 12, "bold"), bg = "red", fg = "white")
        self.labelBill.grid(row=0, column=0, sticky=W, padx=1)

        self.entrySearch=ttk.Entry(searchFrame,textvariable=self.searchBill, font=("arial", 10, "bold"), width=24)
        self.entrySearch.grid(row=0, column=1, sticky=W, padx=2)

        self.btnSearch=Button(searchFrame, text="Search", command=self.functionSearchBill, width=15, cursor="hand2", font=("arial", 10, "bold"), bg="orangered", fg="white")
        self.btnSearch.grid(row=0, column=2)

        


        # Right Frame Bill Area
        rightLabelFrame=LabelFrame(mainFrame, text="Bill Area", font=("times new roman", 12, "bold"), bg = "white", fg="red")
        rightLabelFrame.place(x=1030, y=45, width=480, height=432)

        #Text Area and Scroll Bar
        scrollY=Scrollbar(rightLabelFrame, orient=VERTICAL)
        self.textarea=Text(rightLabelFrame, yscrollcommand=scrollY.set, bg="white", fg="blue", font=("times new roman", 12, "bold"))
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #Bill counter LabelFrame
        bottomFrame=LabelFrame(mainFrame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white", fg="red")
        bottomFrame.place(x = 0, y = 480, width = 1520, height = 140)

        #Subtotl field in Bottom Frame
        self.subTotal=Label(bottomFrame, text="Subtotal", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.subTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entrySubTotal=ttk.Entry(bottomFrame, font=("arial", 10, "bold"), width=24, textvariable=self.subtotal)
        self.entrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        #Tax field in Bottom Frame
        self.tax=Label(bottomFrame, text="Tax", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entryTax=ttk.Entry(bottomFrame, font=("arial", 10, "bold"), width=24, textvariable=self.taxInput)
        self.entryTax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #Amount Total field in Bottom Frame
        self.total=Label(bottomFrame, text="Total Amount", font=("arial", 12, "bold"), bg = "white", bd=4)
        self.total.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entryTotal=ttk.Entry(bottomFrame, font=("arial", 10, "bold"), width=24, textvariable=self.Total)
        self.entryTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)


        #Fames for buttons in Bottom Frame

        btnFrame= Frame(bottomFrame, bd=2, bg="white")
        btnFrame.place(x=320, y=0)

        #Add to cart Button
        self.btnAddToCart=Button(btnFrame, command=self.functionAddItem , text="Add To Cart", height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg="orangered", fg="white")
        self.btnAddToCart.grid(row=0, column=0)

        #Generate Bill Button
        self.btngenerateBill=Button(btnFrame, text="Generate Bill", command=self.functionGenerateBill, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg="orangered", fg="white")
        self.btngenerateBill.grid(row=0, column=1)

        #Save Bill Button
        self.btnSaveBill=Button(btnFrame, text="Save Bill", command=self.functionSaveBill, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg="orangered", fg="white")
        self.btnSaveBill.grid(row=0, column=2)

        #Print Button
        self.btnPrint=Button(btnFrame, text="Print", command=self.functionPrintBill, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg="orangered", fg="white")
        self.btnPrint.grid(row=0, column=3)

        #Clear Button
        self.btnClear=Button(btnFrame, text="Clear", command=self.functionClear, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg="orangered", fg="white")
        self.btnClear.grid(row=0, column=4)

        #Exit Button
        self.btnExit=Button(btnFrame, text="Exit", command=self.root.destroy, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg="orangered", fg="white")
        self.btnExit.grid(row=0, column=5)
        self.welcome()
    
        self.l = []
    # ========================================================Function Declaration =============================================================
    def functionAddItem(self):
        self.n = self.prices.get()
        self.m = self.quantity.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error! Please Select Product")

        else:
            self.textarea.insert(END, f"\n {self.product.get()}\t\t\t {self.quantity.get()}\t\t\t{self.m}")
            self.subtotal.set(str('RS.%.2f'%(sum(self.l))))
            self.taxInput.set(str('RS.%.2f'%((((sum(self.l))-(self.prices.get()))*self.Tax)/100)))
            self.Total.set(str('RS.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*self.Tax)/100)))))
    
    def functionGenerateBill(self):
        if self.product.get()=="":
            messagebox.showerror("Error! Please Add to Cart Product")
        
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, "\n==================================================\n")
            self.textarea.insert(END, f"\n Sub Amount:\t\t\t{self.subtotal.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t\t{self.taxInput.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.Total.get()}")
            self.textarea.insert(END, "\n==================================================\n")
    
    def functionSaveBill(self):
        op = messagebox.askyesno("Save Bill", "Do You Want to Save the Bill?")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            f1=open('Bills/' + str(self.billNO.get()) + ".txt", "w")
            f1.write(self.bill_data)
            messagebox.showinfo("Saved,", f"Bill No {self.billNO.get()} Saved Successfull!")
            f1.close()
            
    
    def functionPrintBill(self):
        q = self.textarea.get(1.0, "end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename, 'w').write(q)
        os.startfile(filename, "Print")

    
    def functionSearchBill(self):
        found="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.searchBill.get():
                f1 = open(f"Bills/{i}", 'r')
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                found = "yes"
                if found == "no":
                    messagebox.showerror("Error", "Invalid Bill Number")
    
    def functionClear(self):
        self.textarea.delete(1.0, END)
        self.cName.set("")
        self.cPhoneNumber.set("")
        self.cEmail.set("")
        x = random.randint(1000, 9999)
        self.billNO.set(x)
        self.searchBill.set("")
        self.product.set("")
        self.prices.set(0)
        self.quantity.set(0)
        self.l=[0]
        self.Total.set("")
        self.subtotal.set("")
        self.taxInput.set("")
        self.welcome()






    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END,"\tWelcome Binary Dose Mini Mall")
        self.textarea.insert(END, f"\n Bill Number:{self.billNO.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.cName.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.cPhoneNumber.get()}")
        self.textarea.insert(END, f"\n E-mail:{self.cEmail.get()}")

        self.textarea.insert(END, "\n==================================================\n")
        self.textarea.insert(END, f"Products\t\t\tQuantity\t\t\tPrice")
        self.textarea.insert(END, "\n==================================================\n")

    def functionCategories(self, events=""):
        if self.comboCategory.get() == "Clothing":
            self.comboSubCategory.config(value=self.subCategoryClothing)
            self.comboSubCategory.current(0)
        
        if self.comboCategory.get() == "Life Style":
            self.comboSubCategory.config(value=self.subCategoryLifeStyle)
            self.comboSubCategory.current(0)
    
    def functionProductAdd(self, events=""):

        #Clohting
        if self.comboSubCategory.get() == "Pant":
            self.comboProductName.config(value=self.pant)
            self.comboProductName.current(0)

        if self.comboSubCategory.get() == "T-shirt":
            self.comboProductName.config(value=self.tshirt)
            self.comboProductName.current(0)

        if self.comboSubCategory.get() == "Shirt":
            self.comboProductName.config(value=self.shirt)
            self.comboProductName.current(0)
        
        #Life Style
        if self.comboSubCategory.get() == "Bath Soap":
            self.comboProductName.config(value=self.bathSoap)
            self.comboProductName.current(0)
        
        if self.comboSubCategory.get() == "Face Cream":
            self.comboProductName.config(value=self.faceCream)
            self.comboProductName.current(0)
        
        if self.comboSubCategory.get() == "Hair Oil":
            self.comboProductName.config(value=self.hairOil)
            self.comboProductName.current(0)
        

    
    def functionPrice(self, events=""):
        #Pant
        if self.comboProductName.get()=="Levis":
            self.comboPrice.config(value=self.levis)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Mufti":
            self.comboPrice.config(value=self.Mufti)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Spykar":
            self.comboPrice.config(value=self.spykar)
            self.comboPrice.current(0)
            self.quantity.set(1)
    
        #Shirt
        if self.comboProductName.get()=="Peter England":
            self.comboPrice.config(value=self.peter)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Louis Phillips":
            self.comboPrice.config(value=self.louisPhillps)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()== "Park Avenue":
            self.comboPrice.config(value=self.parkAvenue)
            self.comboPrice.current(0)
            self.quantity.set(1)
        
        #T-Shirt
        if self.comboProductName.get()=="Polo":
            self.comboPrice.config(value=self.polo)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Roadstar":
            self.comboPrice.config(value=self.roadstar)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Jack&Jones":
            self.comboPrice.config(value=self.jackjones)
            self.comboPrice.current(0)
            self.quantity.set(1)
    
        #Hair Oil
        if self.comboProductName.get()=="Amla":
            self.comboPrice.config(value=self.Amla)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Parachute":
            self.comboPrice.config(value=self.Parachute)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Jasmine":
            self.comboPrice.config(value=self.Jasmine)
            self.comboPrice.current(0)
            self.quantity.set(1)
        
        #Bath Soap
        if self.comboProductName.get()=="Life Boy":
            self.comboPrice.config(value=self.lifeboy)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Dettol":
            self.comboPrice.config(value=self.dettol)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Dove":
            self.comboPrice.config(value=self.Dove)
            self.comboPrice.current(0)
            self.quantity.set(1)

        #Face Cream
        if self.comboProductName.get()=="Glow & Lovely":
            self.comboPrice.config(value=self.glowLovely)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Himalaya":
            self.comboPrice.config(value=self.Himalaya)
            self.comboPrice.current(0)
            self.quantity.set(1)

        if self.comboProductName.get()=="Cold Cream":
            self.comboPrice.config(value=self.coldCream)
            self.comboPrice.current(0)
            self.quantity.set(1)
        

        
        


        




if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()