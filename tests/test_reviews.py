import unittest
from app.models import Review, User, Comments
from datetime import datetime
from app import db
class ReviewTest(unittest.TestCase):
def setUp(self):
    self.user_Me = User(username = 'Me', password = 'Herme', email = 'her@gmail.com')
    self.new_review = Review(title = 'test', post = 'testing',category='chicken',user_id = 1)
def tearDown(self):
    Review.query.delete()
    User.query.delete()
def test_check_instance_variables(self):
    self.assertEquals(self.new_review.title, 'test')
    self.assertEquals(self.new_review.post, 'testing' )
    self.assertEquals(self.new_review.category, 'chicken')
    self.assertEquals(self.new_review.user_id, 1)
   
 def test_save_review(self):
    self.new_review.save_pitch()
    self.assertTrue(len(Review.query.all())>0)
    
    
    
    