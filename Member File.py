#MEMBER FILE
import os,csv
def addRecords():
    f=open("Member.csv",'a',newline='')
    csvw=csv.writer(f)
    n=int(input("Enter the value of n:"))
    for k in range(n):
        na=input("Member Name:")
        for k in na:
            if not k.isalpha():
                print("Invalid Name")
                break
            else:
                break
        co=int(input("Member Code:"))
        dd=int(input("Day"))
        mm=int(input("Month"))
        yy=int(input("Year"))
        da=str(dd)+'/'+str(mm)+'/'+str(yy)
        maxdays=0
        if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10:
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
            print("Date:",da)
        else:
            print("Invalid date")
        ad=input("Email address:")
        ph=int(input("Phone Number:"))
        f1=int(input("Enter 1 if facility 1 is being availed:"))
        f2=int(input("Enter 1 if facility 2 is being availed:"))
        f3=int(input("Enter 1 if facility 3 is being availed:"))
        if f1!=1 and f2!=1 and f3!=1:
            print("No facility availed")
        rec=[na,co,da,ad,ph,f1,f2,f3]
        csvw.writerow(rec)
    f.close()

def displayRecords():
    '''f=open("Member.csv","r")
    stulist=csv.reader(f)
    for stu in stulist:
        print(stu[0],stu[1],stu[2], sep="\t")'''
    f=open("Member.csv","r")
    csvr=csv.reader(f)
    for k in csvr:
        print(k[0],k[1],k[2],k[3],k[4],sep='\t')
    f.close()
    
def searchRecords():
    def searchName():
        f=open("Member.csv")
        csvr=csv.reader(f)
        co1=input("Enter the name to be searched:")
        found=0
        for k in csvr:
            if k[0]==co1:
                found=1
                break
        if found:
            print("Name found")
            print(k)
        else:
            print("Name not found")
        f.close()
        
    def searchCode():
        f=open("Member.csv")
        csvr=csv.reader(f)
        co2=int(input("Enter the code to be searched:"))
        found=0
        for k in csvr:
            if int(k[1])==co2:
                found=1
                break
        if found:
            print("Code found")
            print(k)
        else:
            print("Code not found")
        f.close()

    def searchPhone():
        f=open("Member.csv")
        csvr=csv.reader(f)
        co5=int(input("Enter the phone number to be searched:"))
        found=0
        for k in csvr:
            if int(k[4])==co5:
                found=1
                break
        if found:
            print("Phone number found")
            print(k)
        else:
            print("Phone number not found")
        f.close()
        
    while True:
        print('-- Search Menu --')
        print('1. Search by Name')
        print('2. Search by Code')
        print('3. Search by Phone Number')
        print('4. Returning to the program')
        ch=input('Enter the choice[1-4]')
        if ch=='1':
            searchName()
        elif ch=='2':
            searchCode()
        elif ch=='3':
            searchPhone()
        elif ch=='4':
            break

def editRecords():
    def EditDate():
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        da1=input("Enter the date to be changed:")
        da2=input("Enter the new date:")
        for k in csvr:
            if k[2]==da1:
                k[2]=da2
            csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    def EditAddress():
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        ad1=input("Enter the address to be changed:")
        ad2=input("Enter the new address:")
        for k in csvr:
            if k[3]==ad1:
                k[3]=ad2
            csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    def EditPhone():
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        ph1=input("Enter the phone no. to be changed:")
        ph2=input("Enter the new phone no.:")
        for k in csvr:
            if k[4]==ph1:
                k[4]=ph2
            csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    while True:
        print('-- Edit Menu --')
        print('1. Edit Date')
        print('2. Edit Address')
        print('3. Edit Phone no.')
        print('4. Returning to the program')
        ch=input('Choice[1-4]? ')
        if ch=='1':
            EditDate()
        elif ch=='2':
            EditAddress()
        elif ch=='3':
            EditPhone()
        elif ch=='4':
            break

def delRecords(): 
    def delName():
        na1=input("Enter the name of the record to be deleted:")
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if k[0]==na1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    def delCode():
        co1=input("Enter the code of the record to be deleted:")
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if k[1]==co1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    def delDate():
        da1=input("Enter the date of the record to be deleted:")
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if k[2]==da1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    def delAddress():
        ad1=input("Enter the address of the record to be deleted:")
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if k[3]==ad1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    def delPhone():
        ph1=input("Enter the phone no. of the record to be deleted:")
        f1=open("Member.csv")
        f2=open("Member2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if k[4]==ph1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Member.csv")
        os.rename("Member2.csv","Member.csv")

    while True:
        print('-- Delete Menu --')
        print('1. Delete by name')
        print('2. Delete by code')
        print('3. Delete by date')
        print('4. Delete by address')
        print('5. Delete by phone')
        print('6. Returning to the main menu')
        ch=input('Choice[1-6]? ')
        if ch=='1':
            delName()
        elif ch=='2':
            delCode()
        elif ch=='3':
            delDate()
        elif ch=='4':
            delAddress()
        elif ch=='5':
            delPhone()
        elif ch=='6':
            break

while True:
     print('-- Main Menu --')
     print('1. Add Records')
     print('2. Display Records')
     print('3. Search Records')
     print('4. Edit Records')
     print('5. Delete Records')
     print('6. Exit')
     ch=input('Choice[1-6]? ')
     if ch=='1':
         addRecords()
     elif ch=='2':
         displayRecords()
     elif ch=='3':
         searchRecords()
     elif ch=='4':
         editRecords()
     elif ch=='5':
         delRecords()
     elif ch=='6':
         print("Exiting from the menu")
         break

