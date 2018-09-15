import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)






@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/user', methods=['POST'])
def user():
 
  return redirect(url_for('index'))

if __name__ == '__main__':

  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
