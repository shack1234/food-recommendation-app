
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required,Email
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(),Email()])
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")
     
class AddRestraurantForm(FlaskForm):
    name = StringField(' name ', validators=[Required()])
    description = StringField('Restraurant Description', validators=[Required()])
    image = FileField('Image', validators=[Required()])
    submit = SubmitField('Add Restraurant')


class ReviewForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Bolognese','Bolognese'),('Burger','Burger'),('Chicken','Chicken'),('Fish','Fish')],validators=[Required()])
    post = TextAreaField('Your Review', validators=[Required()])
    submit = SubmitField('Review')