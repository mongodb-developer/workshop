from flask import Flask, render_template, redirect
from pymongo import MongoClient
import os,sys
from classes import *

if "MONGODB_ATLAS_URI" in os.environ:
    print ("connecting to ",os.environ.get("MONGODB_ATLAS_URI"))
    MONGO_URI=os.environ.get("MONGODB_ATLAS_URI")
else:
    print("No Atlas URI Set... please create a .env with a MONGODB_ATLAS_URI variable")
    sys.exit(1)

client = MongoClient(MONGO_URI)
db = client.EmployeeData

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))

if db.settings.find({'name': 'next_id'}).count() <= 0:
    print("next_id Not found, creating....")
    db.settings.insert_one({'name':'next_id', 'value':0})

def updateEmployeeID(value):
    next_id = db.settings.find_one()['value']
    next_id += value
    db.settings.update_one(
        {'name':'next_id'},
        {'$set':
            {'value':next_id}
        })

def createEmployee(form):
    name = form.name.data
    age = form.age.data
    email = form.email.data
    country = form.country.data
    next_id = db.settings.find_one()['value']
    
    emp = {'id':next_id, 'name':name, 'age':age, 'email':email, 'country':country}

    db.Employees.insert_one(emp)
    updateEmployeeID(1)
    return redirect('/')

def deleteEmployee(form):
    key = form.key.data
    name = form.name.data
    if(key):
        print(key, type(key))
        db.Employees.delete_many({'id':int(key)})
    else:
        db.Employees.delete_many({'name':name})

    return redirect('/')

def updateEmployee(form):
    key = form.key.data
    name = form.name.data
    
    db.Employees.update_one(
        {"id": int(key)},
        {"$set":
            {"name": name}
        }
    )

    return redirect('/')

def resetEmployee(form):
    db.Employees.drop()
    db.settings.drop()
    db.settings.insert_one({'name':'next_id', 'value':0})
    return redirect('/')

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    cform = CreateEmployee(prefix='cform')
    dform = DeleteEmployee(prefix='dform')
    uform = UpdateEmployee(prefix='uform')
    reset = ResetEmployee(prefix='reset')

    # response
    if cform.validate_on_submit() and cform.create.data:
        return createEmployee(cform)
    if dform.validate_on_submit() and dform.delete.data:
        return deleteEmployee(dform)
    if uform.validate_on_submit() and uform.update.data:
        return updateEmployee(uform)
    if reset.validate_on_submit() and reset.reset.data:
        return resetEmployee(reset)

    # read all data
    docs = db.Employees.find()
    data = []
    for i in docs:
        data.append(i)

    return render_template('home.html', cform = cform, dform = dform, uform = uform, \
            data = data, reset = reset)

@app.route('/delete/<emp>', methods=['GET','POST'])
def delete(emp):
    if(emp):
        print(emp, type(emp))
        db.Employees.delete_many({'id':int(emp)})

    return redirect('/')

if __name__=='__main__':
    app.run(debug=True,port=8081)
