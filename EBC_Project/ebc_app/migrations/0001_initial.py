# Generated by Django 2.2.3 on 2019-07-29 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TopicSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('fileLink', models.URLField(max_length=1000)),
                ('dateAndTime', models.DateTimeField()),
                ('preacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ebc_app.Preacher')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ebc_app.Serie')),
                ('topicSection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ebc_app.TopicSection')),
            ],
        ),
    ]