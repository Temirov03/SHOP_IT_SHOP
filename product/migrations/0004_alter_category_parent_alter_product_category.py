# Generated by Django 4.2.1 on 2023-05-12 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_remove_product_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="child_product",
                to="product.category",
                verbose_name="Kategoriyasi",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_related",
                to="product.category",
                verbose_name="Kategoriyasi",
            ),
        ),
    ]
