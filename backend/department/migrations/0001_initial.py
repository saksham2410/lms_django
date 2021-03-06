# Generated by Django 2.0.6 on 2019-04-03 09:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[A-Z]{2}[\\d]{3}$', message='not a valid course id')])),
            ],
        ),
        migrations.CreateModel(
            name='CourseOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Course')),
                ('enrolled_students', models.ManyToManyField(to='account.StudentProfile')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.InstructorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('img', 'Image File'), ('vid', 'Video File(.mp4)'), ('pdf', 'PDF File'), ('doc', 'Document Word File'), ('oth', 'Other')], default='pdf', max_length=3)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('course_offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.CourseOffering')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department'),
        ),
    ]
