from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Article, Tags, Scope

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    # fromset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image',]
    inlines = [ScopeInline, ]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']


