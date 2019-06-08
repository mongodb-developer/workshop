# 
# mlynn - create example
#
import os,sys
from pymongo import MongoClient


if "MONGODB_ATLAS_URI" in os.environ:
    print ("connecting to ",os.environ.get("MONGODB_ATLAS_URI"))
    MONGO_URI=os.environ.get("MONGODB_ATLAS_URI")
else:
    print("No Atlas URI Set... please create a .env with a MONGODB_ATLAS_URI variable")
    sys.exit(1)

client = MongoClient(MONGO_URI)
db = client.EmployeeData

def main():

    while(1):

        selection = input('\nSelect C to Create, R to read, U to Update, D to Delete, x to Exit\n')

        if selection == 'C':
            insert()
        elif selection == 'U':
            update()
        elif selection == 'R':
            read()
        elif selection == 'D':
            delete()
        elif selection == 'x':
            sys.exit(0)
        else:
            print('\n INVALID SELECTION \n')

def insert():
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter Age :')
        employeeEmail = input('Enter Email Address :')
        employeeCountry = input('Enter Country :')
        
        db.Employees.insert_one(
            {
                "id": employeeId,
                "name":employeeName,
                "age":employeeAge,
                "email":employeeEmail,
                "country":employeeCountry
        })
        print('\nInserted data successfully\n')
    
    except(Exception, e):
        print({},str(e))

def update():
    print ("not implemented")

def read():
    print ("not implemented")

def delete():
    print ("not implemented")

if __name__ == "__main__":
    main()