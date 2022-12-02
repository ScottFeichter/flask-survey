# Question("Have you shopped here before?")

class Question:
    """Question on a questionnaire."""

    def __init__(self, prompt, choices=('Yes', 'No'), allow_text=False):
        """Create question (assume Yes/No for choices).

        prompt = prompt text
        choices = iterable, like ["Yes", "No", "Maybe"]
        allow_text = T/F to control free-form textual explanation
        """
        
        self.prompt = prompt
        self.choices = choices
        self.allow_text = allow_text

        # should question be prompt?
        # how do we play in ipython3 (mem address)
        # can you debug the templates?



class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire.

        instructions = textual instructions
        question = list of Question instances: [q1, q2, ...]
        """


        self.title = title
        self.instructions = instructions
        self.questions = questions

    def __repr__(self):
        return f"<Survey  title={self.title} instructions={self.instructions} questions={self.questions}>"

satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question(
            "On average, how much do you spend a month on frisbees?",
            ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question(
            "Do you prefer porcupines or hedgehogs?",
            ["Porcupines", "Hedgehogs"]),
        Question(
            "Which is the worst function name, and why?",
            ["do_stuff()", "run_me()", "wtf()"],
            allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}
