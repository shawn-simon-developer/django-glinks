# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blueprint'
        db.create_table(u'glinks_blueprint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'glinks', ['Blueprint'])

        # Adding model 'Glink'
        db.create_table(u'glinks_glink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blueprint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glinks.Blueprint'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('isActive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=9)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 2, 5, 0, 0), null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('clicks', self.gf('django.db.models.fields.BigIntegerField')(default=0, blank=True)),
            ('impressions', self.gf('django.db.models.fields.BigIntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'glinks', ['Glink'])

        # Adding model 'ImpressionTracking'
        db.create_table(u'glinks_impressiontracking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('glink_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glinks.Glink'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'glinks', ['ImpressionTracking'])

        # Adding model 'ClickTracking'
        db.create_table(u'glinks_clicktracking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('glink_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glinks.Glink'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'glinks', ['ClickTracking'])

        # Adding model 'SpamBlockList'
        db.create_table(u'glinks_spamblocklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'glinks', ['SpamBlockList'])


    def backwards(self, orm):
        # Deleting model 'Blueprint'
        db.delete_table(u'glinks_blueprint')

        # Deleting model 'Glink'
        db.delete_table(u'glinks_glink')

        # Deleting model 'ImpressionTracking'
        db.delete_table(u'glinks_impressiontracking')

        # Deleting model 'ClickTracking'
        db.delete_table(u'glinks_clicktracking')

        # Deleting model 'SpamBlockList'
        db.delete_table(u'glinks_spamblocklist')


    models = {
        u'glinks.blueprint': {
            'Meta': {'object_name': 'Blueprint'},
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'glinks.clicktracking': {
            'Meta': {'object_name': 'ClickTracking'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'glink_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glinks.Glink']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'glinks.glink': {
            'Meta': {'object_name': 'Glink'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'blueprint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glinks.Blueprint']", 'null': 'True'}),
            'clicks': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'impressions': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'blank': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 5, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '9'})
        },
        u'glinks.impressiontracking': {
            'Meta': {'object_name': 'ImpressionTracking'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'glink_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glinks.Glink']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'glinks.spamblocklist': {
            'Meta': {'object_name': 'SpamBlockList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['glinks']