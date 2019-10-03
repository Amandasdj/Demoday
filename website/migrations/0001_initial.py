# Generated by Django 2.2.6 on 2019-10-03 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('tema', models.CharField(max_length=15)),
                ('valor', models.TextField(max_length=240)),
                ('total', models.PositiveIntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
                ('criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='avatar/')),
                ('user', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=15)),
                ('sobrenome', models.CharField(max_length=15)),
                ('mensagem', models.CharField(default='', max_length=50)),
                ('senha', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=14)),
                ('ativo', models.BooleanField(default=True)),
                ('criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.TextField(max_length=240)),
                ('total', models.PositiveIntegerField(default=0)),
                ('ativo', models.BooleanField(default=True)),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Perfil')),
                ('desafio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Desafio')),
                ('likes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Like')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Perfil'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Perfil'),
        ),
        migrations.AddField(
            model_name='desafio',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Like'),
        ),
    ]
