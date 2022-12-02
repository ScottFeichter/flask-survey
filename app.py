from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey # "survey" is our survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

RESPONSES = [] # ['Yes', 'No', 'Less than $10,000', 'Yes']

@app.get("/")
def start_survey():
    """create begin survey page with title and instructions"""

    RESPONSES = []

    return render_template(
        "survey_start.html",
        title=survey.title,
        instructions=survey.instructions
    )

@app.post("/begin")
def get_question_zero():
    """redirect to first question of the survey"""

    return redirect("/questions/0")

@app.get("/questions/<int:question_number>")
def get_question(question_number):
    """get new question, based on value passed in url"""

    question = survey.questions[question_number]

    return render_template("question.html", question=question)

@app.post("/answer")
def receive_answer():
    """handle answer submission - add to responses and render next question"""

    answer = request.form.get("answer")
    RESPONSES.append(answer)

    if len(RESPONSES) >= len(survey.questions):
        return redirect("/completion")

    return redirect(f"/questions/{len(RESPONSES)}")

@app.get("/completion")
def show_end_page():
    """show end page of the survey, with summary"""

    return render_template(
        "completion.html", 
        questions=survey.questions, 
        survey_responses=RESPONSES, 
        length=range(len(survey.questions))
    )
