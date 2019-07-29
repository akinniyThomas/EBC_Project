from django.db import models

# Create your models here.
class Serie(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Preacher(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TopicSection(models.Model):
    section = models.CharField(max_length=50)

    def __str__(self):
        return self.section

class Message(models.Model):
    topic = models.CharField(max_length=200)
    series = models.ForeignKey(Serie, on_delete=models.PROTECT)
    fileLink = models.URLField(max_length=1000)
    topicSection = models.ManyToManyField(TopicSection)
    preacher = models.ForeignKey(Preacher, on_delete=models.PROTECT)
    dateAndTime = models.DateTimeField('date uploaded')

    def __str__(self):
        return self.topic