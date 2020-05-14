from flask import render_template, request, redirect, url_for, abort ,flash
from . import main  
from .forms import  UpdateProfile,AddRestraurantForm,ReviewForm
from ..models import User ,Restaurant,Food,Review
from flask_login import login_required, current_user
from .. import db,photos
from flask_uploads import UploadSet,configure_uploads,IMAGES
import markdown2
import secrets
import os
from PIL import Image



@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching Website Online'

    search_pitch = request.args.get('pitch_query')
   
    return render_template('index.html', title = title)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('app/static/photos', picture_filename)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

@main.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Succesfully updated your profile')
        return redirect(url_for('main.profile'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename = 'photos/'+ current_user.profile_pic_path) 
    return render_template('profile/profile.html', profile_pic_path=profile_pic_path, form = form)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)







@main.route('/add', methods=['GET','POST'])
def add_restraurant():
   
    rest_form = AddRestraurantForm()
    if request.method =='POST':
        if rest_form.validate_on_submit():
            f = request.files['image']
            path = f'image'
            f.save(f.filename)
            url = f.filename
            new_rest = Restaurant(name=rest_form.name.data,description=rest_form.description.data ,image=url)
            db.session.add(new_rest)
            db.session.commit()
            flash('New restraurant was added success')
        
    return render_template('add_rest.html', rest_form=rest_form)

# #new-review file
# @main.route('/food/review/new/', methods = ['GET','POST'])
# @login_required
# def new_review():
#     form = ReviewForm()
#     if form.validate_on_submit():
#         title = form.name.data
#         review = form.review.data
#         # Updated review instance
#         new_review = Review(food_id=food.id,food_name=name,image_path=food.image,food_review=review,user=current_user)
#         # save review method
#         new_review.save_review()
#         return redirect(url_for('.food'))

#     title = f'food review'
#     return render_template('new_review.html',title = title, review_form=form, food=food)
#movie file

# @main.route('/food')
# def food():
#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     title = food
#     reviews = Review
#     return render_template('food.html',title = food,reviews = reviews)

@main.route('/food/review/new/', methods = ['GET','POST'])
@login_required
def new_review():
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_review_object = Review(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_review_object.save_review()
        return redirect(url_for('main.index'))
    return render_template('new_review.html', form = form)


# new review 2
@main.route('/food/review/new/', methods = ['GET','POST'])
@login_required
def new_review1():
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_review_object = Review(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_review_object.save_review()
        return redirect(url_for('main.index'))
    return render_template('new_review1.html', form = form)


# new review 3
@main.route('/food/review/new/', methods = ['GET','POST'])
@login_required
def new_review2():
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_review_object = Review(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_review_object.save_review()
        return redirect(url_for('main.index'))
    return render_template('new_review2.html', form = form)


# new review 4
@main.route('/food/review/new/', methods = ['GET','POST'])
@login_required
def new_review3():
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_review_object = Review(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_review_object.save_review()
        return redirect(url_for('main.index'))
    return render_template('new_review3.html', form = form)







@main.route('/food/burger')
def food():
    title ='food Burger'
    burger = Review.query.filter_by(category = 'Burger').all()
    bolognese = Review.query.filter_by(category = 'Bolognese').all()
    chicken = Review.query.filter_by(category = 'Chicken').all()
    fish = Review.query.filter_by(category = 'Fish').all()
    return render_template('food.html', burger = burger, title = title, chicken = chicken, fish = fish, bolognese = bolognese)


@main.route('/food/bolognese')
def Bolognese():
    title ='food bolognese'
    bolognese = Review.query.filter_by(category = 'Bolognese').all()
    burger = Review.query.filter_by(category = 'Burger').all()
    chicken = Review.query.filter_by(category = 'Chicken').all()
    fish = Review.query.filter_by(category = 'Fish').all()
    return render_template('food1.html', burger = burger, title = title, chicken = chicken, fish = fish, bolognese = bolognese)


@main.route('/food/chicken')
def Chicken():
    title ='food chicken'
    chicken = Review.query.filter_by(category = 'Chicken').all()
    bolognese = Review.query.filter_by(category = 'Bolognese').all()
    burger = Review.query.filter_by(category = 'Burger').all()
    fish = Review.query.filter_by(category = 'Fish').all()
    return render_template('food2.html', burger = burger, title = title, chicken = chicken, fish = fish, bolognese = bolognese)


@main.route('/food/fish')
def Fish():
    title ='food Fish'
    fish = Review.query.filter_by(category = 'Fish').all()
    bolognese = Review.query.filter_by(category = 'Bolognese').all()
    burger = Review.query.filter_by(category = 'Burger').all()
    chicken = Review.query.filter_by(category = 'Chicken').all()
    
    return render_template('food3.html', burger = burger, title = title, chicken = chicken, fish = fish, bolognese = bolognese)
