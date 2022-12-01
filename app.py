from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey # "survey" is our survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []

@app.get("/")
def start_survey():

    return render_template(
        "survey_start.html",
        title=survey.title,
        instructions=survey.instructions
    )

@app.get("/questions/<int:question_number>")
def get_question(question_number):

    # grab question_number
    # access that question from the survey object
    # access the choices from the survey object
    # return a template, passing the question and options to it

    # prompt = survey.questions[question_number].prompt
    # choices = survey.questions[question_number].choices

    question = survey.questions[question_number]

    return render_template("question.html", question=question)
