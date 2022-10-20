

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('taggit', '0005_auto_20220424_2025'),

        ('contents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='like_authors',
            field=models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='contents.TaggedFeed', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.feed'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
