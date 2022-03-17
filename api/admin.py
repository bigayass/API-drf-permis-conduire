from django.contrib import admin

from . import models

class QuestionInlineModel(admin.TabularInline):
    model = models.Question
    fields = [
        'title',
        'image', 
        ]


@admin.register(models.Serie)

class SerieAdmin(admin.ModelAdmin):
    list_display = [ 
        'title',
        'is_active',
        'date_created'
        ]

    search_fields = ('title',)
    list_filter = ('is_active',)

    inlines = [
        QuestionInlineModel, 
        ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer', 
        'is_right'
        ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'serie',
        'image',
        ]
    list_display = [
        'title', 
        'serie',
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer', 
        'is_right', 
        'question'
        ]

