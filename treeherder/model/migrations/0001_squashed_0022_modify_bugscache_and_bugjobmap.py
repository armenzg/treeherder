# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-08 11:41
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RepositoryGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'repository_group',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('dvcs_type', models.CharField(db_index=True, max_length=25)),
                ('url', models.CharField(max_length=255)),
                ('branch', models.CharField(db_index=True, max_length=50, null=True)),
                ('codebase', models.CharField(blank=True, db_index=True, max_length=50)),
                ('description', models.TextField(blank=True)),
                (
                    'active_status',
                    models.CharField(blank=True, db_index=True, default='active', max_length=7),
                ),
                ('performance_alerts_enabled', models.BooleanField(default=False)),
                (
                    'repository_group',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.RepositoryGroup'
                    ),
                ),
                ('expire_performance_data', models.BooleanField(default=True)),
                ('is_try_repo', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'repository',
                'verbose_name_plural': 'repositories',
            },
        ),
        migrations.CreateModel(
            name='Push',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('revision', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=150)),
                ('time', models.DateTimeField(db_index=True)),
                (
                    'repository',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Repository'
                    ),
                ),
            ],
            options={
                'db_table': 'push',
            },
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('revision', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=150)),
                ('comments', models.TextField()),
                (
                    'push',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='commits',
                        to='model.Push',
                    ),
                ),
            ],
            options={
                'db_table': 'commit',
            },
        ),
        migrations.CreateModel(
            name='Bugscache',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(db_index=True, max_length=64)),
                ('resolution', models.CharField(blank=True, db_index=True, max_length=64)),
                ('summary', models.CharField(max_length=255)),
                ('crash_signature', models.TextField(blank=True)),
                ('keywords', models.TextField(blank=True)),
                ('os', models.CharField(blank=True, max_length=64)),
                ('modified', models.DateTimeField()),
                ('whiteboard', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'bugscache',
                'verbose_name_plural': 'bugscache',
            },
        ),
        migrations.CreateModel(
            name='BuildPlatform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('os_name', models.CharField(max_length=25)),
                ('platform', models.CharField(db_index=True, max_length=100)),
                ('architecture', models.CharField(blank=True, db_index=True, max_length=25)),
            ],
            options={
                'db_table': 'build_platform',
            },
        ),
        migrations.CreateModel(
            name='ClassifiedFailure',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bug_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'classified_failure',
            },
        ),
        migrations.CreateModel(
            name='FailureClassification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'failure_classification',
            },
        ),
        migrations.CreateModel(
            name='JobGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(db_index=True, default='?', max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'job_group',
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(db_index=True, default='?', max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'job_type',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'machine',
            },
        ),
        migrations.CreateModel(
            name='MachinePlatform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('os_name', models.CharField(max_length=25)),
                ('platform', models.CharField(db_index=True, max_length=100)),
                ('architecture', models.CharField(blank=True, db_index=True, max_length=25)),
            ],
            options={
                'db_table': 'machine_platform',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ReferenceDataSignatures',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('signature', models.CharField(db_index=True, max_length=50)),
                ('build_os_name', models.CharField(db_index=True, max_length=25)),
                ('build_platform', models.CharField(db_index=True, max_length=100)),
                ('build_architecture', models.CharField(db_index=True, max_length=25)),
                ('machine_os_name', models.CharField(db_index=True, max_length=25)),
                ('machine_platform', models.CharField(db_index=True, max_length=100)),
                ('machine_architecture', models.CharField(db_index=True, max_length=25)),
                ('job_group_name', models.CharField(blank=True, db_index=True, max_length=100)),
                ('job_group_symbol', models.CharField(blank=True, db_index=True, max_length=25)),
                ('job_type_name', models.CharField(db_index=True, max_length=100)),
                ('job_type_symbol', models.CharField(blank=True, db_index=True, max_length=25)),
                (
                    'option_collection_hash',
                    models.CharField(blank=True, db_index=True, max_length=64),
                ),
                ('build_system_type', models.CharField(blank=True, db_index=True, max_length=25)),
                ('repository', models.CharField(db_index=True, max_length=50)),
                ('first_submission_timestamp', models.IntegerField(db_index=True)),
            ],
            options={
                'db_table': 'reference_data_signatures',
                'verbose_name_plural': 'reference data signatures',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('guid', models.CharField(max_length=50, unique=True)),
                ('project_specific_id', models.PositiveIntegerField(null=True)),
                ('coalesced_to_guid', models.CharField(default=None, max_length=50, null=True)),
                ('option_collection_hash', models.CharField(max_length=64)),
                ('who', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=125)),
                ('result', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('submit_time', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('running_eta', models.PositiveIntegerField(default=None, null=True)),
                ('tier', models.PositiveIntegerField()),
                (
                    'build_platform',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='jobs',
                        to='model.BuildPlatform',
                    ),
                ),
                (
                    'failure_classification',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='jobs',
                        to='model.FailureClassification',
                    ),
                ),
                (
                    'job_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='jobs',
                        to='model.JobType',
                    ),
                ),
                (
                    'machine',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Machine'
                    ),
                ),
                (
                    'machine_platform',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.MachinePlatform'
                    ),
                ),
                (
                    'product',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Product'
                    ),
                ),
                (
                    'push',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='jobs',
                        to='model.Push',
                    ),
                ),
                (
                    'repository',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Repository'
                    ),
                ),
                (
                    'signature',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='model.ReferenceDataSignatures',
                    ),
                ),
                (
                    'autoclassify_status',
                    models.IntegerField(
                        choices=[
                            (0, 'pending'),
                            (1, 'crossreferenced'),
                            (2, 'autoclassified'),
                            (3, 'skipped'),
                            (255, 'failed'),
                        ],
                        default=0,
                    ),
                ),
                (
                    'job_group',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='jobs',
                        to='model.JobGroup',
                    ),
                ),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='BugJobMap',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bug_id', models.PositiveIntegerField(db_index=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                (
                    'job',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Job'),
                ),
                (
                    'user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'db_table': 'bug_job_map',
            },
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70, null=True)),
                ('value', models.CharField(max_length=125)),
                ('url', models.URLField(max_length=512, null=True)),
                (
                    'job',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='job_details',
                        to='model.Job',
                    ),
                ),
            ],
            options={
                'db_table': 'job_detail',
            },
        ),
        migrations.CreateModel(
            name='JobLog',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=255)),
                (
                    'status',
                    models.IntegerField(
                        choices=[(0, 'pending'), (1, 'parsed'), (2, 'failed')], default=0
                    ),
                ),
                (
                    'job',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='job_log',
                        to='model.Job',
                    ),
                ),
            ],
            options={
                'db_table': 'job_log',
            },
        ),
        migrations.CreateModel(
            name='JobNote',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                (
                    'failure_classification',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='model.FailureClassification',
                    ),
                ),
                (
                    'job',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Job'),
                ),
                (
                    'user',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'db_table': 'job_note',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'option',
            },
        ),
        migrations.CreateModel(
            name='OptionCollection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('option_collection_hash', models.CharField(max_length=40)),
                (
                    'option',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Option'
                    ),
                ),
            ],
            options={
                'db_table': 'option_collection',
            },
        ),
        migrations.CreateModel(
            name='RunnableJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('option_collection_hash', models.CharField(max_length=64)),
                ('ref_data_name', models.CharField(max_length=255)),
                ('build_system_type', models.CharField(max_length=25)),
                ('last_touched', models.DateTimeField(auto_now=True)),
                (
                    'build_platform',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.BuildPlatform'
                    ),
                ),
                (
                    'job_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.JobType'
                    ),
                ),
                (
                    'machine_platform',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.MachinePlatform'
                    ),
                ),
                (
                    'repository',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Repository'
                    ),
                ),
                (
                    'job_group',
                    models.ForeignKey(
                        default=2, on_delete=django.db.models.deletion.CASCADE, to='model.JobGroup'
                    ),
                ),
            ],
            options={
                'db_table': 'runnable_job',
            },
        ),
        migrations.CreateModel(
            name='FailureLine',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('job_guid', models.CharField(max_length=50)),
                (
                    'action',
                    models.CharField(
                        choices=[
                            ('test_result', 'test_result'),
                            ('log', 'log'),
                            ('crash', 'crash'),
                            ('truncated', 'truncated'),
                        ],
                        max_length=11,
                    ),
                ),
                ('line', models.PositiveIntegerField()),
                ('test', models.TextField(blank=True, null=True)),
                ('subtest', models.TextField(blank=True, null=True)),
                (
                    'status',
                    models.CharField(
                        choices=[
                            ('PASS', 'PASS'),
                            ('FAIL', 'FAIL'),
                            ('OK', 'OK'),
                            ('ERROR', 'ERROR'),
                            ('TIMEOUT', 'TIMEOUT'),
                            ('CRASH', 'CRASH'),
                            ('ASSERT', 'ASSERT'),
                            ('SKIP', 'SKIP'),
                            ('NOTRUN', 'NOTRUN'),
                        ],
                        max_length=7,
                    ),
                ),
                (
                    'expected',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('PASS', 'PASS'),
                            ('FAIL', 'FAIL'),
                            ('OK', 'OK'),
                            ('ERROR', 'ERROR'),
                            ('TIMEOUT', 'TIMEOUT'),
                            ('CRASH', 'CRASH'),
                            ('ASSERT', 'ASSERT'),
                            ('SKIP', 'SKIP'),
                            ('NOTRUN', 'NOTRUN'),
                        ],
                        max_length=7,
                        null=True,
                    ),
                ),
                ('message', models.TextField(blank=True, null=True)),
                ('signature', models.TextField(blank=True, null=True)),
                (
                    'level',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('PASS', 'PASS'),
                            ('FAIL', 'FAIL'),
                            ('OK', 'OK'),
                            ('ERROR', 'ERROR'),
                            ('TIMEOUT', 'TIMEOUT'),
                            ('CRASH', 'CRASH'),
                            ('ASSERT', 'ASSERT'),
                            ('SKIP', 'SKIP'),
                            ('NOTRUN', 'NOTRUN'),
                        ],
                        max_length=8,
                        null=True,
                    ),
                ),
                ('stack', models.TextField(blank=True, null=True)),
                ('stackwalk_stdout', models.TextField(blank=True, null=True)),
                ('stackwalk_stderr', models.TextField(blank=True, null=True)),
                ('best_is_verified', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                (
                    'best_classification',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='best_for_lines',
                        to='model.ClassifiedFailure',
                    ),
                ),
                (
                    'job_log',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='failure_line',
                        to='model.JobLog',
                    ),
                ),
                (
                    'repository',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Repository'
                    ),
                ),
            ],
            options={
                'db_table': 'failure_line',
            },
        ),
        migrations.CreateModel(
            name='Matcher',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'matcher',
            },
        ),
        migrations.CreateModel(
            name='FailureMatch',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                (
                    'score',
                    models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
                ),
                (
                    'classified_failure',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='matches',
                        to='model.ClassifiedFailure',
                    ),
                ),
                (
                    'failure_line',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='matches',
                        to='model.FailureLine',
                    ),
                ),
                (
                    'matcher',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Matcher'
                    ),
                ),
            ],
            options={
                'db_table': 'failure_match',
                'verbose_name_plural': 'failure matches',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                (
                    'failure_lines',
                    models.ManyToManyField(related_name='group', to='model.FailureLine'),
                ),
            ],
            options={
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='TextLogStep',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('started', models.DateTimeField(null=True)),
                ('finished', models.DateTimeField(null=True)),
                ('started_line_number', models.PositiveIntegerField()),
                ('finished_line_number', models.PositiveIntegerField()),
                (
                    'result',
                    models.IntegerField(
                        choices=[
                            (0, 'success'),
                            (1, 'testfailed'),
                            (2, 'busted'),
                            (3, 'skipped'),
                            (4, 'exception'),
                            (5, 'retry'),
                            (6, 'usercancel'),
                            (7, 'unknown'),
                            (8, 'superseded'),
                        ]
                    ),
                ),
                (
                    'job',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='text_log_step',
                        to='model.Job',
                    ),
                ),
            ],
            options={
                'db_table': 'text_log_step',
            },
        ),
        migrations.CreateModel(
            name='TextLogError',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('line', models.TextField()),
                ('line_number', models.PositiveIntegerField()),
                (
                    'step',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='errors',
                        to='model.TextLogStep',
                    ),
                ),
            ],
            options={
                'db_table': 'text_log_error',
            },
        ),
        migrations.CreateModel(
            name='TextLogErrorMatch',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                (
                    'score',
                    models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
                ),
                (
                    'classified_failure',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='error_matches',
                        to='model.ClassifiedFailure',
                    ),
                ),
                (
                    'matcher',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='model.Matcher'
                    ),
                ),
                (
                    'text_log_error',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='matches',
                        to='model.TextLogError',
                    ),
                ),
            ],
            options={
                'db_table': 'text_log_error_match',
                'verbose_name_plural': 'text log error matches',
            },
        ),
        migrations.CreateModel(
            name='TaskclusterMetadata',
            fields=[
                (
                    'job',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name='taskcluster_metadata',
                        serialize=False,
                        to='model.Job',
                    ),
                ),
                (
                    'task_id',
                    models.CharField(
                        max_length=22, validators=[django.core.validators.MinLengthValidator(22)]
                    ),
                ),
                ('retry_id', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'taskcluster_metadata',
            },
        ),
        migrations.CreateModel(
            name='TextLogErrorMetadata',
            fields=[
                (
                    'text_log_error',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name='_metadata',
                        serialize=False,
                        to='model.TextLogError',
                    ),
                ),
                ('best_is_verified', models.BooleanField(default=False)),
                (
                    'best_classification',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='best_for_errors',
                        to='model.ClassifiedFailure',
                    ),
                ),
                (
                    'failure_line',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='text_log_error_metadata',
                        to='model.FailureLine',
                    ),
                ),
            ],
            options={
                'db_table': 'text_log_error_metadata',
            },
        ),
        migrations.AddField(
            model_name='classifiedfailure',
            name='failure_lines',
            field=models.ManyToManyField(
                related_name='classified_failures',
                through='model.FailureMatch',
                to='model.FailureLine',
            ),
        ),
        migrations.AddField(
            model_name='classifiedfailure',
            name='text_log_errors',
            field=models.ManyToManyField(
                related_name='classified_failures',
                through='model.TextLogErrorMatch',
                to='model.TextLogError',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='referencedatasignatures',
            unique_together=set([('name', 'signature', 'build_system_type', 'repository')]),
        ),
        migrations.AlterUniqueTogether(
            name='machineplatform',
            unique_together=set([('os_name', 'platform', 'architecture')]),
        ),
        migrations.AlterUniqueTogether(
            name='jobtype',
            unique_together=set([('name', 'symbol')]),
        ),
        migrations.AlterUniqueTogether(
            name='jobgroup',
            unique_together=set([('name', 'symbol')]),
        ),
        migrations.AlterUniqueTogether(
            name='buildplatform',
            unique_together=set([('os_name', 'platform', 'architecture')]),
        ),
        migrations.AlterUniqueTogether(
            name='textlogstep',
            unique_together=set([('job', 'started_line_number', 'finished_line_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='textlogerrormatch',
            unique_together=set([('text_log_error', 'classified_failure', 'matcher')]),
        ),
        migrations.AlterUniqueTogether(
            name='textlogerror',
            unique_together=set([('step', 'line_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='runnablejob',
            unique_together=set([('ref_data_name', 'build_system_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='push',
            unique_together=set([('repository', 'revision')]),
        ),
        migrations.AlterUniqueTogether(
            name='optioncollection',
            unique_together=set([('option_collection_hash', 'option')]),
        ),
        migrations.AlterUniqueTogether(
            name='joblog',
            unique_together=set([('job', 'name', 'url')]),
        ),
        migrations.AlterUniqueTogether(
            name='jobdetail',
            unique_together=set([('title', 'value', 'job')]),
        ),
        migrations.AlterIndexTogether(
            name='job',
            index_together=set(
                [
                    ('repository', 'option_collection_hash', 'job_type', 'start_time'),
                    ('repository', 'build_platform', 'job_type', 'start_time'),
                    ('repository', 'submit_time'),
                    ('machine_platform', 'option_collection_hash', 'push'),
                    (
                        'repository',
                        'build_platform',
                        'option_collection_hash',
                        'job_type',
                        'start_time',
                    ),
                    ('repository', 'job_type', 'start_time'),
                ]
            ),
        ),
        migrations.AlterUniqueTogether(
            name='failurematch',
            unique_together=set([('failure_line', 'classified_failure', 'matcher')]),
        ),
        migrations.AlterUniqueTogether(
            name='failureline',
            unique_together=set([('job_log', 'line')]),
        ),
        migrations.AlterIndexTogether(
            name='failureline',
            index_together=set([('job_guid', 'repository')]),
        ),
        migrations.AlterUniqueTogether(
            name='commit',
            unique_together=set([('push', 'revision')]),
        ),
        migrations.AlterUniqueTogether(
            name='bugjobmap',
            unique_together=set([('job', 'bug_id')]),
        ),
        # Manually created migrations.
        # Since Django doesn't natively support creating FULLTEXT indices.
        migrations.RunSQL(
            [
                # Suppress the MySQL warning "InnoDB rebuilding table to add column FTS_DOC_ID":
                # https://dev.mysql.com/doc/refman/5.7/en/innodb-fulltext-index.html#innodb-fulltext-index-docid
                # The table is empty when the index is added, so we don't care about it being rebuilt,
                # and there isn't a better way to add the index without Django FULLTEXT support.
                'SET @old_max_error_count=@@max_error_count, max_error_count=0;',
                'CREATE FULLTEXT INDEX idx_summary ON bugscache (summary);',
                'SET max_error_count=@old_max_error_count;',
            ],
            reverse_sql=['ALTER TABLE bugscache DROP INDEX idx_summary;'],
        ),
        # Since Django doesn't natively support creating composite prefix indicies.
        migrations.RunSQL(
            [
                'CREATE INDEX failure_line_test_idx ON failure_line (test(50), subtest(25), status, expected, created);',
                'CREATE INDEX failure_line_signature_test_idx ON failure_line (signature(25), test(50), created);',
            ],
            reverse_sql=[
                'DROP INDEX failure_line_test_idx ON failure_line;',
                'DROP INDEX failure_line_signature_test_idx ON failure_line;',
            ],
            state_operations=[
                migrations.AlterIndexTogether(
                    name='failureline',
                    index_together=set(
                        [
                            ('test', 'subtest', 'status', 'expected', 'created'),
                            ('job_guid', 'repository'),
                            ('signature', 'test', 'created'),
                        ]
                    ),
                ),
            ],
        ),
    ]
