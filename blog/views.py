from django.shortcuts import render, redirect
from blog.models import *
from django.shortcuts import render, get_object_or_404, redirect


def news_list(request):
    news = News.objects.filter(is_deleted=False)
    return render(request, 'blog/news_list.html', {'news': news})


def news_detail(request, news_slug, news_id):
    news = get_object_or_404(News, slug=news_slug, pk=news_pk)
    return render(request, 'blog/news_detail.html', {'news': news})


def add_news(request):
    user = request.user
    error = ''
    if request.POST:
        data = request.data, request.FILES
        if data.is_valid():
            print(data)
            news = News.objects.create(
                title=data['title'],
                author=user,
                content=data['content'],
                category=data.get('category', ''),
                featured_image=data.get("featured_image", '/static/assets/images/blog/grid/pic2.png'),
            )
            news.save()
            return redirect('news_list')
        else:
            error = 'Les champs invalides'
        return render(request, 'blog/add_news.html', locals())


def news_update(request, news_slug, news_id):
    global data
    news = get_object_or_404(News, slug=news_slug, pk=news_pk)
    if request.method == 'POST':
        data = request.POST, request.FILES
        if data.is_valid():
            news.title = data.get('title')
            news.content = data.get('content')
            featured_image = data.get('featured_image', 'default_image.jpg')
            news.featured_image = featured_image
            news.category = data.get('category')
            news.save()
            return redirect('news_list')
    return render(request, 'blog/news_update.html', locals())


def article_delete(request, news_slug, news_pk, pk):
    article = get_object_or_404(News, slug=news_slug, pk=news_pk)
    if request.method == 'POST':
        article.is_deleted = True
        article.save()
        return redirect('news_list')
    return render(request, 'blog/news_confirm_delete.html', {'article': article})

# Create your views here.
