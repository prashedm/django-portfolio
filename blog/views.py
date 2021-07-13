from django.shortcuts import render, get_object_or_404
from .models import news

def all_blogs(request):
    News = news.objects.all()#instead of .all() we can say .order_by(-date)[:5]
    return render(request, 'blog/all_blogs.html', {'News':News})
def detail(request, blog_id):
    blog = get_object_or_404(news, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
