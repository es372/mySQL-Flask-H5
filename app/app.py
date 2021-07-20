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

def tree_value():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable')
    result = cursor.fetchall()
    return

@app.route('/', methods = ['GET'])
def index():
    user = {'Trees Homework5'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable')
    result = cursor.fetchall()
    return render_template('index.html', user=user, trees=result)

@app.route('/view/<int:tree_value>', methods = ['GET'])
def view_tree_index(tree_value):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable WHERE value=%s', tree_value)
    result = cursor.fetchall()
    return render_template('view.html', tree=result[0])

@app.route('/edit/<int:tree_value>', methods = ['GET'])
def edit_tree_index(tree_value):
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM treesTable WHERE value=%s', tree_value)
        result = cursor.fetchall()
        return render_template('edit.html', tree=result[0])


''' ####THIS CODE KEEPS GETTING ERRORS#####
@app.route('/edit/<int:tree_value>', methods=['POST'])
def save_tree_edit(tree_value):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('value'), request.form.get('Girth_in'), request.form.get('Height_ft'),
                 request.form.get('Volume_ft'), tree_value)
    sql_update_query = "UPDATE treesTable t SET t.value = %s, t.Girth_in = %s, t.Height_ft = %s, t.Volume_ft = %s"
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)
'''



@app.route('/edit/<int:tree_value>', methods=['POST'])
def save_tree_edit(tree_value):
    cursor = mysql.get_db().cursor()
    update = '''UPDATE treesTable t SET value=%s, Girth_in=%s, Height_ft=%s, Volume_ft=%s WHERE value=%s'''
    cursor.execute(update, (request.form.get('value'), request.form.get('Girth_in'), request.form.get('Height_ft'),
             request.form.get('Volume_ft'), tree_value))
    mysql.get_db().commit()
    return redirect("/", code=302)


if __name__ == '__main__':
    app.run(host='0.0.0.0')