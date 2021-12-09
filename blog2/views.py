from django.shortcuts import render
from django.http import HttpResponse
from blog2.models import Posts


def title(request):
    return HttpResponse('Title:')


def description(request):
    return HttpResponse('Description:')


def comments(request):
    return HttpResponse('Comments:')


def get_real_posts(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'post_list.html', context)
