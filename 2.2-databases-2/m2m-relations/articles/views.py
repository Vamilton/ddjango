from django.shortcuts import render

from articles.models import Article, Tags, Scope


def articles_list(request):
    template = 'articles/news.html'
    news = Article.objects.order_by('-published_at')
    context = {
        'object_list': news
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    for article in news:
        print(article.scopes.all())
        for scope in article.scopes.all():
            print(scope.tags.name)


    return render(request, template, context)
