import unittest, os
from app import app, db
from app.models import User, Poll, Option, Behaviour
import json

class StudentModelCase(unittest.TestCase):

    def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']=\
      'sqlite:///'+os.path.join(basedir,'test.db')
    self.app = app.test_client()#creates a virtual test environment
    db.create_all()
    user1 = User(id=23,username='test2',email='333@qq.com',preference="Action Movie")
    admin = User(id=5,username='admin',email='311133@qq.com',adminstrator=1,preference="Action Movie")
    poll1 = Poll(id=11, poll_name="sd", category="Action Movie", description="nothing")
    option1 = Option(id=1,poll_id=poll1.id, option='Lion King', votes=0)
    be1 =Behaviour(id=2 poll_id=11,user_id=23)


    db.session.add(user1)
    db.session.add(admin)
    db.session.add(poll1)
    db.session.add(option1)
    db.session.commit()
    db.session.commit(be1)
    pass

    def tearDown(self):
    db.session.remove()
    db.drop_all()
    print("Now the database is dropped")

    def test_registration(self):

    print('test_registration')
    user= User.query.get(23)
    user.set_password('Superbugs!')

    u = User.query.get(23)
    self.assertTrue(u.check_password('Superbugs!'))
    self.assertFalse(u.check_password('Regular bugs!'))

    def test_email(self):

      print('test_email')
      u = User.query.get(23)
      self.assertEqual(u.email, '333@qq.com')

    def  test_behaviour(self):

      print('test_behaviour')
      p= Poll.query.first()
      b= Behaviour(poll_id=p.id,user_id=23,option='Lion King')
      db.session.add(b)
      db.session.commit()
      self.assertEqual(b.option,'Lion King')


    def test_option(self):

      print('test_option')
      p= Poll.query.first()
      o= Option(poll_id=p.id,option='Mickey Mouse')
      db.session.add(o)
      db.session.commit()
      self.assertEqual(o.option,'Mickey Mouse')

    def test_create_poll(self):

      print('test_create_poll')
      p= Poll(poll_name='testing',category='Action Movie', description='nothing to show')
      db.session.add(p)
      db.session.commit()
      self.assertEqual(p.category,'Action Movie')

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.client.get('/delete_user')
        self.assertEqual(response.status_code, 200)

    def test_create_poll(self):
        response = self.client.get('/create_poll')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/template/1')
        self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = self.client.get('/wrong/url',headers=self.get_api_headers('username', 'password'))
        self.assertEqual(response.status_code, 404)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['error'], 'not found')






if __name__=='__main__':
  unittest.main()
