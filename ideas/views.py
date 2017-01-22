from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from .models import Idea

# Create your views here.

def get_ideas(request, pk):
    ideas = []

    if not pk:
        for idea in Idea.objects.all():
            ideas += [{'id': idea.id, 'category': idea.category, 'text': idea.text, 'likes': idea.likes}]
    else:
        for idea in Idea.objects.filter(category__iexact=pk):
            ideas += [{'id': idea.id, 'category': idea.category, 'text': idea.text, 'likes': idea.likes}]

    return JsonResponse(ideas, safe=False)

@require_POST
def submit_idea(request):
    idea = Idea()

    idea.category = request.POST['category']
    idea.text = request.POST['text']

    idea.save()

    return HttpResponse(idea.category)

@require_POST
def vote_idea(request):
    idea = Idea.objects.get(id=request.POST['idea_id'])

    if request.POST['vote'] == 'up':
        idea.likes += 1
    elif request.POST['vote'] == 'down':
        idea.likes -= 1

    idea.save()

    return HttpResponse(idea.likes)
