#FACILITY FILE
import os,csv
def append():
    f=open("Facility.csv","a",newline='')
    csvw=csv.writer(f)
    n=int(input("Enter the value for n"))
    for k in range(n):
        fcode=int(input("Enter the value for the facility code=="))
        facility=input("your sport??")
        rec=[fcode,facility]
        csvw.writerow(rec)
    f.close()
def display():
    f=open("Facility.csv","r")
    csvr=csv.reader(f)
    for k in csvr:
        print(k[0],k[1])
    f.close()
def searchRecords():
    def searchFC():
        f=open("Facility.csv")
        csvr=csv.reader(f)
        co1=int(input("Enter the facility code to be searched:"))
        found=0
        for k in csvr:
            if int(k[0])==co1:
                found=1
                break
        if found:
            print("Facility code found")
            print(k)
        else:
            print("Facility code not found")
        f.close()
        
    def searchFacility():
        f=open("Facility.csv")
        csvr=csv.reader(f)
        co2=input("Enter the facility to be searched:")
        found=0
        for k in csvr:
            if k[1]==co2:
                found=1
                break
        if found:
            print("Facility found")
            print(k)
        else:
            print("Facility not found")
        f.close()
        
    while True:
        print('-- Search Menu --')
        print('1. Search by Facility code')
        print('2. Search by Facility')
        print('3. Returning to the program')
        ch=input('Enter the choice[1-3]')
        if ch=='1':
            searchFC()
        elif ch=='2':
            searchFacility()
        elif ch=='3':
            break

def editRecords():
    def EditFC():
        f1=open("Facility.csv")
        f2=open("Facility2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        fc1=int(input("Enter the facility code to be changed:"))
        fc2=int(input("Enter the new facility code:"))
        for k in csvr:
            if int(k[0])==fc1:
                k[0]=fc2
            csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Facility.csv")
        os.rename("Facility2.csv","Facility.csv")

    def EditFacility():
        f1=open("Facility.csv")
        f2=open("Facility2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        ad1=input("Enter the facility to be changed:")
        ad2=input("Enter the new facility:")
        for k in csvr:
            if k[1]==ad1:
                k[1]=ad2
            csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Facility.csv")
        os.rename("Facility2.csv","Facility.csv")

    while True:
        print('-- Edit Menu --')
        print('1. Edit Facility code')
        print('2. Edit Facility')
        print('3. Returning to the program')
        ch=input('Choice[1-3]? ')
        if ch=='1':
            EditFC()
        elif ch=='2':
            EditFacility()
        elif ch=='3':
            break

def delRecords(): 
    def delFC():
        co1=int(input("Enter the facility code of the record to be deleted:"))
        f1=open("Facility.csv")
        f2=open("Facility2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if int(k[0])==co1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Facility.csv")
        os.rename("Facility2.csv","Facility.csv")

    def delFacility():
        fa1=input("Enter the facility of the record to be deleted:")
        f1=open("Facility.csv")
        f2=open("Facility2.csv",'w',newline='')
        csvr=csv.reader(f1)
        csvw=csv.writer(f2)
        for k in csvr:
            if k[1]==fa1:
                pass
            else:
                csvw.writerow(k)
        f1.close()
        f2.close()
        os.remove("Facility.csv")
        os.rename("Facility2.csv","Facility.csv")

    while True:
        print('-- Delete Menu --')
        print('1. Delete by facility code')
        print('2. Delete by facility')
        print('3. Returning to the program')
        ch=input('Choice[1-3]? ')
        if ch=='1':
            delFC()
        elif ch=='2':
            delFacility()
        elif ch=='3':
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
        append()
     elif ch=='2':
         display()
     elif ch=='3':
         searchRecords()
     elif ch=='4':
         editRecords()
     elif ch=='5':
         delRecords()
     elif ch=='6':
         print("Exiting from the menu")
         break


