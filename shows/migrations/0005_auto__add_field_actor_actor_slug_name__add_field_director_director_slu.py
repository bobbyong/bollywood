# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Actor.actor_slug_name'
        db.add_column('shows_actor', 'actor_slug_name',
                      self.gf('django.db.models.fields.SlugField')(default=9999, max_length=50),
                      keep_default=False)

        # Adding field 'Director.director_slug_name'
        db.add_column('shows_director', 'director_slug_name',
                      self.gf('django.db.models.fields.SlugField')(default=9999, max_length=50),
                      keep_default=False)

        # Adding field 'Show.show_slug_name'
        db.add_column('shows_show', 'show_slug_name',
                      self.gf('django.db.models.fields.SlugField')(default=9999, max_length=50),
                      keep_default=False)

        # Adding field 'Episode.episode_slug_name'
        db.add_column('shows_episode', 'episode_slug_name',
                      self.gf('django.db.models.fields.SlugField')(default=9999, max_length=50),
                      keep_default=False)

        # Adding field 'Network.network_slug_name'
        db.add_column('shows_network', 'network_slug_name',
                      self.gf('django.db.models.fields.SlugField')(default=9999, max_length=50),
                      keep_default=False)

        # Adding field 'Genre.genre_slug_type'
        db.add_column('shows_genre', 'genre_slug_type',
                      self.gf('django.db.models.fields.SlugField')(default=9999, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Actor.actor_slug_name'
        db.delete_column('shows_actor', 'actor_slug_name')

        # Deleting field 'Director.director_slug_name'
        db.delete_column('shows_director', 'director_slug_name')

        # Deleting field 'Show.show_slug_name'
        db.delete_column('shows_show', 'show_slug_name')

        # Deleting field 'Episode.episode_slug_name'
        db.delete_column('shows_episode', 'episode_slug_name')

        # Deleting field 'Network.network_slug_name'
        db.delete_column('shows_network', 'network_slug_name')

        # Deleting field 'Genre.genre_slug_type'
        db.delete_column('shows_genre', 'genre_slug_type')


    models = {
        'shows.actor': {
            'Meta': {'object_name': 'Actor'},
            'actor_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'actor_slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.director': {
            'Meta': {'object_name': 'Director'},
            'director_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'director_slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.episode': {
            'Meta': {'object_name': 'Episode'},
            'episode_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episode_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'episode_number': ('django.db.models.fields.IntegerField', [], {}),
            'episode_show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shows.Show']"}),
            'episode_slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'episode_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_slug_type': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'genre_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.network': {
            'Meta': {'object_name': 'Network'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'network_slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'shows.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_actor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Actor']", 'null': 'True', 'blank': 'True'}),
            'show_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_current_episode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Director']", 'null': 'True', 'blank': 'True'}),
            'show_genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Genre']", 'null': 'True', 'blank': 'True'}),
            'show_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'show_network': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Network']", 'null': 'True', 'blank': 'True'}),
            'show_official_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'show_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'show_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'show_storyline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        }
    }

    complete_apps = ['shows']