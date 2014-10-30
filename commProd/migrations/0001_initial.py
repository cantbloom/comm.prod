# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('commProd_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('class_year', self.gf('django.db.models.fields.IntegerField')(default=1933)),
            ('send_mail', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('pic_url', self.gf('django.db.models.fields.CharField')(default='/public/img/placeholder.jpg', max_length=1000)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('data_point_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('use_tour', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('stripe_customer_id', self.gf('django.db.models.fields.CharField')(default='no_id', max_length=1000)),
        ))
        db.send_create_signal('commProd', ['UserProfile'])

        # Adding model 'Email'
        db.create_table('commProd_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75)),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 30, 0, 0), auto_now=True, blank=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(default='ba7bd00e0d7d2751e51cc396c6040ea7766ac399', max_length=40)),
        ))
        db.send_create_signal('commProd', ['Email'])

        # Adding model 'ShirtName'
        db.create_table('commProd_shirtname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('number', self.gf('django.db.models.fields.CharField')(default='', max_length=40)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Human Jizz Rag', max_length=40)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=1933)),
            ('editable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('commProd', ['ShirtName'])

        # Adding model 'CommProdEmail'
        db.create_table('commProd_commprodemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('subject', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('commProd', ['CommProdEmail'])

        # Adding model 'CommProd'
        db.create_table('commProd_commprod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('email_content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.CommProdEmail'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('original_content', self.gf('django.db.models.fields.TextField')()),
            ('media_content', self.gf('django.db.models.fields.TextField')()),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('trending_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('media', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('commProd', ['CommProd'])

        # Adding model 'Rating'
        db.create_table('commProd_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commprod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.CommProd'])),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('previous_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('commProd', ['Rating'])

        # Adding model 'TrendData'
        db.create_table('commProd_trenddata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('avg_score', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('commProd', ['TrendData'])

        # Adding model 'Correction'
        db.create_table('commProd_correction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('commprod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.CommProd'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('commProd', ['Correction'])

        # Adding model 'CorrectionRating'
        db.create_table('commProd_correctionrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('correction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.Correction'])),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('previous_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('commProd', ['CorrectionRating'])

        # Adding model 'Favorite'
        db.create_table('commProd_favorite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('commprod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.CommProd'])),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('fav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('commProd', ['Favorite'])

        # Adding model 'PasswordReset'
        db.create_table('commProd_passwordreset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(default='6ba302b864f7c0d5e0216783d8a9317b61ec7da6', max_length=40)),
        ))
        db.send_create_signal('commProd', ['PasswordReset'])

        # Adding model 'CommProdRec'
        db.create_table('commProd_commprodrec', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['commProd.UserProfile'])),
            ('ranked_list', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('commProd', ['CommProdRec'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('commProd_userprofile')

        # Deleting model 'Email'
        db.delete_table('commProd_email')

        # Deleting model 'ShirtName'
        db.delete_table('commProd_shirtname')

        # Deleting model 'CommProdEmail'
        db.delete_table('commProd_commprodemail')

        # Deleting model 'CommProd'
        db.delete_table('commProd_commprod')

        # Deleting model 'Rating'
        db.delete_table('commProd_rating')

        # Deleting model 'TrendData'
        db.delete_table('commProd_trenddata')

        # Deleting model 'Correction'
        db.delete_table('commProd_correction')

        # Deleting model 'CorrectionRating'
        db.delete_table('commProd_correctionrating')

        # Deleting model 'Favorite'
        db.delete_table('commProd_favorite')

        # Deleting model 'PasswordReset'
        db.delete_table('commProd_passwordreset')

        # Deleting model 'CommProdRec'
        db.delete_table('commProd_commprodrec')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'commProd.commprod': {
            'Meta': {'object_name': 'CommProd'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.CommProdEmail']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'media_content': ('django.db.models.fields.TextField', [], {}),
            'original_content': ('django.db.models.fields.TextField', [], {}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'trending_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.commprodemail': {
            'Meta': {'object_name': 'CommProdEmail'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.TextField', [], {}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.commprodrec': {
            'Meta': {'object_name': 'CommProdRec'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ranked_list': ('django.db.models.fields.TextField', [], {}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.correction': {
            'Meta': {'object_name': 'Correction'},
            'commprod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.CommProd']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.correctionrating': {
            'Meta': {'object_name': 'CorrectionRating'},
            'correction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.Correction']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previous_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.email': {
            'Meta': {'object_name': 'Email'},
            'activation_key': ('django.db.models.fields.CharField', [], {'default': "'ba7bd00e0d7d2751e51cc396c6040ea7766ac399'", 'max_length': '40'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 30, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.favorite': {
            'Meta': {'object_name': 'Favorite'},
            'commprod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.CommProd']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.passwordreset': {
            'Meta': {'object_name': 'PasswordReset'},
            'activation_key': ('django.db.models.fields.CharField', [], {'default': "'6ba302b864f7c0d5e0216783d8a9317b61ec7da6'", 'max_length': '40'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.rating': {
            'Meta': {'object_name': 'Rating'},
            'commprod': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.CommProd']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'previous_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.shirtname': {
            'Meta': {'object_name': 'ShirtName'},
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Human Jizz Rag'", 'max_length': '40'}),
            'number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1933'})
        },
        'commProd.trenddata': {
            'Meta': {'object_name': 'TrendData'},
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['commProd.UserProfile']"})
        },
        'commProd.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'}),
            'avg_score': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'class_year': ('django.db.models.fields.IntegerField', [], {'default': '1933'}),
            'data_point_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic_url': ('django.db.models.fields.CharField', [], {'default': "'/public/img/placeholder.jpg'", 'max_length': '1000'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'send_mail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stripe_customer_id': ('django.db.models.fields.CharField', [], {'default': "'no_id'", 'max_length': '1000'}),
            'use_tour': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['commProd']