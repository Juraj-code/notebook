from flask import jsonify
from app import app, db
from app.models import Person

@app.route('/')
def index():
    return 'Work in progress!'

@app.route('/test_db_connection')
def test_db_connection():
    try:
        person_count = db.session.query(Person).count()
        return jsonify(success=True, message="Database connection successful", person_count=person_count)
    except Exception as e:
        return jsonify(success=False, message=str(e))