from flask import jsonify, render_template, request, Flask, url_for, redirect
from app import app, db, bcrypt
from app.models import Person
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
def index():
    return render_template('index.html')

## Test of connection to the database
@app.route('/test_db_connection')
def test_db_connection():
    try:
        people_count = db.session.query(Person).count()
        return jsonify(success=True, message="Database connection successful", people_count=people_count)
    except Exception as e:
        return jsonify(success=False, message=str(e))
    
# TODO: Limit na userov v databaze
# TODO: Exceptions    
## Registration of the user
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        user = User(username=username, password=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

## Login 
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter(User.username == username).first()
        print("user :"+ str(user.username))
        
        if user is None:
            return jsonify(message="Invalid username or password"), 401
    
        if bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return render_template('index.html')
        else:
            return 'Failed'
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/secret')
@login_required
def secret():
    return 'The Secrete'
    