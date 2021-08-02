from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from .assets import compile_assets

assets = Environment()

mysql = MySQL(cursorclass=DictCursor)

def init_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    mysql.init_app(app)

    with app.app_context():


        from .home.routes import home_bp
        app.register_blueprint(home_bp)
        compile_assets(assets)

    return app