from django.db import models


class Inventario(models.Model):
    nombe = models.CharField(max_length=100, null=False, blank=False)
    costo_por_item = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    cantidad_en_stock = models.IntegerField(null=False, blank=False)
    cantidad_vendida = models.IntegerField(null=False, blank=False)
    ventas = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock_fecha = models.DateField(auto_now_add=True)
    ultima_venta_fecha = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name