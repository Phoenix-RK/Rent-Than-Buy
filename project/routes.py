import os
import secrets
from flask import *
from flask import render_template, url_for, flash, redirect,request
from project import app, db, bcrypt
from project.forms import RegistrationForm, LoginForm,UpdateAccountForm,SuggestForm,OrderForm,ExtendForm,ListForm,LoginAdm
from project.models import Farmer1, Admin1,Tools1,Details,Suggestions,Order,Extend
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/farmer_home",methods=['GET'])
def farmer_home():
    return render_template('farmer_home.html')

@app.route("/tools",methods=['GET', 'POST'])
def tools():
     return render_template('tools.html')

@app.route("/lists",methods=['GET','POST'])  
def lists():  
    form = ListForm()
    user = Order.query.filter_by(username=form.username.data).all()
    print(user)
    return render_template('lists.html',rows = user,form=form)  
 
@app.route("/adminlist",methods=['GET','POST'])  
def adminlist():  
    
    user = Order.query.all()
    print(user)
    return render_template('adminlist.html',rows = user)  

@app.route("/adminsug",methods=['GET','POST'])  
def adminsug():  
    
    user = Suggestions.query.all()
    print(user)
    return render_template('adminsug.html',rows = user)  
 
@app.route("/adminex",methods=['GET','POST'])  
def adminex():  
    
    user = Extend.query.all()
    print(user)
    return render_template('adminex.html',rows = user)  
 

@app.route("/suggest", methods=['GET', 'POST'])
def suggest():
    
    form = SuggestForm()
    if form.validate_on_submit():
        user = Suggestions(tool_name=form.tool_name.data,size=form.size.data)
        db.session.add(user)
        db.session.commit()
        flash('Your suggestion has been accepted! Tools will be available soon')
        return redirect(url_for('suggest'))
    return render_template('suggest.html', title='Suggest', form=form)


@app.route("/about")
def about():
     return render_template('about.html')

@app.route("/order", methods=['GET' , 'POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        user = Order(username=form.username.data, tool=form.tool.data, duration=form.duration.data)
        db.session.add(user)
        db.session.commit()
        flash('Your selection has been added! You cad add another tool or place order')
        return redirect(url_for('order'))
    return render_template('order.html', title='Order', form=form)

@app.route("/extend", methods=['GET' , 'POST'])
def extend():
    form = ExtendForm()
    if form.validate_on_submit():
        user = Extend(username=form.username.data,duration=form.duration.data)
        db.session.add(user)
        db.session.commit()
        flash('Your request has been sent and amount will be added')
        return redirect(url_for('farmer_home'))
    return render_template('extend.html', title='extend', form=form)

    
@app.route("/register", methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Farmer1(username=form.username.data, Aadhaar=form.Aadhaar.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    redirect(url_for('login'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Farmer1.query.filter_by(Aadhaar=form.Aadhaar.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('farmer_home'))        
        else:
            flash('Login Unsuccessful. Please check Aadhaar and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logina")
def logina():
     return render_template('admin_home.html')

@app.route("/logind")
def logind():
      user = Details.query.all()
      print(user)
      return render_template('deliverer_home.html',rows = user)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET' , 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        user = Details(username=form.username.data, door_no=form.door_no.data, Area=form.Area.data)
        db.session.add(user)
        db.session.commit()
        flash('your account has been updated successfully!!!')
        return redirect(url_for('farmer_home'))
    
    return render_template('account.html', title='Account',form=form)

    