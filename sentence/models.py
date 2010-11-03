from django.db import models
import datetime

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice

class Word(models.Model):
    word = models.CharField(max_length=200)

    def __unicode__(self):
        return self.word 

class Pos(models.Model):
    word = models.ForeignKey(Word)
    pos = models.IntegerField()

    def __unicode__(self):
        return self.pos

class Noun(Word):
    pass

class Verb(Word):
    pass

class Adjective(Word):
    pass

class Preposition(Word):
    pass

class Pronoun(Word):
    pass

class Article(Word):
    pass

