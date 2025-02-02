from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    template = loader.get_template('all_members.html')
    members = Member.objects.all().values()
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('testing.html')
    fruits = ['Apple', 'Orange', 'Lemon']
    context = {
        'fruits': fruits,
        "first_name": 'Costas',
        "last_name": 'Zeimpekis',
        "if_var": 1
    }
    return HttpResponse(template.render(context, request))
