from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kendramoore@localhost:5432/students'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students_data_two'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

 
@app.route('/students', methods=['GET'])
def  get_students():
    students = Student.query.all()
    formatted_students = []
    for stud in students:
        formatted_students.append({'id': stud.id, 'first_name': stud.id, 'last_name': stud.last_name, 'age': stud.age, 'grade': stud.grade})
    return jsonify(formatted_students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    students = Student.query.all()
    old = []
    for stud in students:
        if stud.age > 20:
            old.append({'id': stud.id, 'first_name': stud.id, 'last_name': stud.last_name, 'age': stud.age, 'grade': stud.grade})
    return jsonify(old)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    students = Student.query.all()
    young = []
    for stud in students:
        if stud.age < 21:
            young.append({'id': stud.id, 'first_name': stud.id, 'last_name': stud.last_name, 'age': stud.age, 'grade': stud.grade})
    return jsonify(young)

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    students = Student.query.all()
    advance = []
    for stud in students:
        if stud.age < 21 and stud.grade == 'A':
            advance.append({'id': stud.id, 'first_name': stud.id, 'last_name': stud.last_name, 'age': stud.age, 'grade': stud.grade})
    return jsonify(advance)

@app.route('/student_names', methods=['GET'])
def get_student_names():
    students = Student.query.all()
    advance = []
    for stud in students:
        advance.append({'first_name': stud.first_name, 'last_name': stud.last_name})
    return jsonify(advance)


@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    students = Student.query.all()
    advance = []
    for stud in students:
        student_name = stud.first_name + " " + stud.last_name
        advance.append({'age': stud.age, 'name': student_name})
    return jsonify(advance)

if __name__ == '__main__':
    app.run(debug=True)