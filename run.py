from app import create_app
from flask_script import Manager
app = create_app('dev')
# app = Manager(create_app)
if __name__ == '__main__':
    app.run()
