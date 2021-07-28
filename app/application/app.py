import simplejson as json
from flask import Flask, request, Response, redirect, make_response
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask import render_template
from app.application.home.forms import ContactForm


app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL(cursorclass=DictCursor)
mysql.init_app(app)


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

@app.route('/edit/<int:tree_value>', methods=['POST'])
def save_tree_edit(tree_value):
    cursor = mysql.get_db().cursor()
    update = '''UPDATE treesTable SET value=%s, Girth_in=%s, Height_ft=%s, Volume_ft=%s WHERE value=%s'''
    cursor.execute(update, (request.form.get('value'), request.form.get('Girth_in'), request.form.get('Height_ft'),
             request.form.get('Volume_ft'), tree_value))
    mysql.get_db().commit()
    return redirect("/", code=302)



@app.route('/trees/new', methods=['GET'])
def insert_new_tree():
    return render_template('new.html')

@app.route('/trees/new', methods = ['POST'])
def save_new_tree():
    cursor = mysql.get_db().cursor()
    insert = '''INSERT INTO treesTable (value, Girth_in, Height_ft, Volume_ft) VALUES (%s, %s,%s, %s)'''
    cursor.execute(insert, (request.form.get('value'), request.form.get('Girth_in'), request.form.get('Height_ft'),
    request.form.get('Volume_ft')))
    mysql.get_db().commit()
    return redirect("/", code=302)



@app.route('/delete/<int:tree_value>', methods=['POST'])
def form_delete_post(tree_value):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM treesTable WHERE value = %s """
    cursor.execute(sql_delete_query, tree_value)
    mysql.get_db().commit()
    return redirect("/", code=302)



@app.route('/api/v1/trees', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/trees/<int:tree_value>', methods=['GET'])
def api_retrieve(tree_value) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM treesTable WHERE value=%s', tree_value)
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/trees/<int:tree_value>', methods=['PUT'])
def api_edit(tree_value) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['value'], content['Girth_in'], content['Height_ft'],
                 content['Volume_ft'], tree_value)
    sql_update_query = '''UPDATE treesTable SET value=%s, Girth_in=%s, Height_ft=%s, Volume_ft=%s WHERE value=%s'''
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp

@app.route('/api/v1/trees', methods=['POST'])
def api_add() -> str:
    content = request.json
    cursor = mysql.get_db().cursor()
    insert = '''INSERT INTO treesTable (value, Girth_in, Height_ft, Volume_ft) VALUES (%s, %s,%s, %s)'''
    cursor.execute(insert, (content['value'], content['Girth_in'], content['Height_ft'], content['Volume_ft']))
    mysql.get_db().commit()
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/trees/<int:tree_value>', methods=['DELETE'])
def api_delete(tree_value) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM treesTable WHERE value = %s """
    cursor.execute(sql_delete_query, tree_value)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect("/", code=302)
    return render_template("contact.html", form=form)

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        'SORRY. THIS PAGE IS NOT FOUND.',
        404
     )


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        'BAD REQUEST! THIS SERVER DOES NOT SUPPORT YOUR REQUEST.',
        400
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')