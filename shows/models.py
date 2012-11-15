# encoding: utf-8
from django.db import models

class Actor(models.Model):
	ACTOR_TYPES = (
		(u'Actor Type 1', u'Actor Type 1'),
		(u'Actor Type 2', u'Actor Type 2'),
		(u'Actor Type 3', u'Actor Type 3'),
		)

	actor_type = models.CharField(max_length=200, 
									choices = ACTOR_TYPES,
									blank=True)
	actor_name = models.CharField(max_length=200, blank=True)
	

	def __unicode__(self):
		return self.actor_name


class Director(models.Model):
	director_name = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.director_name


class Genre(models.Model):
	GENRE_TYPES = (
		(u'Genre Type 1', u'Genre Type 1'),
		(u'Genre Type 2', u'Genre Type 2'),
		(u'Genre Type 3', u'Genre Type 3'),
		)

	genre_type = models.CharField(max_length=200, blank=True)
	
	def __unicode__(self):
		return self.genre_type


class Show(models.Model):
	show_name = models.CharField(max_length=200)
	show_startdate = models.DateField(blank=True, null=True)
	show_current_episode = models.IntegerField(blank=True, null=True)
	show_official_site = models.URLField(blank=True)
	show_rating = models.IntegerField(blank=True, null=True)
	show_trailer = models.CharField(max_length=11, 
									blank=True, 
									help_text=u'Key in the 11 characters Youtube ID. Eg M0jmSsQ5ptw')
	show_actor = models.ManyToManyField(Actor, blank=True, null=True)
	show_director = models.ManyToManyField(Director, blank=True, null=True)
	show_genre = models.ManyToManyField(Genre, blank=True, null=True)

	def __unicode__(self):
	    return self.show_name



class Episode(models.Model):
	episode_number = models.IntegerField()
	episode_name = models.CharField(max_length=200)
	episode_duration = models.IntegerField(blank=True, null=True, 
											help_text=u'Duration of episode in minutes')
	episode_trailer = models.CharField(max_length=11, 
									blank=True, 
									help_text=u'Key in the 11 characters Youtube ID. Eg M0jmSsQ5ptw')
	episode_show = models.ForeignKey(Show)

	def __unicode__(self):
		return self.episode_name



