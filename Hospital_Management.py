from tkinter import *
import random
import time
import datetime
from tkinter import messagebox 
import mysql.connector
from tkinter import ttk



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        lbtitle=Label(self.root,relief=RIDGE,bd=20,text="HOSPITAL MANAGEMENT SYSTEM",fg="RED",bg="white",font=("times new roman",30,"bold"))
        lbtitle.pack(side=TOP,fill=X)
        
        #=====================================DataFrame===========================================
        Dataframe=Label(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=95,width=1275,height=300)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,
                                 padx=10,font=("ariel",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=880,height=250)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,
                                 padx=10,font=("ariel",12,"bold"),text="Prescription")
        DataframeRight.place(x=890,y=4,width=340,height=250)
        
        #=====================================Button Frames=========================================
        
        
        Buttonframe=Label(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=395,width=1275,height=70)
        
        #=====================================Details Frames========================================
        
        
        Detailsframe=Label(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=469,width=1275,height=190)
        
        #==================================DataframeLeft========================================

        lbNameTablet=Label(DataframeLeft,text="Names OF Tablet",font=("ariel",12,"bold"),padx=2,pady=0)
        lbNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,font=("ariel",9,"bold"),width=35)

        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderail","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,text="Reference No.",font=("ariel",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lbldose=Label(DataframeLeft,text="Dose",font=("ariel",12,"bold"),padx=5,pady=4)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtdose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,text="No. of Tablets::",font=("ariel",12,"bold"),padx=5,pady=6)
        lblNoOftablets.grid(row=2,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtNoOftablets.grid(row=2,column=1)
        
        lbllot=Label(DataframeLeft,text="Lot:",font=("ariel",12,"bold"),padx=5,pady=6)
        lbllot.grid(row=3,column=0,sticky=W)
        txtlot=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtlot.grid(row=3,column=1)

        lblissueDate=Label(DataframeLeft,text="Issue Date:",font=("ariel",12,"bold"),padx=5,pady=6)
        lblissueDate.grid(row=4,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtissueDate.grid(row=4,column=1)

        lblExpDate=Label(DataframeLeft,text="Exp Date:",font=("ariel",12,"bold"),padx=5,pady=6)
        lblExpDate.grid(row=5,column=0,sticky=W)
        txlExpDate=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txlExpDate.grid(row=5,column=1)

        lblDailyDose=Label(DataframeLeft,text="Daily Dose:",font=("ariel",12,"bold"),padx=5,pady=0)
        lblDailyDose.grid(row=6,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtDailyDose.grid(row=6,column=1)

        
#=============================Column 2==============================================================================
        lblFurtherInfo=Label(DataframeLeft,text="Further Info:",font=("ariel",12,"bold"),padx=5)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,text="Blood Pressure:",font=("ariel",12,"bold"),padx=5)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,text="Storage Advice:",font=("ariel",12,"bold"),padx=5)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,text="Medication:",font=("ariel",12,"bold"),padx=5)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientID=Label(DataframeLeft,text="Patient ID:",font=("ariel",12,"bold"),padx=5)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtPatientID.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,text="NHS Number:",font=("ariel",12,"bold"),padx=5)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblNhsNumber=Label(DataframeLeft,text="NHS Number:",font=("ariel",12,"bold"),padx=5)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,text="Patient Name:",font=("ariel",12,"bold"),padx=5)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("ariel",10,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)


        #==============================DataframeRight========================================================
        self.txtPrescription=Text(DataframeRight,font=("ariel",10,"bold"),width=27,height=13,padx=55,pady=0)
        self.txtPrescription.grid(row=0,column=0) 


        #===================================Buttons==========================================================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("Arial", 10, "bold"), width=25, height=1)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("Arial", 10, "bold"), width=25, height=1)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("Arial", 10, "bold"), width=25, height=1)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("Arial", 10, "bold"), width=25, height=1)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("Arial", 10, "bold"), width=25, height=1)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("Arial", 10, "bold"), width=25, height=1)
        btnExit.grid(row=0, column=5)


        #==========================================================Table=========================================================================================
        #==========================================================Scroll========================================================================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                                                              "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column("nameoftablets",width=102)
        self.hospital_table.column("ref",width=102)
        self.hospital_table.column("dose",width=102)
        self.hospital_table.column("nooftablets",width=102)
        self.hospital_table.column("lot",width=102)
        self.hospital_table.column("issuedate",width=102)
        self.hospital_table.column("expdate",width=102)
        self.hospital_table.column("dailydose",width=102)
        self.hospital_table.column("storage",width=102)
        self.hospital_table.column("nhsnumber",width=102)
        self.hospital_table.column("pname",width=178)

        self.hospital_table.pack(fill=BOTH,expand=1)





        


        



        


root=Tk()
ob=Hospital(root)
root.mainloop()
 