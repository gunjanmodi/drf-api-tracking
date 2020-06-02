# Generated by Django 2.2 on 2020-06-02 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('rest_framework_tracking', '0009_auto_20200505_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='apirequestlog',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apirequestlog',
            name='object_id',
            field=models.PositiveIntegerField(),
            preserve_default=False,
        ),
    ]