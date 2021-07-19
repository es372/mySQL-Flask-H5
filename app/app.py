import simplejson as json
from flask import Flask, request, Response, redirect
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask import render_template


app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'treesData'
mysql.init_app(app)


@app.route('/', methods = ['GET'])
def index():
    user = {'Trees Homework5'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable')
    result = cursor.fetchall()
    return render_template('index.html', user=user, trees=result)

@app.route('/view/tree.Index', methods = ['GET'])
def view_tree_index():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable')
    result = cursor.fetchall()
    return render_template('view.html', tree=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0')