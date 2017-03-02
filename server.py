import flask
import flask_sqlalchemy
import flask_restless

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__, static_url_path='/ayylmao')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/<path:path>')
def send_js(path):
    return flask.send_from_directory('todoist/dist', path)
@app.route('/')
def send_index():
    return flask.send_file('todoist/dist/index.html')

# Create your Flask-SQLALchemy models as usual but with the following
# restriction: they must have an __init__ method that accepts keyword
# arguments for all columns (the constructor in
# flask_sqlalchemy.SQLAlchemy.Model supplies such a method, so you
# don't need to declare a new one).
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode)
    done = db.Column(db.Boolean)

# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Todo, methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])

# start the flask loop
app.run()
