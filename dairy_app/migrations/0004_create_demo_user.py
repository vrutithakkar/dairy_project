from django.db import migrations


def create_demo_user(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    username = 'user'
    password = 'admin123'
    email = 'user@example.com'
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, email=email, password=password)


def remove_demo_user(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    User.objects.filter(username='user').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_app', '0003_create_default_user'),
    ]

    operations = [
        migrations.RunPython(create_demo_user, remove_demo_user),
    ]
