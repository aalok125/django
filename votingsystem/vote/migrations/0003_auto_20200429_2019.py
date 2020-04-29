# Generated by Django 3.0.5 on 2020-04-29 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_answer_guestuser_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, unique=True)),
                ('slug', models.CharField(max_length=225, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Answer')),
                ('guest_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.GuestUser')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserSearchLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('guest_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.GuestUser')),
            ],
        ),
        migrations.CreateModel(
            name='GuestUserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('guest_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.GuestUser')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='vote.Tag'),
        ),
    ]
