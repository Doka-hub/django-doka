from django.shortcuts import render

from .models import Post


def main(request):
    post_name = request.GET.get('post_name')

    if post_name:
        post_list = Post.objects.filter(title__contains=post_name)
    else:
        post_list = Post.objects.all()

    context = {
        'post_list': post_list
    }
    return render(request, 'base.html', context)
