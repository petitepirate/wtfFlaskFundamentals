from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from models import Employee, Department, db, connect_db
from forms import AddSnackForm  # UserForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"

connect_db(app)

# toolbar = DebugToolbarExtension(app)


@app.route("/phones")
def phone_list():
    """Get list of users & dept phones.

    This version will be a 'n+1 query' --- it will query once for all
    users, and then for each department.

    There's a way to tell SQLAlchemy to load all the data in a single query,
    but don't worry about this for now.
    """

    emps = Employee.query.all()
    return render_template("phones.html", emps=emps)


@app.route('/snacks/new')
def add_snack():
    form = AddSnackForm()
    return render_template("snack_add_form.html", form=form)
