from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort, marshal
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class CategoryModel(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"CategoryModel(category = {self.category})"

class CommandModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(200), nullable=False)
    command_description = db.Column(db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category_model.category_id', ondelete='CASCADE'), nullable=False) #TO-DO: Trying to delete not empty categories
    category = db.relationship('CategoryModel', backref=db.backref('commands', lazy=True))

    def __repr__(self):
        return f"CommandModel(command = {self.command}, command_description = {self.command_description}, category_id = {self.category_id})"

# Just the first time to create the tables
with app.app_context():
    db.create_all()

#small healthcheck test when call /healthcheck
class healthcheck(Resource):
    def get(self):
        return {'hello': 'healthy'}

api.add_resource(healthcheck, '/healthcheck')
#--------------------------------------------#

kb_post_args = reqparse.RequestParser()
kb_post_args.add_argument("id", type=int, help="ID of the category")
kb_post_args.add_argument("command", type=str, help="Command you'd like to save", required=True)
kb_post_args.add_argument("command_description", type=str, help="Description or use case of the command", required=True)

kb_update_args = reqparse.RequestParser()
#kb_update_args.add_argument("id", type=int, help="ID of the category")
kb_update_args.add_argument("command", type=str, help="Command you'd like to save", required=True)
kb_update_args.add_argument("command_description", type=str, help="Description or use case of the command", required=True)

# Solution I found to get the category name
def get_category_name(command):
    category = CategoryModel.query.get(command.category_id)
    return category.category

command_resource_fields = {
    'id': fields.Integer,
    'category_id': fields.Integer,
    'category': fields.String(attribute=get_category_name),
    'command': fields.String,
    'command_description': fields.String
}

category_post_args = reqparse.RequestParser()
category_post_args.add_argument("category", type=str, help="Name of the category", required=True)

category_resource_fields = {
    'category_id': fields.Integer,
    'category': fields.String
}

#---------CATEGORY CLASS---------#
class Category(Resource):
    @marshal_with(category_resource_fields)
    def post(self):
        args = category_post_args.parse_args()
        category = CategoryModel(category=args['category'])
        db.session.add(category)
        db.session.commit()
        return category, 201
    
    @marshal_with(category_resource_fields)
    def get(self):
        categories = CategoryModel.query.all()
        return categories
    
    def delete(self, category_id):
        result = CategoryModel.query.filter_by(category_id=category_id).first()
        if not result:
            abort(404, message="Could not find Category with that id")
        db.session.delete(result)
        db.session.commit()
        log = {"message": f"Deleted Category with id {category_id}"}
        return log, 200
    
api.add_resource(Category, "/categories",
                 "/categories/<int:category_id>")

#---------COMMAND CLASS---------#
class Commands(Resource):
    @marshal_with(command_resource_fields)
    def get(self, category_id, id=None):
        category = CategoryModel.query.filter_by(category_id=category_id).first()
        if not category:
            abort(404, message="Category not found")
        if id is not None:
            commands = CommandModel.query.filter_by(id=id, category_id=category_id).first()
        else:
            commands = CommandModel.query.filter_by(category_id=category_id).all()
        
        return commands
    
    @marshal_with(command_resource_fields)
    def post(self, category_id, id=None):
        args = kb_post_args.parse_args()
        category = CategoryModel.query.filter_by(category_id=category_id).first()
        if not category:
            abort(404, message="Category not found")
        if id is not None:
            check_existing_id = CommandModel.query.get(id)
            if check_existing_id:
                abort(409, message="Command ID already exists. Please choose another one!")
            else:
                command = CommandModel(id=id,command=args['command'], category_id=category_id, command_description=args['command_description'])
        else:
            command = CommandModel(command=args['command'], category_id=category_id, command_description=args['command_description'])
        db.session.add(command)
        db.session.commit()
        return command, 201
    
    def delete(self, category_id, id):
        command = CommandModel.query.filter_by(category_id=category_id, id=id).first()
        if not command:
            abort(404, message="Could not find command with that id")
        db.session.delete(command)
        db.session.commit()
        log = {"message": f"Deleted command with id {id}"}
        return log, 200
    
    @marshal_with(command_resource_fields)
    def put(self, category_id, id):
        args = kb_update_args.parse_args()
        command = CommandModel.query.filter_by(category_id=category_id, id=id).first()
        if not command:
            abort(404, message="Could not find command with that id")
        if 'command' in args:
            command.command = args['command']
        if 'command_description' in args:
            command.command_description = args['command_description']
        db.session.commit()
        return command, 200

api.add_resource(Commands, '/categories/<int:category_id>/commands',
                 '/categories/<int:category_id>/commands/<int:id>')

#--------------------------------------------#

if __name__ == '__main__':
    debug_mode = os.environ.get("DEBUG_MODE", "false").lower() == "true"
    app.run(debug=debug_mode)