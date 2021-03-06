# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 08:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='explosamplefile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='explosample',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='explochsample',
            name='exploSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.exploSample', verbose_name='对应的炸药'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='devcompsamplepeak',
            name='devCompSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.devCompSampleFile', verbose_name='对应的物证文件'),
        ),
        migrations.AddField(
            model_name='devcompsamplefile',
            name='devCompSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.devCompSample', verbose_name='对应的样本'),
        ),
        migrations.AddField(
            model_name='devcompsamplefile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='devcompsample',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='devcompchsample',
            name='devCompSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.devCompSample', verbose_name='对应的样本'),
        ),
    ]
