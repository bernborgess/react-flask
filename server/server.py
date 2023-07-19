from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, fields, marshal_with
from flask_cors import CORS

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)
app.app_context().push()
CORS(app, supports_credentials=True)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


todo_fields = {"id": fields.Integer, "title": fields.String, "complete": fields.Boolean}


class TodoResource(Resource):
    @marshal_with(todo_fields)
    def get(self):
        return Todo.query.all()


api.add_resource(TodoResource, "/")


@app.get("/")
def home():
    todo_list = Todo.query.all()
    return jsonify(todo_list)


@app.post("/add")
def add():
    new_todo = Todo(title="TITLE", complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"msg": "OK"})


@app.get("/update/<int:todo_id>")
def update(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return jsonify({"msg": "FAIL"})

    todo.complete = not todo.complete
    db.session.commit()
    return jsonify({"msg": "OK"})


@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"msg": "OK"})


if __name__ == "__main__":
    app.run(debug=True)
