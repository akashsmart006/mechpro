from asyncio.windows_events import NULL
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        mobile=request.form.get('phone')
        pass1=request.form.get('password1')

        user=User.query.filter_by(mobile=mobile).first()
        if user:
            if(check_password_hash(user.password,pass1)):
                if (user.usertype=="mechanic"):
                    return redirect(url_for("views.home1"))
                else:
                    return redirect(url_for("views.home2"))
        else:
            print("user not found")

    return render_template("login.html")

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        mobile=request.form.get('phone')
        name=request.form.get('firstName')
        pass1=request.form.get('password1')
        pass2=request.form.get('password2')
        usertype=request.form.get('usertype')
        locat=request.form.get('location')
        location=float(locat)
    
        if(pass1==pass2):
            new_user=User(mobile=mobile,name=name,password=generate_password_hash(pass1,method='sha256'),usertype=usertype)
            db.session.add(new_user)
            db.session.commit()
            if(usertype=="mechanic"):
                return redirect(url_for("views.home1"))
            else:
                return redirect(url_for("views.home2"))


    return render_template("signup.html")