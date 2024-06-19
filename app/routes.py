from flask import jsonify, render_template, request, Flask, url_for, redirect
from app import app, db, bcrypt
from app.models import Person
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError
from app.forms import validate_username, validate_password


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
    try:
        # Limit maximum of existing users
        if User.query.count() >= 11:
            return jsonify(message="User limit reached. No more registrations are allowed."), 403
        
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            # Check for empty entry
            if not username or not password:
                return jsonify(message="Username and password are required"), 400

            if not validate_username(username):
                return jsonify(message="Invalid username. Must be 4-20 characters long, contain only letters, numbers, and underscores, and have no spaces."), 400
        
            if not validate_password(password):
                return jsonify(message="Invalid password. Must be at least 6 characters long and have no spaces."), 400

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            
            user = User(username=username, password=hashed_password)
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        
    except IntegrityError:
        db.session.rollback()
        return jsonify(message='User already exists'), 409
    except Exception as e:
        return jsonify(message=f'An error occurred: {str(e)}'), 500
    
## Login 
@app.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            # Check for empty entry
            if not username or not password:
                return jsonify(message="Username and password are required"), 400
            
            user = User.query.filter(User.username == username).first()
            
            if user is None:
                return jsonify(message="Invalid username or password"), 401
        
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return render_template('index.html'), 200
            else:
                return jsonify(message="Invalid username or password"), 401
    except Exception as e:
        return jsonify(massage=f'An error occurred: {str(e)}'), 500

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/secret')
@login_required
def secret():
    return 'The Secrete'
    