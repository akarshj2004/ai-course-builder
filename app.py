from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    course = ""

    if request.method == "POST":
        topic = request.form["topic"]

        course = f"""
        Course Title: {topic}

        Lesson 1: Introduction
        Lesson 2: Basics
        Lesson 3: Intermediate Concepts
        Lesson 4: Practical Examples
        Lesson 5: Advanced Concepts
        """

    return render_template("index.html", course=course)


if __name__ == "__main__":
    app.run(debug=True)