from flask import Flask, render_template, request, redirect, url_for

from database import (
    create_table,
    add_student,
    get_students,
    get_student,
    update_student,
    delete_student
)

app = Flask(__name__)


# Home page
@app.route("/")
def index():
    students = get_students()
    return render_template("index.html", students=students)


# Add student
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]

        add_student(name, age, course, email)

        return redirect(url_for("index"))

    return render_template("add_student.html")


# View student
@app.route("/view/<int:id>")
def view(id):
    student = get_student(id)
    return render_template("view_students.html", student=student)


# Edit student
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    student = get_student(id)

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]
        email = request.form["email"]

        update_student(id, name, age, course, email)

        return redirect(url_for("index"))

    return render_template("edit_student.html", student=student)


# Delete student
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    delete_student(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    create_table()
    app.run(debug=True)