# Generated by Django 3.0.7 on 2020-06-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_de_nascimento',
            field=models.DateField(verbose_name='data de nascimento'),
        ),
        migrations.AddConstraint(
            model_name='usuario',
            constraint=models.UniqueConstraint(fields=('login',), name='unique_login'),
        ),
        migrations.AddConstraint(
            model_name='usuario_possui_perfil',
            constraint=models.UniqueConstraint(fields=('usuario', 'perfil'), name='unique_usuario_perfil'),
        ),
    ]