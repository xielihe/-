# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0004_auto_20180504_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devcompchsample',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='devcompsample',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='devcompsamplefile',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='devcompsamplepeak',
            name='peakEnd',
        ),
        migrations.RemoveField(
            model_name='devcompsamplepeak',
            name='peakStart',
        ),
        migrations.RemoveField(
            model_name='devshapesample',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='explochsample',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='explosample',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='explosamplefile',
            name='isDelete',
        ),
        migrations.RemoveField(
            model_name='explosamplepeak',
            name='peakEnd',
        ),
        migrations.RemoveField(
            model_name='explosamplepeak',
            name='peakStart',
        ),
        migrations.AddField(
            model_name='devcompsamplefile',
            name='handledUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/devCompSampleFile/handled', verbose_name='处理完的文件'),
        ),
        migrations.AddField(
            model_name='devcompsamplepeak',
            name='peakPos',
            field=models.FloatField(default=0, verbose_name='峰高位置'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='backCoordi',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='背景颜色点坐标'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='blackWhiteUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSample/blackWhite/', verbose_name='黑白图像路径'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='boardCheckCoordi',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='主板像素坐标（校验）'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='boardCoordi',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='主板颜色点坐标'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='compCheckCoordi',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='元器件点坐标（校验）'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='featureUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/devShapeSample/feature', verbose_name='特征文件路径'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='interColorUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSample/interColor/', verbose_name='中间彩色图像路径'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='proCoordi',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='前景颜色点坐标'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='rectCoordi',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='矩形框坐标（4个）'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='resultFileUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/devShapeSample/result/', verbose_name='结果文件形式路径'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='resultPicUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSample/result/', verbose_name='结果图像形式路径'),
        ),
        migrations.AddField(
            model_name='explosamplefile',
            name='handledUrl',
            field=models.FileField(blank=True, null=True, upload_to='file/exploSampleFile/handled', verbose_name='处理完的文件'),
        ),
        migrations.AddField(
            model_name='explosamplepeak',
            name='peakPos',
            field=models.FloatField(default=0, verbose_name='峰高位置'),
        ),
        migrations.AlterField(
            model_name='devcompchsample',
            name='devCompSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devCompChSample', to='samples.devCompSample', verbose_name='对应的样本'),
        ),
        migrations.AlterField(
            model_name='devcompsamplefile',
            name='devCompSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devCompSampleFile', to='samples.devCompSample', verbose_name='对应的样本'),
        ),
        migrations.AlterField(
            model_name='devcompsamplepeak',
            name='devCompSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devCompSamplePeak', to='samples.devCompSampleFile', verbose_name='对应的物证文件'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='nomUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSample/nom/', verbose_name='归一化图像文件路径'),
        ),
        migrations.AlterField(
            model_name='devshapesample',
            name='originalUrl',
            field=models.ImageField(blank=True, null=True, upload_to='image/devShapeSample/original/', verbose_name='原始图像文件路径'),
        ),
        migrations.AlterField(
            model_name='explochsample',
            name='exploSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploChSample', to='samples.exploSample', verbose_name='对应的炸药'),
        ),
        migrations.AlterField(
            model_name='explosamplepeak',
            name='exploSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploSamplePeak', to='samples.exploSampleFile', verbose_name='对应的炸药文件'),
        ),
    ]
