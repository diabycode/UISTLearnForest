from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.base import ContextMixin

from .models import Cours, Video, Article


class CoursList(ListView):
    model = Cours
    template_name = 'cours/cours_list.html'
    context_object_name = 'cours_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cours_list"] = Cours.objects.all().order_by('-create_at')

        return context


class CoursDetail(DetailView):
    model = Cours
    template_name = 'cours/cours_details.html'
    context_object_name = 'cours'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["short_desc"] = self.object.description.split(".")[0]
        context["full_desc"] = " ".join(self.object.description.split(".")[1:])

        return context



class CoursLearn(View, TemplateResponseMixin, ContextMixin):
    template_name = 'cours/cours_learn.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cours'] = Cours.objects.get(slug=self.kwargs['slug'])
        return context
    



def get(request) -> JsonResponse:
    """Return a list of all courses.
    """

    cours_serealized = [
        {
            'id': c.pk,
            'title': c.title,
            'description': c.description,
            'create_at': c.create_at,
        }

        for c in Cours.objects.all()
    ]

    response = JsonResponse({
        'cours': cours_serealized
    })
    return response
    


def get_item(request, pk, type) -> JsonResponse:
    items = Video.objects.all() if type == 'video' else Article.objects.all()
    item = items.get(pk=pk)

    if item is None:
        return JsonResponse({
            'object': {},
            'status': 'error',
            'error': 'Item not found'
        })

    item_data = {
        'status': 'ok',
        'object': {
            'id': item.pk,
            'title': item.title,
            'type': item.type,
            'create_at': item.create_at,
        }
    }

    if item.type == 'video':
        item_data['object']['source'] = item.video_source
        item_data['object']['description'] = item.description
    else:
        item_data['object']['content'] = item.content

    response = JsonResponse(item_data)
    return response