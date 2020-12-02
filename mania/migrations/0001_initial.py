from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('registered_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('email', models.EmailField(db_index=True, max_length=250, unique=True)),
                ('username', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_merchant', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=250)),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('apartment', models.CharField(blank=True, max_length=250, null=True)),
                ('building', models.CharField(blank=True, max_length=250, null=True)),
                ('landmark', models.CharField(blank=True, max_length=250, null=True)),
                ('district', models.CharField(default=None, max_length=250)),
                ('state', models.CharField(default=None, max_length=250)),
                ('pincode', models.CharField(default=None, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('mobile', models.CharField(default='', max_length=15)),
                ('fees', models.CharField(max_length=10)),
                ('registration_id', models.CharField(default='', max_length=100, unique=True)),
                ('txn_id', models.CharField(default='', max_length=100)),
                ('txn_amount', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
