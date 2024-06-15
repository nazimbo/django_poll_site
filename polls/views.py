from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
