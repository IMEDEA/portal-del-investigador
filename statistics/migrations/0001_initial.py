# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'statistics_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number_valid_cvn', self.gf('django.db.models.fields.IntegerField')()),
            ('computable_members', self.gf('django.db.models.fields.IntegerField')()),
            ('total_members', self.gf('django.db.models.fields.IntegerField')()),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'statistics', ['Department'])

        # Adding model 'Area'
        db.create_table(u'statistics_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=40)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number_valid_cvn', self.gf('django.db.models.fields.IntegerField')()),
            ('computable_members', self.gf('django.db.models.fields.IntegerField')()),
            ('total_members', self.gf('django.db.models.fields.IntegerField')()),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'statistics', ['Area'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'statistics_department')

        # Deleting model 'Area'
        db.delete_table(u'statistics_area')


    models = {
        u'statistics.area': {
            'Meta': {'object_name': 'Area'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'computable_members': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'number_valid_cvn': ('django.db.models.fields.IntegerField', [], {}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'total_members': ('django.db.models.fields.IntegerField', [], {})
        },
        u'statistics.department': {
            'Meta': {'object_name': 'Department'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'computable_members': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'number_valid_cvn': ('django.db.models.fields.IntegerField', [], {}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'total_members': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['statistics']