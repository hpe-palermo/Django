# Generated by Django 4.2.7 on 2023-11-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_usuarioscomcamposadicionais_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('criador', models.CharField(blank=True, max_length=30, null=True)),
                ('nome', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('alunos', models.ManyToManyField(blank=True, null=True, to='app.usuario')),
            ],
        ),
    ]