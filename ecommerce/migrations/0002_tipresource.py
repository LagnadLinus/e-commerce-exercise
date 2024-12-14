# Generated by Django 5.1.3 on 2024-11-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(help_text='Main content about the tip or resource.')),
                ('health_benefits', models.TextField(blank=True, help_text='Health benefits or additional information.', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tips_resources/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tip/Resource',
                'verbose_name_plural': 'Tips/Resources',
                'ordering': ['-created_at'],
            },
        ),
    ]