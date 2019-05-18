import unittest
from flask import current_app
from app import app,db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
