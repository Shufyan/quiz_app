from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    objects = models.Manager()

    def __str__(self):
        return str(self.topic_text)


class Question(models.Model):
    quiz_topic = models.ForeignKey(Topic, related_name="questions", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return str(self.question_text)

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return str(self.choice_text)