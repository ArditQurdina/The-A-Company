# Generated by Django 4.0.6 on 2022-07-25 12:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('profile', models.ImageField(default='download.jpg', upload_to='profile')),
                ('cover', models.ImageField(default='default.png', upload_to='cover')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('profileSetup', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.city')),
            ],
        ),
        migrations.CreateModel(
            name='UserLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('Limited working proficiency', 'Limited working proficiency'), ('Full professional proficiency', 'Full professional proficiency'), ('Native or bilingual proficiency', 'Native or bilingual proficiency'), ('Professional working proficiency', 'Professional working proficiency'), ('Elementary proficiency', 'Elementary proficiency')], max_length=255)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.languages')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserExperiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country')),
                ('city_usExp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.city')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('field_of_study', models.CharField(max_length=255)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField(blank=True, null=True)),
                ('total_examples_passed', models.IntegerField(default=0)),
                ('GPA', models.FloatField(default=0.0)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.university')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('salary_per_hour', models.IntegerField()),
                ('type_of_work', models.CharField(choices=[('Full Time', 'Full Time')], max_length=50)),
                ('hour_per_work', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('housing', models.CharField(choices=[('Provided', 'Provided')], max_length=50)),
                ('housing_cost_per_week', models.IntegerField()),
                ('program', models.CharField(choices=[('Work And Travel', 'Work And Travel')], max_length=50)),
                ('programCost', models.IntegerField()),
                ('logo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], default='Open', max_length=20)),
                ('postDate', models.DateField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
                ('city_j', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.city')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.country'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField()),
                ('status', models.CharField(choices=[('Pennding', 'Pennding'), ('Read', 'Read')], max_length=50)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.jobs')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
