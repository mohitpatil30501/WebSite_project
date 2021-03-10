# Generated by Django 3.1.6 on 2021-02-27 04:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_auto_20210227_0947'),
        ('Dashboard', '0002_auto_20210225_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b3cb8016-d745-4e42-97df-3d1972db4c5e'), unique=True),
        ),
        migrations.AlterField(
            model_name='administrativeexperience',
            name='id',
            field=models.UUIDField(default=uuid.UUID('10bfbf7e-03d8-43f4-b432-0152b5064fa6'), unique=True),
        ),
        migrations.AlterField(
            model_name='designation',
            name='id',
            field=models.UUIDField(default=uuid.UUID('60d32c31-37ac-433e-b7a1-d2a7b050ffa7'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='id',
            field=models.UUIDField(default=uuid.UUID('8dc302b3-386e-4baa-a3ac-6b426f7a38ee'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='facultydevelopment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('17752b31-f56f-43f1-8432-138e498e9717'), unique=True),
        ),
        migrations.AlterField(
            model_name='industrialexperience',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a221e8de-8e83-4405-8c75-d9e887ea00e9'), unique=True),
        ),
        migrations.AlterField(
            model_name='professionalmembership',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0106160a-08e5-4b22-8d3b-0574ab43a673'), unique=True),
        ),
        migrations.AlterField(
            model_name='subjectofinterest',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4e648fc4-59dd-4b59-9d7b-7f21e287fffc'), unique=True),
        ),
        migrations.AlterField(
            model_name='teachingexperience',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ffc7adcd-d03f-4354-ba96-02d1547e98eb'), unique=True),
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('06467c35-6903-4cf1-a3b4-250b2ae79451'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('date_form', models.CharField(max_length=10)),
                ('date_to', models.CharField(max_length=10)),
                ('day', models.IntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ShortTermsTrainingProgram',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('bec1a38c-f3ea-4b51-9f24-763309a2ad87'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('date_form', models.CharField(max_length=10)),
                ('date_to', models.CharField(max_length=10)),
                ('day', models.IntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationsPaper',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('81088012-31cf-4b84-979f-23ae94d2e1a7'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('url', models.CharField(max_length=300)),
                ('level', models.CharField(max_length=15)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationsJournal',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('f9b6408d-c229-468b-9576-2c88afe6a136'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=100)),
                ('page', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=5)),
                ('url', models.CharField(max_length=300)),
                ('level', models.CharField(max_length=15)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationsBook',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e020757a-397a-4a8b-8530-b15775935046'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGuided',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('38b88987-55ef-4d4b-9e53-557aa1e90f37'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('level', models.CharField(max_length=3)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='OtherInstituteInteractions',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('af1924a1-6dcd-4e12-8985-f0a184b80dac'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('invitee', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCurricularActivities',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('28791ab7-7660-4da9-a673-94caffba97b2'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=5)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Consultancy',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('010cf0b2-8964-49e9-a81b-d9c0dd5b2ecd'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('work_done', models.CharField(max_length=300)),
                ('cost', models.CharField(max_length=20)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='AwardReceived',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('f83d1b79-43b5-41ee-97ad-6e38c2c53a67'), unique=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('organization', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.teacher')),
            ],
        ),
    ]
