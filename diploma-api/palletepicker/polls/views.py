from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
import json
from .modules import quant
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def kmeans(request):
    response_data = {}
    try:
        source = request.GET['source']
    except Exception as e:
        response_data['success'] = False
        response_data['message'] = 'No source'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    try:
        k = int(request.GET['k'])
    except(KeyError, Choice.DoesNotExist):
        response_data['success'] = False
        response_data['message'] = 'No k-value'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    except(KeyError, ValueError):
        response_data['success'] = False
        response_data['message'] = 'Not a number'
        return HttpResponse(json.dumps(response_data), content_type="application/json")


    response_data['success'] = True
    response_data['message'] = 'Get colors'
    center = quant.get_colors(source, k)
    colors = quant.colorsToString(center)
    response_data['colors'] = colors
    return HttpResponse(json.dumps(response_data), content_type="application/json")
