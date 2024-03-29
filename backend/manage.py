from app import create_app,db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

"""
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver -p 8000
虚拟环境，进入script activate
"""

app = create_app("development")
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()