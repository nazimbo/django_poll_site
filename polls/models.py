from django.db import models

# The following code defines the database schema for the polls application.
# It creates the following tables:


# - Question
class Question(models.Model):
    # Each field is represented by an instance of a Field class.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # The __str__() method is the default human-readable representation of the object.
    def __str__(self):
        return self.question_text


# - Choice
class Choice(models.Model):
    # The ForeignKey tells Django that each Choice is related to a single Question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
