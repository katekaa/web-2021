from django.db import models

class Language(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField(max_length=30)
    extension = models.CharField(max_length=20)
    ide = models.CharField(db_column='IDE', max_length=40)  # Field name made lowercase.

    def __str__(self):
        return f'{self.name}'

    class Meta:
        managed = False
        db_table = 'language'

class Library(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField(max_length=30)
    lang = models.ForeignKey('Language', models.DO_NOTHING, db_column='lang_id')

    class Meta:
        managed = False
        db_table = 'library'
