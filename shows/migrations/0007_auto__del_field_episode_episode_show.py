# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field show_episode on 'Show'
        db.create_table('shows_show_show_episode', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['shows.show'], null=False)),
            ('episode', models.ForeignKey(orm['shows.episode'], null=False))
        ))
        db.create_unique('shows_show_show_episode', ['show_id', 'episode_id'])

        # Deleting field 'Episode.episode_show'
        db.delete_column('shows_episode', 'episode_show_id')


    def backwards(self, orm):
        # Removing M2M table for field show_episode on 'Show'
        db.delete_table('shows_show_show_episode')

        # Adding field 'Episode.episode_show'
        db.add_column('shows_episode', 'episode_show',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='deleted', to=orm['shows.Show']),
                      keep_default=False)


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
        'shows.network': {
            'Meta': {'object_name': 'Network'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'network_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'shows.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_actor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Actor']", 'null': 'True', 'blank': 'True'}),
            'show_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'show_current_episode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Director']", 'null': 'True', 'blank': 'True'}),
            'show_episode': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Episode']", 'null': 'True', 'blank': 'True'}),
            'show_genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Genre']", 'null': 'True', 'blank': 'True'}),
            'show_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'show_network': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Network']", 'null': 'True', 'blank': 'True'}),
            'show_official_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'show_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_slug_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'show_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'show_storyline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        }
    }

    complete_apps = ['shows']