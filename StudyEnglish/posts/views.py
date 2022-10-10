from django.shortcuts import render


def all_posts(request):
    return render(request, 'posts/all_posts.html')
