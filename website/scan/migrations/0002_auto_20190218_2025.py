from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scan',
            old_name='dia_id',
            new_name='diagnosis',
        ),
        migrations.RenameField(
            model_name='scan',
            old_name='pid',
            new_name='patient',
        ),
    ]
