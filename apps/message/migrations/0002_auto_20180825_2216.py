# Generated by Django 2.1 on 2018-08-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermessage',
            options={'verbose_name': '用户留言信息', 'verbose_name_plural': '用户留言信息'},
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='id',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='object_id',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='主键'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(default='', max_length=500, verbose_name='留言信息'),
        ),
    ]
