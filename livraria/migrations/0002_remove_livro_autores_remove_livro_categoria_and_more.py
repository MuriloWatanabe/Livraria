# Generated by Django 4.2.3 on 2023-08-08 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('livraria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='autores',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='editora',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='preco',
        ),
        migrations.RemoveField(
            model_name='livro',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]