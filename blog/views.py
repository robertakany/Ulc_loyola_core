from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST

from blog.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .models import News


def news_list(request):
    news = News.objects.filter(is_deleted=False)
    return render(request, 'blog/news_list.html', {'news': news})


def news_detail(request, news_slug, news_id):
    news = get_object_or_404(News, slug=news_slug, pk=news_id)
    return render(request, 'blog/news_detail.html', {'news': news})





def add_news(request):
    user = request.user
    error = ''

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category', '')
        featured_image = request.FILES.get('featured_image', '/static/assets/images/blog/grid/pic2.png')

        if title and content:
            news = News.objects.create(
                title=title,
                author=user,
                content=content,
                category=category,
                featured_image=featured_image,
            )
            news.save()
            return redirect('news_list')
        else:
            error = 'Les champs invalides'

    return render(request, 'blog/add_news.html', {'error': error})


def news_update(request, news_slug, news_id):
    global data
    news = get_object_or_404(News, slug=news_slug, pk=news_id)
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


def article_delete(request, news_slug, news_id,):
    article = get_object_or_404(News, slug=news_slug, pk=news_id)
    if request.method == 'POST':
        article.is_deleted = True
        article.save()
        return redirect('news_list')
    return render(request, 'blog/news_confirm_delete.html', {'article': article})


def news_content(request,news_id):
    news_content=News.objects.get(id=news_id)
    recent_news = News.objects.all().order_by('-date')[:3]
    comments = Comment.objects.filter(news=news_content)
    popular_news = News.objects.order_by('-views')[:3]
    
    
   # Vérifier si l'utilisateur a déjà vu cette news dans la session
    viewed_news = request.session.get('viewed_news', [])
    if news_id not in viewed_news:
        # Incrémenter le compteur de vues si l'utilisateur n'a pas encore vu cette news
        news_content.add_view()
        viewed_news.append(news_id)
        request.session['viewed_news'] = viewed_news
        
        is_liked = Like.objects.filter(
        news=news_content, user=request.user).exists()

    return render(request, 'blog/news_content.html', locals())


# Vue pour ajouter un commentaire à une news

# views.py


@login_required
@require_http_methods(["POST"])
def toggle_like(request, news_id):
    news = get_object_or_404(News, id=news_id)
    like, created = Like.objects.get_or_create(
        news=news, user=request.user)
    if not created:
        like.is_active = not like.is_active
        like.save()

    likes_count = news.likes.filter(is_active=True).count()

    data = {
        'is_liked': like.is_active,
        'likes_count': likes_count,
    }
    return JsonResponse(data)


@login_required
@require_POST
def add_comment(request,news_pk, *args, **kwargs):
    news = News.get_object_or_404(News, id=news_pk)
    content = request.POST.get('content')

    if content:
        comment = Comment.create(
            news=news, user=request.user,content=content
        )
        data = {
            'user': comment.user.username,
            content: comment.content,
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Content cannot be empty.'})



# Create your views here.
