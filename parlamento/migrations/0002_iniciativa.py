# Generated by Django 2.2.3 on 2019-07-30 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parlamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iniciativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('description', models.TextField()),
                ('sinopsis', models.TextField()),
                ('type_presentation', models.CharField(choices=[('GROUP', 'De grupo'), ('ADHERENT', 'Adherente'), ('INITIATOR', 'Iniciante'), ('DIVGROUP', 'Diversos grupos parlamentarios')], max_length=50)),
                ('status', models.CharField(choices=[('APPROVED', 'Aprobada'), ('ATTENDED', 'Atendidas'), ('REJECTED', 'Desechadas'), ('DECLINED', 'Retiradas'), ('PENDING', 'Pendientes')], max_length=20)),
                ('date_presentation', models.DateTimeField()),
                ('date_status', models.DateTimeField()),
                ('diputado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parlamento.Diputado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
