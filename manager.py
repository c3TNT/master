from flask_migrate import MigrateCommand
from flask_script import Manager


app =create_app('develop')

manager =Manager()
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()