from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
  id  = db.Column(db.Integer, primary_key = True)
  username  = db.Column(db.String(80), unique = True, nullable = False)
  email  = db.Column(db.String(80), unique = True, nullable = False)
  
  def __repr__(self):
    return f'<User {self.username}>'
  
user_args = reqparse.RequestParser()
user_args.add_argument('username', type=str, required=True, help="Username cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")

# In Flask-RESTful, the fields module is used to define how the output of an API endpoint should be structured and serialized before sending the response to the client. 
userFields = {
  'id': fields.Integer,
  'username': fields.String,
  'email': fields.String
}

# Resource is used to represent an endpoint in your API, and it can handle HTTP requests like GET, POST, PUT, and DELETE based on the methods you define in the class.
class Users(Resource):
  # The decorator to format the response returned by the get() method is serialized (converted into a format that can be sent as a JSON response) based on the structure defined in userFields.
  @marshal_with(userFields)
  def get(self):
    users = UserModel.query.all()
    return users
  @marshal_with(userFields)
  def post(self):
    args = user_args.parse_args()
    # The UserModel represents the user table in the database
    user = UserModel(username=args["username"], email=args["email"])
    db.session.add(user)
    db.session.commit()
    users = UserModel.query.all()
    return users, 201


class User(Resource):
  @marshal_with(userFields)
  def get(self, id):
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404, 'User not found')
    return user, 201
  
  @marshal_with(userFields)
  # The PATCH method is used for a partial update of a resource.
  def patch(self, id):
    args = user_args.parse_args()
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404, 'User not found')
    user.username = args['username']
    user.email = args['email']
    db.session.commit()
    return user
  
  @marshal_with(userFields)
  def delete(self, id):
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404, 'User not found')
    db.session.delete(user)
    db.session.commit()
    users = UserModel.query.all()
    return users, 200
    
    
# This method is used to register a resource (typically a class-based resource) with a specific route (or URL endpoint) in a Flask-RESTful API.
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

@app.route('/')
def home():
  return '<h1>Flask Rest API</h1>'

if __name__ == '__main__':
  app.run(debug=True)
  