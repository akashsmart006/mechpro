from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views',__name__)

@views.route('/')
def base():
    return render_template("base.html")
@views.route('/home1')
def home1():
    return render_template("home1.html")
@views.route('/home2',methods=['GET','POST'])
def home2():
    if request.method=='POST':
        lat=request.form.get('lat')
        lon=request.form.get('lon')
        lat=float(lat)
        lon=float(lon)
        print(lat)
        print(lon)
    return render_template("home2.html")
