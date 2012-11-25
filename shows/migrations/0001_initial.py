# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actor'
        db.create_table('shows_actor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor_type', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('actor_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('shows', ['Actor'])

        # Adding model 'Director'
        db.create_table('shows_director', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('director_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('shows', ['Director'])

        # Adding model 'Genre'
        db.create_table('shows_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre_type', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('shows', ['Genre'])

        # Adding model 'Show'
        db.create_table('shows_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('show_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('show_startdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('show_current_episode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('show_official_site', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('show_rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('show_trailer', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
        ))
        db.send_create_signal('shows', ['Show'])

        # Adding M2M table for field show_actor on 'Show'
        db.create_table('shows_show_show_actor', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['shows.show'], null=False)),
            ('actor', models.ForeignKey(orm['shows.actor'], null=False))
        ))
        db.create_unique('shows_show_show_actor', ['show_id', 'actor_id'])

        # Adding M2M table for field show_director on 'Show'
        db.create_table('shows_show_show_director', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['shows.show'], null=False)),
            ('director', models.ForeignKey(orm['shows.director'], null=False))
        ))
        db.create_unique('shows_show_show_director', ['show_id', 'director_id'])

        # Adding M2M table for field show_genre on 'Show'
        db.create_table('shows_show_show_genre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['shows.show'], null=False)),
            ('genre', models.ForeignKey(orm['shows.genre'], null=False))
        ))
        db.create_unique('shows_show_show_genre', ['show_id', 'genre_id'])

        # Adding model 'Episode'
        db.create_table('shows_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episode_number', self.gf('django.db.models.fields.IntegerField')()),
            ('episode_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('episode_duration', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('episode_show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shows.Show'])),
        ))
        db.send_create_signal('shows', ['Episode'])


    def backwards(self, orm):
        # Deleting model 'Actor'
        db.delete_table('shows_actor')

        # Deleting model 'Director'
        db.delete_table('shows_director')

        # Deleting model 'Genre'
        db.delete_table('shows_genre')

        # Deleting model 'Show'
        db.delete_table('shows_show')

        # Removing M2M table for field show_actor on 'Show'
        db.delete_table('shows_show_show_actor')

        # Removing M2M table for field show_director on 'Show'
        db.delete_table('shows_show_show_director')

        # Removing M2M table for field show_genre on 'Show'
        db.delete_table('shows_show_show_genre')

        # Deleting model 'Episode'
        db.delete_table('shows_episode')


    models = {
        'shows.actor': {
            'Meta': {'object_name': 'Actor'},
            'actor_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'actor_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.director': {
            'Meta': {'object_name': 'Director'},
            'director_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.episode': {
            'Meta': {'object_name': 'Episode'},
            'episode_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episode_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'episode_number': ('django.db.models.fields.IntegerField', [], {}),
            'episode_show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shows.Show']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'shows.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_actor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Actor']", 'null': 'True', 'blank': 'True'}),
            'show_current_episode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_director': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Director']", 'null': 'True', 'blank': 'True'}),
            'show_genre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shows.Genre']", 'null': 'True', 'blank': 'True'}),
            'show_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'show_official_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'show_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show_startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'show_trailer': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        }
    }

    complete_apps = ['shows']