from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Population'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root@localhost:3306/Population'
mysql.init_app(app)

