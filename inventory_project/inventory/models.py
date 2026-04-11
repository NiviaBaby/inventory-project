from django.db import models


class InventoryItem(models.Model):
    sku = models.CharField(max_length=255, unique=True, help_text="Stock Keeping Unit")
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Inventory Item'
        verbose_name_plural = 'Inventory Items'

    def __str__(self):
        return f"{self.sku} - {self.name}"
