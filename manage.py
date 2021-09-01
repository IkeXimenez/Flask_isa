
# App management file for runnig from command Line IKE 1 sep 2021

from flask_script import Manager
from flaskisa.App import app

manager = Manager(app)
#App.config['DEBUG'] = True # Ensure debugger will load.

if __name__ == '__main__':
	manager.run()
