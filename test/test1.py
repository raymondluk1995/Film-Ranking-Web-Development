import unittest, os
from app import app, db

from app.models import User, Poll

class StudentModelCase(unittest.TestCase):

  def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI']=\
      'sqlite:///'+os.path.join(basedir,'test.db')
    self.app = app.test_client()#creates a virtual test environment
    db.create_all()
    user1 = User(id='1',username='Test',email='22126041@qq.com',preference="Action Movie")
    poll1 = Poll(id='22', poll_name="happy", category="Action Movie", description="nothing" )

    db.session.add(user1)
    db.session.add(poll1)
    
    db.session.commit()
    pass

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_registration(self):

    print('test_registration')
    user= User.query.get('1')
    user.set_password('Superbugs!')

    u = User.query.get('1')
    self.assertTrue(u.check_password('Superbugs!'))
    self.assertFalse(u.check_password('Regular bugs!'))

  def test_email(self):

      print('test_email')
      u = User.query.get('1')
      self.assertEqual(u.email, '22126041@qq.com')











if __name__=='__main__':
  unittest.main()
