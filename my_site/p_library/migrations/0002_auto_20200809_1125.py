# Generated by Django 2.2.6 on 2020-08-09 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя друга')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(verbose_name='Год рожения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=2, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=256, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Author'),
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book', verbose_name='Книга')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Friend', verbose_name='Друг')),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='books',
            field=models.ManyToManyField(through='p_library.Reading', to='p_library.Book', verbose_name='Читает'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p_library.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(through='p_library.Reading', to='p_library.Friend', verbose_name='Читатели'),
        ),
    ]
