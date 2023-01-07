from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from collections import Counter

from .models import Article, Tags, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        sc = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main'] == True:
                sc += 1
        if sc > 1:
            raise ValidationError('Главным может быть только один тэг')
        elif sc == 0:
            raise ValidationError('Выберите главный тэг')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image',]
    inlines = [ScopeInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']