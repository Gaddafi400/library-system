# Generated by Django 4.1.3 on 2022-11-12 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0005_alter_contactus_table"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactus", options={"verbose_name_plural": "contactus"},
        ),
        migrations.AlterModelTable(name="contactus", table=None,),
    ]
