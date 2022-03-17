from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Serie(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default=_("New Serie"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

    @property
    def all_questions(self):
    	return self.questions.all()


class Question(models.Model):

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serie = models.ForeignKey(Serie, related_name='questions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    image = models.ImageField(upload_to='quiz_imgs/', verbose_name=_("Question Image"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        return self.title

    @property
    def all_answers(self):
    	return self.answers.all()



class Answer(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
