const APP_ID = 'johnhackathon-irndc';
const ATLAS_SERVICE = 'mongodb-atlas';
const app = new Realm.App({id: APP_ID});

user_id = null;

// Function executed by the LOGIN button.
const login = async () => {
    const credentials = Realm.Credentials.anonymous();
    try {
        const user = await app.logIn(credentials);
        $('#user').empty().append(user.id); // update the user div with the user ID
        user_id = user.id;
    } catch (err) {
        console.error("Failed to log in", err);
    }
};

const insert_todo = async () => {
    const mongodb = app.currentUser.mongoClient(ATLAS_SERVICE);
    coll = mongodb.db("test").collection("todos");
    console.log("===> User ID", user_id);
    coll.insertOne({"task": "I NEED TODO", status: false, owner_id: user_id})
}

// Function executed by the "FIND" button.
const find_todos = async () => {
    console.log("HelloWorld?");
    let coll;
    try {
        // Access the todos collection through MDB Realm.
        const mongodb = app.currentUser.mongoClient(ATLAS_SERVICE);
        coll = mongodb.db("test").collection("todos");
        console.log("mongodb", mongodb);
        console.log("coll", coll);
    } catch (err) {
        $("#user").append("Need to login first.");
        console.error("Need to log in first", err);
        return;
    }

    // Retrieve todos
    const todos = await coll.find({}, {
        "projection": {
            "_id": 0,
            "task": 1,
            "status": 1
        }
    });

    console.log(todos);

    // Access the todos div and clear it.
    let todos_div = $("#todos");
    todos_div.empty();

    // Loop through the todos and display them in the todos div.
    for (const todo of todos) {
        console.log(todo.task);
        let p = document.createElement("p");
        p.append(todo.task);
        p.append("=>");
        p.append(todo.status);
        todos_div.append(p);
    }
};

