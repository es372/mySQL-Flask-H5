
PROPERLY MANAGING TREE DATABASE MODEL WITH FLASK-MYSQL, DOCKER, AND PYTHON

The tutorial went over how to properly structure and code flask applications with a database model. The project assignment involved
updating our current applications with the goal of learning correct practices when managing our data application. 

Here are the some of systems/tools that my project uses:
- Bootstrap CSS
- Flask
- Flask-MySQL
- Pycharm
- JSON
- Docker
- Python
- Flask-WTF
- Jinja2
- Blueprints

The tutorial uses different systems such as SQLAlchemy and stylesheets. So I implemented the systems in my project accordingly with
the instructions of the tutorials to achieve the same goal, by researching how to solve the problems I encountered in doing so. Being
that my application uses different systems, here is a general overview on how I updated my project:

1. Routing my flask application to handle errors
2. Configuring my flask app with secret keys for WTForms
3. Relocating Configuration in seperate file (no inline configuration)
4. Project restructure for application factory pattern
5. Initiate Flask in __init__.py
6. Create application context
7. Create app's entry point(wsgi.py)
8. Get rid of app.py and implement single responsiblity principle
9. Create routes.py for application routing
10. Add blueprint configuration to routes.py
11. create global variable of mysql for cursor in __init__.py (Database functionality)
12. Implemt Flask structure with home blueprint
13. Register Home Blueprint in __init__.py
14. Fix Jinja2 routing with Home Blueprint

After reading the tutorial, I realized my current application may work, however, it was no where near the quality a Flask application
needs to be. Thus, I learned a lot about the best methods to manage a flask application with a database. 











