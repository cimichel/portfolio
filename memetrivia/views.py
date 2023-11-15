from django.shortcuts import render
from memetrivia.models import MemeTrivia


def trivia_index(request):
    trivia_questions = MemeTrivia.objects.all()
    context = {
        "trivia_questions": trivia_questions
    }
    return render(request, "trivia/trivia.html", context)
