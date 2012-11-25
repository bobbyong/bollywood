# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Production_House'
        db.create_table('shows_production_house', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('production_house_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('production_house_slug_name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('shows', ['Production_House'])

        # Deleting field 'Movie.movie_current_episode'
        db.delete_column('shows_movie', 'movie_current_episode')

        # Adding field 'Movie.movie_language'
        db.add_column('shows_movie', 'movie_language',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Removing M2M table for field movie_network on 'Movie'
        db.delete_table('shows_movie_movie_network')

        # Adding M2M table for field movie_production_house on 'Movie'
        db.create_table('shows_movie_movie_production_house', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['shows.movie'], null=False)),
            ('production_house', models.ForeignKey(orm['shows.production_house'], null=False))
        ))
        db.create_unique('shows_movie_movie_production_house', ['movie_id', 'production_house_id'])

    def backwards(self, orm):
        # Deleting model 'Production_House'
        db.delete_table('shows_production_house')

        # Adding field 'Movie.movie_current_episode'
        db.add_column('shows_movie', 'movie_current_episode',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Movie.movie_language'
        db.delete_column('shows_movie', 'movie_language')

        # Adding M2M table for field movie_network on 'Movie'
        db.create_table('shows_movie_movie_network', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['shows.movie'], null=False)),
            ('network', models.ForeignKey(orm['shows.network'], null=False))
        ))
        db.create_unique('shows_movie_movie_network', ['movie_id', 'network_id'])

        # Removing M2M table for field movie_production_house on 'Movie'
        db.delete_table('shows_movie_movie_production_house')

    models = {
        'shows.actor': {
            'Meta': {'object_name': 'Actor'},
            'actor_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'actor_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.director': {
            'Meta': {'object_name': 'Director'},
            'director_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'director_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.episode': {
            'Meta': {'object_name': 'Episode'},
            'episode_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episode_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'episode_number': ('django.db.models.fields.IntegerField', [], {}),
            'episode_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'episode_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'episode_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_slug_type': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'genre_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.movie': {
            'Meta': {'object_name': 'Movie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_abbrev': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'movie_actor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Actor']", 'null': 'True', 'blank': 'True'}),
            'movie_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'movie_director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Director']", 'null': 'True', 'blank': 'True'}),
            'movie_episode': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Episode']", 'null': 'True', 'blank': 'True'}),
            'movie_genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Genre']", 'null': 'True', 'blank': 'True'}),
            'movie_language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'movie_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'movie_official_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'movie_pix1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'movie_pix2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'movie_pix3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'movie_production_house': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Production_House']", 'null': 'True', 'blank': 'True'}),
            'movie_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'movie_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'movie_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'movie_storyline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'movie_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        },
        'shows.network': {
            'Meta': {'object_name': 'Network'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'network_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'shows.production_house': {
            'Meta': {'object_name': 'Production_House'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'production_house_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'production_house_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'shows.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'show_actor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Actor']", 'null': 'True', 'blank': 'True'}),
            'show_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_current_episode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Director']", 'null': 'True', 'blank': 'True'}),
            'show_episode': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Episode']", 'null': 'True', 'blank': 'True'}),
            'show_genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Genre']", 'null': 'True', 'blank': 'True'}),
            'show_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'show_network': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Network']", 'null': 'True', 'blank': 'True'}),
            'show_official_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'show_pix1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_pix2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_pix3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'show_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'show_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'show_storyline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        }
    }

    complete_apps = ['shows']