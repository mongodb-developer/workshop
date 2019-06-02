# 
# mlynn - create example
#
import os,sys
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData


if "MONGODB_ATLAS_URI" in os.environ:
    print ("connecting to ",os.environ.get("MONGODB_ATLAS_URI"))
else:
    print("No Atlas URI Set... please create a .env with a MONGODB_ATLAS_URI variable")
    sys.exit(1)

def main():

    while(1):
    # chossing option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print('\n INVALID SELECTION \n')

def insert():
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')
        
        db.Employees.insert_one(
            {
                "id": employeeId,
                "name":employeeName,
                "age":employeeAge,
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
