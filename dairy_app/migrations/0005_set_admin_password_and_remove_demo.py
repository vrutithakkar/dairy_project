from django.db import migrations


def set_admin_password_and_remove_demo(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        admin = User.objects.filter(username='admin').first()
        if admin:
            admin.set_password('admin@123')
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()
    except Exception:
        pass

    # remove demo user if exists
    try:
        User.objects.filter(username='user').delete()
    except Exception:
        pass


def reverse_func(apps, schema_editor):
    # no reverse action
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('dairy_app', '0004_create_demo_user'),
    ]

    operations = [
        migrations.RunPython(set_admin_password_and_remove_demo, reverse_func),
    ]
