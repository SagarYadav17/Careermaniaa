# Generated by Django 3.1.4 on 2021-01-04 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mania', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='coaching_branch_name')),
                ('branch_type', models.CharField(default='Main', max_length=250, verbose_name='coaching_branch')),
            ],
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('logo', models.ImageField(null=True, upload_to='')),
                ('registration_number', models.CharField(default=None, max_length=50)),
                ('country', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('address', models.CharField(default=None, max_length=50)),
                ('director_name', models.CharField(default=None, max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default=None, max_length=200)),
                ('rating', models.IntegerField(default=None)),
                ('review_time', models.DateTimeField(auto_now_add=True)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_app.coaching')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('description', models.CharField(default=None, max_length=200)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_app.coaching')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default=None, max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_type', models.CharField(default=None, max_length=10)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('stream', models.CharField(default=None, max_length=250, verbose_name='coaching_stream')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobRecruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.BigIntegerField()),
                ('registration_no', models.CharField(default=None, max_length=50)),
                ('company_name', models.CharField(default=None, max_length=100)),
                ('company_address', models.CharField(default=None, max_length=500)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('country', models.CharField(default=None, max_length=50)),
                ('director_name', models.CharField(default=None, max_length=50)),
                ('industry_type', models.CharField(default=None, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50)),
                ('skills', models.CharField(default=None, max_length=100)),
                ('available_posts', models.PositiveIntegerField(default=1)),
                ('description', models.TextField()),
                ('job_type', models.CharField(default='Full Time', max_length=50)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_app.jobrecruiter')),
            ],
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_of', to='mania.address')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc_code', models.CharField(default=None, max_length=20)),
                ('description', models.CharField(default=None, max_length=200)),
                ('disc_percent', models.IntegerField(default=None)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_app.coaching')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='branch_course_name')),
                ('timePeriod', models.CharField(default=None, max_length=20)),
                ('trial', models.CharField(default='Not Available', max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('syllabus', models.FileField(blank=True, null=True, upload_to='')),
                ('fees', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('currency', models.CharField(blank=True, default='INR', max_length=30)),
                ('is_active', models.BooleanField(default=False)),
                ('stream', models.CharField(default=None, max_length=250, verbose_name='coaching_stream')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_of', to='merchant_app.branch')),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchant_app.coaching')),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(default=None, max_length=50)),
                ('contact_no', models.BigIntegerField()),
                ('college_name', models.CharField(default=None, max_length=255)),
                ('university_type', models.CharField(default=None, max_length=50)),
                ('institute_type', models.CharField(default=None, max_length=50)),
                ('chairman', models.CharField(default=None, max_length=50)),
                ('college_address', models.CharField(default=None, max_length=255)),
                ('country', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('city', models.CharField(default=None, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoachingReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.BigIntegerField()),
                ('description', models.CharField(default=None, max_length=250)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_of', to='merchant_app.coaching')),
            ],
        ),
        migrations.CreateModel(
            name='CoachingMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(default=None, max_length=250)),
                ('owner_image', models.ImageField(default=None, upload_to='owners/')),
                ('established_on', models.DateField()),
                ('mobile', models.BigIntegerField()),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metadata_of', to='merchant_app.coaching')),
            ],
        ),
        migrations.CreateModel(
            name='CoachingFacultyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.BigIntegerField()),
                ('specialization', models.CharField(max_length=250)),
                ('faculty_image', models.ImageField(default=None, upload_to='faculties/')),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_of', to='merchant_app.coaching')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='coaching',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='merchant_app.coaching'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(auto_now_add=True)),
                ('check_out', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending for Approval', 'Pending for Approval'), ('Awaiting', 'Awaiting'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default=None, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='course_batch_name')),
                ('start_time', models.CharField(default=None, max_length=20)),
                ('end_time', models.CharField(default=None, max_length=20)),
                ('student_limit', models.BigIntegerField(blank=True, null=True)),
                ('students_enrolled', models.BigIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batches_of', to='merchant_app.course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaches', to='merchant_app.coachingfacultymember')),
            ],
        ),
        migrations.CreateModel(
            name='BankAccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(default=None, max_length=30)),
                ('ifsc_code', models.CharField(default=None, max_length=20)),
                ('bank_name', models.CharField(default=None, max_length=50)),
                ('account_holder', models.CharField(default=None, max_length=100)),
                ('adhar_card', models.FileField(default=None, upload_to='adhar_cards/')),
                ('pan_card', models.FileField(default=None, upload_to='pan_cards/')),
                ('mobile_no', models.CharField(default=None, max_length=20)),
                ('coaching', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='merchant_app.coaching')),
            ],
        ),
    ]
