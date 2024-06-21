from django.urls import path

from . import views

# The app_name attribute is used to help Django distinguish between different apps that have the same URL patterns.
app_name = "polls"

# The following code maps URL patterns to views.
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
