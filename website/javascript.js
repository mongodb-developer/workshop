const APP_ID = '<YOUR-APPID>';
const ATLAS_SERVICE = 'mongodb-atlas';
const app = new Realm.App({id: APP_ID});

let user_id = null;
let mongodb = null;
let coll = null;

// Function executed by the LOGIN button.
const login = async () => {
    const credentials = Realm.Credentials.anonymous();
    try {
        const user = await app.logIn(credentials);
        $('#userid').empty().append(user.id); // update the user div with the user ID
        user_id = user.id;
        mongodb = app.currentUser.mongoClient(ATLAS_SERVICE);
        coll = mongodb.db("test").collection("todos");
    } catch (err) {
        console.error("Failed to log in", err);
    }
};

// Function executed by the INSERT button.
const insert_todo = async () => {
    console.log("INSERT");
    const task = $('#taskInput').val();
    await coll.insertOne({task, status: false, owner_id: user_id});
    find_todos();
}

const toggle_todo = async () => {
    console.log("TOGGLE");
    const task = $('#taskInput').val();
    const todo = await coll.findOne({task, owner_id: user_id});
    await coll.updateOne({"_id": todo._id, owner_id: user_id}, {"$set": {"status": !todo.status}});
    find_todos();
}

const delete_todo = async () => {
    console.log("DELETE");
    const task = $('#taskInput').val();
    await coll.deleteOne({task, owner_id: user_id});
    find_todos();
}

// Function executed by the "FIND" button.
const find_todos = async () => {
    if (mongodb == null || coll == null) {
        $("#userid").empty().append("Need to login first.");
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
        let p = document.createElement("p");
        p.append(todo.task);
        p.append(" => ");
        p.append(todo.status ? "Done!" : "TODO!");
        todos_div.append(p);
    }
};

