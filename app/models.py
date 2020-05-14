
from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255), default='My default Bio')
    profile_pic_path = db.Column(db.String(150), default='default.png')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'
    
    
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
      
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),index = True,unique = True, nullable = False)
    image= db.Column(db.String(80))
    description = db.Column (db.String)
    food_id = db.Column(db.Integer, db.ForeignKey("foods.id"))
    
class Food(db.Model):
    
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255),index = True,unique = True, nullable = False)
    image_path = db.Column(db.String)
    description = db.Column (db.String)
    reviews = db.relationship('Review',backref = 'reviews',lazy = "dynamic")
    restaurants = db.relationship('Restaurant',backref = 'user',lazy = "dynamic")
    
class Review(db.Model):
    
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.Text(), nullable = False)
    category = db.Column(db.String(255), index = True,nullable = False)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    food_id = db.Column(db.Integer, db.ForeignKey("foods.id"))
    def save_review(self):
        db.session.add(self)
        db.session.commit()
    def delete_review(self):
        db.session.delete(self)
        db.session.commit()
