from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table=None,
        ),
        migrations.AlterModelTable(
            name='letting',
            table=None,
        ),
    ]
