#FEES FILE
import csv,os
def append():
    f=open("Fees.csv","a",newline="")
    csvw=csv.writer(f)
    n=int(input("Enter the value for n"))
    for x in range(n):
        mcode=int(input("Enter the member code"))
        dd=int(input("Whic day??(in digit)"))
        mm=int(input("which month(in digit)"))
        yy=int(input("which year??"))
        maxdays=0
        if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
            maxdays=31
        elif mm==4 or mm==6 or mm==9 or mm==11:
            maxdays=30
        elif mm==2:
            if yy%4==0 and yy%100!=0 or yy%400==0:
                maxdays=29
            else:
                maxdays=28
        if dd>=1 and dd<=maxdays:
            print("Valid date")
        else:
            print("Invalid date")
        dofs=str(dd) + '/' + str(mm) + '/'+str(yy)
        mfee=int(input("Enter the membership fee"))
        fees=10000+mfee+2000
        if fees>12000 and fees<16000:
            print("fee is applicable")
        else:
            print("fee is not applicable")
        rec=[mcode,dofs,fees]
        csvw.writerow(rec)
    f.close()
def display():
    f=open("fees file.CSV","r")
    stulist=csv.reader(f)
    for stu in stulist:
        print(stu[0],stu[1],stu[2], sep="\t")
    f.close()
def searchrecord():
    def searchmcode():
        f=open("fees file.CSV","r")
        stulist=csv.reader(f)
        mcode=int(input("Enter the value for the member code to be searched=="))
        found=0
        for stu in stulist:
            if mcode==int(stu[0]):
                print(stu[0],stu[1],stu[2],sep="\t")
                found=1
                break
        f.close()
        if found==0:
            print(mcode,"not found in the file")
    def searchdate():
         f=open("fees file.CSV","r")
         stulist=csv.reader(f)
         dd=int(input("Whic day??(in digit)"))
         mm=int(input("which month(in digit)"))
         yy=int(input("whic year??"))
         dofs=str(dd)+'/'+str(mm)+'/'+str(yy)
         found=0
         for stu in stulist:
             if dofs==stu[1]:
                 print(stu[0],stu[1],stu[2],sep="\t")
                 found=1
                 break
         f.close()
         if found==0:
             print(dofs,", such a date is not there. Pls Try again later.")
    def searchfees():
         f=open("fees file.CSV","r")
         stulist=csv.reader(f)
         fees=int(input("Enter the value of the fees to be searched"))
         found=0
         for stu in stulist:
             if fees==int(stu[2]):
                 print(stu[0],stu[1],stu[2],sep="\t")
                 found=1
                 break
         f.close()
         if found==0:
             print(fees,"not found in the file")
    while True:
         print("***Search menu***")
         print("Search Member code--1")
         print("Search Date of Submission--2")
         print("Search fees--3")
         ch=int(input("enter the digit corresponding to each statment for which you want to search--- "))
         if ch==1:
             searchmcode()
         elif ch==2:
             searchdate()
         elif ch==3:
             searchfees()
             break
def editrecord():
    def editdsob():
        frobj=open("fees file.CSV")
        fwobj=open("fees file2.CSV",'w',newline='')
        stulist=csv.reader(frobj)
        csvw=csv.writer(fwobj)
        print("Enter the date which you have inputted in file:--")
        dd1=int(input("Whic day?(in digit)"))
        mm1=int(input("which month(in digit)"))
        yy1=int(input("whic year?"))
        da1=str(dd1)+'/'+str(mm1)+'/'+str(yy1)
        print("the date you want to replace with the date you mentioned before:--")
        dd2=int(input("your new day?(in digit)"))
        mm2=int(input("month(in digit)"))
        yy2=int(input("which year?"))
        da2=str(dd2)+'/'+str(mm2)+'/'+str(yy2)
        for stu in stulist:
            if stu[1]==da1:
                stu[1]=da2
            csvw.writerow(stu)
        frobj.close()
        fwobj.close()
        os.remove("fees file.CSV")
        os.rename("fees file2.CSV","fees file.CSV")
    def editfees():
        frobj=open("fees file.CSV")
        fwobj=open("fees file2.CSV",'w',newline='')
        stulist=csv.reader(frobj)
        csvw=csv.writer(fwobj)
        f1=input("Enter the fees which has been inputted:")
        f2=input("Enter the new fees:")
        for stu in stulist:
            if stu[2]==f1:
                stu[2]=f2
            csvw.writerow(stu)
        frobj.close()
        fwobj.close()
        os.remove("fees file.CSV")
        os.rename("fees file2.CSV","fees file.CSV")
    while True:
         print("***Search menu***")
         print("edit the date of submission???--1")
         print("edit fees???--2")
         ch=int(input("enter the digit corresponding to each statment for which you want to edit--- "))
         if ch==1:
             editdsob()
         elif ch==2:
             editfees()
             break
def delrec():
    frobj=open("fees file.CSV")
    fwobj=open("fees file2.CSV",'w',newline='')
    csvw=csv.writer(fwobj)
    stulist=csv.reader(frobj)
    mcode=int(input("Enter the code to delete that particular record=="))
    found=0
    for stu in stulist:
        if mcode==int(stu[0]):
            found=1
        else:
            csvw.writerow(stu)
    frobj.close()
    fwobj.close()
    if found==1:
        print("Record deleted from the file")
    else:
        print(mcode,"Not found in the file")
    os.remove("fees file.CSV")
    os.rename("fees file2.CSV","fees file.CSV")
while True:
    print("1.To append the record")
    print("2.Display the record")
    print("3.To search the record")
    print("4.To edit the record")
    print("5.To delete the record")
    ch=int(input("Enter the choice="))
    if ch==1:
        append()
    if ch==2:
        display()
    if ch==3:
        searchrecord()
    if ch==4:
        editrecord()
    if ch==5:
        delrec()
        break
