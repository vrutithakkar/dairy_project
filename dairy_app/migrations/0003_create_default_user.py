from django.db import migrations


def create_default_user(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    username = 'admin'
    password = 'admin123'
    email = 'admin@example.com'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)


def remove_default_user(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.filter(username='admin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_app', '0002_remove_dailyentry_animal_remove_animal_breed_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_user, remove_default_user),
    ]
