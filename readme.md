
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
3. Create contact form in tree application
4. Relocating Configuration in seperate file (no inline configuration)
5. Project restructure for application factory pattern
6. Initiate Flask in __init__.py
7. Create application context
8. Create app's entry point(wsgi.py)
9. Get rid of app.py and implement single responsiblity principle
10. Create routes.py for application routing
11. Add blueprint configuration to routes.py
12. create global variable of mysql for cursor in __init__.py (Database functionality)
13. Implemt Flask structure with home blueprint
14. Register Home Blueprint in __init__.py
15. Fix Jinja2 routing with Home Blueprint
16. Test application functionality using Docker (no errors)

After reading the tutorial, I realized my current application may work, however, it was no where near the quality a Flask application
needs to be. Thus, I learned a lot about the best methods to manage a flask application with a database. 











