import os
import random
import tempfile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from product import *


class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        root.configure(bg="black")

        # COLOURS
        b = "black"
        w = "white"
        r = "red"

        # VARIABLES
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
        self.Tax = 100


        #Product Categories, SubCategories, Items, Prices getting from CSV file
        self.ListOfCategories = functionCategory()
        self.FoodItemsDictionary = {}

        #image1
        img1=Image.open("images/img1.jpg")
        img1=img1.resize((310,130),Image.Resampling.LANCZOS) 
        self.photoimg1=ImageTk.PhotoImage(img1)

        label_img1=Label(self.root, image=self.photoimg1, bg=b)
        label_img1.place(x=0,y=0, width=310, height=130)


        #image2
        img2=Image.open("images/img2.jpg")
        img2=img2.resize((310,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label_img2=Label(self.root, image=self.photoimg2, bg=b)
        label_img2.place(x=300,y=0, width=310, height=130)


        #image3
        img3=Image.open("images/img3.jpg")
        img3=img3.resize((310,130),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        label_img3=Label(self.root, image=self.photoimg3, bg=b)
        label_img3.place(x=620,y=0, width=310, height=130)

        #image4
        img4=Image.open("images/img2.jpg")
        img4=img4.resize((310,130),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        label_img4=Label(self.root, image=self.photoimg4, bg=b)
        label_img4.place(x=930,y=0, width=310, height=130)

        #image 5
        img5=Image.open("images/img1.jpg")
        img5=img5.resize((310,130),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        label_img5=Label(self.root, image=self.photoimg5, bg=b)
        label_img5.place(x=1240,y=0, width=310, height=130)

        #LabelTitle
        labelTitle=Label(self.root,text="B.TECH FAST FOOD CORNER", font=("times new roman", 35,"bold"),bg = b,fg= r)
        labelTitle.place(x=0, y=130, width=1530, height=45)

        #mainframe
        mainFrame=Frame(self.root, bd=5, relief=GROOVE, bg="black")
        mainFrame.place(x=0, y=175, width=1530, height=620)
        

        #Customer Label Frame
        customerFrame=LabelFrame(mainFrame, text="Customer", font=("times new roman", 12, "bold"), bg = b, fg = r)
        customerFrame.place(x=10, y=5, width=350, height=140)

        #Mobile Label and its entry in customer lablel
        self.labelMobile=Label(customerFrame, text="Mobile No.", font=("arial", 12, "bold"), bg = b, fg = w)
        self.labelMobile.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entryMobile=ttk.Entry(customerFrame, textvariable=self.cPhoneNumber, font=("arial", 10, "bold"), width=24)
        self.entryMobile.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        #Name Label and its entry in customer lablel
        self.labelName=Label(customerFrame, text="Name", font=("arial", 12, "bold"), bg = b, fg = w)
        self.labelName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entryName=ttk.Entry(customerFrame,textvariable=self.cName, font=("arial", 10, "bold"), width=24)
        self.entryName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #Email Label and its entry in customer lablel
        self.labelEmail=Label(customerFrame, text="E-mail", font=("arial", 12, "bold"), bg = "black", fg="white")
        self.labelEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entryEmail=ttk.Entry(customerFrame, textvariable=self.cEmail, font=("arial", 10, "bold"), width=24)
        self.entryEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)



        #PRODUCT LABEL FRAME
        productFrame=LabelFrame(mainFrame, text="Product", font=("times new roman", 12, "bold"), bg = b, fg = r)
        productFrame.place(x=370, y=5, width=650, height=140)

        #Category List
        #Category
        self.labelCategory=Label(productFrame, text="Select Categories", font=("arial", 12, "bold"), bg = b, fg = w)
        self.labelCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.comboCategory=ttk.Combobox(productFrame, font=("arial", 10, "bold"), value=self.ListOfCategories, width=24, state="readonly")
        self.comboCategory.current(0)
        self.comboCategory.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.comboCategory.bind("<<ComboboxSelected>>", self.functionProductAdd)


        #Product Name
        self.labelProductName=Label(productFrame, text="Food Item", font=("arial", 12, "bold"), bg = b, fg = w, bd=4)
        self.labelProductName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.comboProductName=ttk.Combobox(productFrame, textvariable=self.product,values=[""], font=("arial", 10, "bold"), width=24, state="readonly")
        self.comboProductName.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.comboProductName.bind("<<ComboboxSelected>>", self.functionPrice)


        #Price
        self.labelPrice=Label(productFrame, text="Price", font=("arial", 12, "bold"), bg = b, fg = w, bd=4)
        self.labelPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.comboPrice=ttk.Combobox(productFrame, font=("arial", 10, "bold"), width=24, state="readonly",textvariable=self.prices)
        self.comboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)


        #Quantity
        self.labelQuantity=Label(productFrame, text="Quantity", font=("arial", 12, "bold"), bg = b, fg = w, bd=4)
        self.labelQuantity.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.comboQuantity=ttk.Entry(productFrame, textvariable=self.quantity, font=("arial", 10, "bold"), width=24)
        self.comboQuantity.grid(row=1, column=3, sticky=W, padx=5, pady=2)
    
        #Add to Cart Button
        self.btnAddToCart=Button(productFrame, command=self.functionAddItem , text="Add To Cart", cursor="hand2", font=("arial", 15, "bold"), bg="red", fg="white")
        self.btnAddToCart.grid(row=2, column=3)

        #Middle Frame
        middleFrame=Frame(mainFrame, bd=10, bg=b)
        middleFrame.place(x = 10, y = 150, width = 1010, height = 340)

        #image12
        img12=Image.open("images/img12.jpg")
        img12=img12.resize((490,340),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        label_img12=Label(middleFrame, image=self.photoimg12)
        label_img12.place(x=0,y=0, width=490, height=340)


        #image21
        img21=Image.open("images/img21.jpg")
        img21=img21.resize((490,340),Image.Resampling.LANCZOS)
        self.photoimg21=ImageTk.PhotoImage(img21)

        label_img21=Label(middleFrame, image=self.photoimg21)
        label_img21.place(x=500,y=0, width=490, height=340)

        #Search 
        searchFrame= Frame(mainFrame, bd=2, bg = b)
        searchFrame.place(x=1030, y=15, width=500, height=40)

        self.labelBill=Label(searchFrame, text="Bill Number", font=("arial", 12, "bold"), bg = r, fg = w)
        self.labelBill.grid(row=0, column=0, sticky=W, padx=1)

        self.entrySearch=ttk.Entry(searchFrame,textvariable=self.searchBill, font=("arial", 10, "bold"), width=24)
        self.entrySearch.grid(row=0, column=1, sticky=W, padx=2)

        self.btnSearch=Button(searchFrame, text="Search", command=self.functionSearchBill, width=15, cursor="hand2", font=("arial", 10, "bold"), bg = r, fg = w)
        self.btnSearch.grid(row=0, column=2)

        # Right Frame Bill Area
        rightLabelFrame=LabelFrame(mainFrame, text="Bill Area", font=("times new roman", 12, "bold"), bg = b, fg = r)
        rightLabelFrame.place(x=1030, y=45, width=480, height=432)

        #Text Area and Scroll Bar
        scrollY=Scrollbar(rightLabelFrame, orient=VERTICAL)
        self.textarea=Text(rightLabelFrame, yscrollcommand=scrollY.set, bg = b, fg= w, font=("Courier New", 12, "bold"))
        scrollY.pack(side=RIGHT, fill=Y)
        # scrollY.config(command=self.textarea.yview)
        self.textarea.pack()

        #Bill counter LabelFrame
        bottomFrame=LabelFrame(mainFrame, text="Bill Counter", font=("times new roman", 12, "bold"), bg = b, fg = r)
        bottomFrame.place(x = 0, y = 480, width = 1520, height = 140)

        #Subtotl field in Bottom Frame
        self.subTotal=Label(bottomFrame, text="Subtotal", font=("arial", 12, "bold"), bg = b, fg = w, bd=4)
        self.subTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entrySubTotal=ttk.Entry(bottomFrame, font=("arial", 10, "bold"), width=24, textvariable=self.subtotal)
        self.entrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        #Tax field in Bottom Frame
        self.tax=Label(bottomFrame, text="Tax", font=("arial", 12, "bold"), bg = b, fg = w, bd=4)
        self.tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entryTax=ttk.Entry(bottomFrame, font=("arial", 10, "bold"), width=24, textvariable=self.taxInput)
        self.entryTax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        #Amount Total field in Bottom Frame
        self.total=Label(bottomFrame, text="Total Amount", font=("arial", 12, "bold"), bg = b, fg = w, bd=4)
        self.total.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entryTotal=ttk.Entry(bottomFrame, font=("arial", 10, "bold"), width=24, textvariable=self.Total)
        self.entryTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)


        #Fames for buttons in Bottom Frame

        btnFrame= Frame(bottomFrame, bd=2, bg = b)
        btnFrame.place(x=320, y=0)

        #Generate Bill Button
        self.btngenerateBill=Button(btnFrame, text="Generate Bill", command=self.functionGenerateBill, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg = r, fg = w)
        self.btngenerateBill.grid(row=0, column=0)

        #Save Bill Button
        self.btnSaveBill=Button(btnFrame, text="Save Bill", command=self.functionSaveBill, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg = r, fg = w)
        self.btnSaveBill.grid(row=0, column=1)

        #Print Button
        self.btnPrint=Button(btnFrame, text="Print", command=self.functionPrintBill, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg = r, fg= w)
        self.btnPrint.grid(row=0, column=2)

        #Clear Button
        self.btnClear=Button(btnFrame, text="Clear", command=self.functionClear, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg=r, fg= w)
        self.btnClear.grid(row=0, column=3)

        #Add More Items
        self.btnAddMoreItems=Button(btnFrame, text="Add More", command=self.functionToAddMoreItems, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg = r, fg = w)
        self.btnAddMoreItems.grid(row=0, column=4)
 
        #Exit Button
        self.btnExit=Button(btnFrame, text="Exit", command=self.root.destroy, height=2, width=15, cursor="hand2", font=("arial", 15, "bold"), bg = r, fg = w)
        self.btnExit.grid(row=0, column=5)
        self.welcome()
    
    # ========================================================Function Declaration =============================================================
    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END,"B.TECH FOOD CORNER")
        self.textarea.insert(END, f"\n Bill Number: {self.billNO.get()}")
        self.textarea.insert(END, f"\n Customer Name: {self.cName.get()}")
        self.textarea.insert(END, f"\n Phone Number: {self.cPhoneNumber.get()}")
        self.textarea.insert(END, f"\n E-mail: {self.cEmail.get()}")

        self.textarea.insert(END, f"\n{'='*45}\n")
        self.textarea.insert(END, f"{'Food Items':22s}{' ':3s}{'Plate(s)':8s}{' ':3s}{'Price(Rs)':9s}")
        self.textarea.insert(END, f"\n{'-'*45}\n")



        self.l = []
    def functionAddItem(self):
        self.n = self.prices.get()
        self.m = self.quantity.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error", "Please Select Product")
        else:
            self.textarea.insert(END, f"\n{self.product.get():22s}{' ':3s}{self.quantity.get():^8d}{' ':3s}{self.m:>9d}")

            self.subtotal.set(str('RS.%.2f'%(sum(self.l))))
            self.taxInput.set(str('RS.%.2f'%((((sum(self.l))-(self.prices.get()))*self.Tax)/100)))
            self.Total.set(str('RS.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*self.Tax)/100)))))
    
    def functionGenerateBill(self):
        if self.cPhoneNumber.get().isnumeric() == False or len(self.cPhoneNumber.get())!=10:
            messagebox.showerror("Phone Number", "Please Fill Correct Number")

        #     messagebox.showerror("Name", "Please Fill a Correct Name")

        elif self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")

        
        else:
            text = self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, f"{'='*45}")
            self.textarea.insert(END, f"\n{'Sub Amount':29s}{' '*3}{self.subtotal.get():>13s}")
            self.textarea.insert(END, f"\n{'Tax Amount':29s}{' '*3}{self.taxInput.get():>13s}")
            self.textarea.insert(END, f"\n{'Total Amount':29s}{' '*3}{self.Total.get():>13s}")
            self.textarea.insert(END, f"\n{'='*45}\n")
    
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

    #FUNCTION TO ADD PRODUCT
    def functionProductAdd(self, events=""):
            CategorySelected = self.comboCategory.get()
            self.FoodItemsDictionary = functionFoodItems(CategorySelected)
            self.comboProductName.config(values=list(self.FoodItemsDictionary.keys()))
            self.comboProductName.current(0)
            ProductName = self.comboProductName.get()
            self.comboPrice.config(values=self.FoodItemsDictionary[ProductName])
            self.quantity.set(1)
            self.comboPrice.current(0)

    #FUNCTION TO ADD PRICE
    def functionPrice(self, events=""):
        ProductName = self.comboProductName.get()
        self.comboPrice.config(values=self.FoodItemsDictionary[ProductName])
        self.quantity.set(1)
        self.comboPrice.current(0)
    
    #FUNCTION TO ADD MORE ITEMS
    def functionToAddMoreItems(self):
        top = Toplevel()
        top.title("Add More Items")
        top.configure(bg="black")
        top.geometry("200x230")


        #Select a Category to add 
        self.labelAddCategory=Label(top, text="Add Categories", font=("arial", 12, "bold"), bg = "black", fg = "white")
        self.labelAddCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.comboAddCategory=ttk.Combobox(top, font=("arial", 10, "bold"), value=self.ListOfCategories, width=24)
        self.comboAddCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        #Select Food Item to Add
        self.labelAddFoodItems=Label(top, text="Add Food Items", font=("arial", 12, "bold"), bg = "black", fg = "white", bd=4)
        self.labelAddFoodItems.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.entryAddFoodItems=ttk.Entry(top, font=("arial", 10, "bold"), width=26)
        self.entryAddFoodItems.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        #Select Price to Add
        self.labelAddPrice=Label(top, text="Add Price", font=("arial", 12, "bold"), bg = "black", fg = "white", bd=4)
        self.labelAddPrice.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.entryAddPrice=ttk.Entry(top, font=("arial", 10, "bold"), width=26)
        self.entryAddPrice.grid(row=5, column=0, sticky=W, padx=5, pady=2)

        #Button to Add Data to CSV
        self.btnAddToCart=Button(top, text="Add", command=self.GetItems, cursor="hand2", font=("arial", 10, "bold"), bg="red", fg="white")
        self.btnAddToCart.grid(row=6, column=0)

    def GetItems(self):
        if self.comboAddCategory.get() == "" or self.entryAddFoodItems.get() == "" or self.entryAddPrice.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields")
        
        self.ListOfNewItems = []
        self.ListOfNewItems.append(self.comboAddCategory.get().capitalize())
        self.ListOfNewItems.append(self.entryAddFoodItems.get().capitalize())
        self.ListOfNewItems.append(self.entryAddPrice.get().capitalize())

        #Call function AddtoCSV in product.py
        AddItemtoCSV(self.ListOfNewItems)
        self.ListOfCategories = functionCategory()
        self.comboCategory.config(values=self.ListOfCategories)
        self.comboAddCategory.config(values=self.ListOfCategories)
        self.comboAddCategory.set('')
        self.entryAddFoodItems.delete(0, END)
        self.entryAddPrice.delete(0, END)

        



        
        


        




if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
