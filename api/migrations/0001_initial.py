# Generated by Django 4.2.2 on 2023-06-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('salario', models.FloatField(null=True)),
                ('local', models.CharField(max_length=20)),
                ('quantidade', models.IntegerField()),
                ('contato', models.EmailField(max_length=254)),
                ('tipo_contratacao', models.CharField(choices=[('CLT', 'Empregado registrado pela CLT'), ('PJ', 'Pessoa Jurídica')], max_length=3)),
                ('tecnologias', models.ManyToManyField(to='api.tecnologia')),
            ],
        ),
    ]
