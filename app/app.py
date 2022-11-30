import os
from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine

from sqlalchemy.sql import func
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@python-demo-population-mysql:3306/Population'
engine = create_engine("mysql+pymysql://root:root@python-demo-population-mysql:3306/Population")
conn = engine.connect()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Country(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    population = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Country {self.city}>'

# Displaying All Records

@app.route('/')
def index():
    countrys = Country.query.all()
    return render_template('index.html', countrys=countrys)

#Displaying Single City Information

@app.route('/<int:country_id>/')
def country(country_id):
    country = Country.query.get_or_404(country_id)
    return render_template('population.html', country=country)

# Creating a New Record

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        id = request.form['id']
        city = request.form['city']
        population = request.form['population']
        country = Country(id =id, city=city,
                          population=population,
                          )
        db.session.add(country)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')

# Edit using the ID


@app.route('/<int:country_id>/edit/', methods=('GET', 'POST'))
def edit(country_id):
    country = Country.query.get_or_404(country_id)

    if request.method == 'POST':
        id = country_id
        city = request.form['city']
        population = request.form['population']
        
        result = conn.execute('UPDATE country SET id=%s, city=\'%s\', population=%s Where id=%s' % (id,city,population,id))

        return redirect(url_for('index'))

    return render_template('edit.html', country=country)

# Deleting a Record

@app.post('/<int:country_id>/delete/')
def delete(country_id):
    country = Country.query.get_or_404(country_id)
    db.session.delete(country)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/healthy')
def healthy():
    conn.execute('SELECT city,population FROM Population.country;')
    return 'ok'
