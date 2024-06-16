from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


# The index() view is a placeholder for the index view for the polls application.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# The detail() view is a placeholder for the detail view for a question.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# The results() view is a placeholder for the results view for a question.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# The vote() view is a placeholder for the vote action for a question.
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
