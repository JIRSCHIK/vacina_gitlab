# Generated by Django 3.0.14 on 2023-02-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0003_auto_20230213_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbParametrizacao',
            fields=[
                ('id_parametro', models.AutoField(primary_key=True, serialize=False)),
                ('zoom_mapa_inicial', models.DecimalField(decimal_places=1, default=9.5, max_digits=2)),
                ('zoom_mapa_localizacao', models.DecimalField(decimal_places=1, default=13.5, max_digits=2)),
                ('quantidade_ubs_inicial', models.IntegerField(default=50)),
                ('quantidade_ubs_localizacao', models.IntegerField(default=10)),
            ],
            options={
                'db_table': 'tb_parametrizacao',
                'managed': False,
            },
        ),
    ]
