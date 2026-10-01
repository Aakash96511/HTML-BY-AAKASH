from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder='.')

# Database configuration (creates a local SQLite file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    student_id = db.Column(db.String(20), nullable=False, unique=True)
    course = db.Column(db.String(50), nullable=False)

# Create the database tables before first request
with app.app_context():
    db.create_all()

# Serve the HTML frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# API endpoint to handle form submissions
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # Check if student already exists to avoid duplicates
    if Student.query.filter_by(student_id=data['studentId']).first():
        return jsonify({"status": "error", "message": "Student ID already exists"}), 400
    if Student.query.filter_by(email=data['email']).first():
        return jsonify({"status": "error", "message": "Email already registered"}), 400

    new_student = Student(
        full_name=data['fullName'],
        email=data['email'],
        student_id=data['studentId'],
        course=data['course']
    )
    
    try:
        db.session.add(new_student)
        db.session.commit()
        return jsonify({"status": "success", "message": "Registration successful"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask Server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
