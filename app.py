from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@127.0.0.1:5432/todoapp'
db = SQLAlchemy(app)

@app.route('/')
def index():
  return render_template('index.html', data=[{
    'description': 'Todo 1'
  }, {
    'description': 'Todo 2'
  }, {
    'description': 'Todo 3'
  }])