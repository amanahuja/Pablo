from django.db import models
import datetime

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

class Adverb(Word):
    pass

