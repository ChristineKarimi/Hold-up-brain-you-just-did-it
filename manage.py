from app import create_app
from project_utils import generate_fake_users
from flask_script import Manager,Server


app = create_app('development')
manager = Manager(app)


manager.add_command('server',Server)


@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.option('-n', '--num', help='Number of fake users')
def fake_users(num=10,file="fake_users.json"):
    '''
    generate fake users
    '''
    f=generate_fake_users.FakeUsers()
    f.generate_to_json_file(int(num))




if __name__ == '__main__':
    manager.run()