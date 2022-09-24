from django.db import models
from . import (
    KARTRIC_NOVU_CHOICES
)
# Create your models here.
class Mehsullar(models.Model):
    mehsulun_adi = models.CharField(max_length=300)
    qiymet = models.FloatField()
    shirket = models.ForeignKey('company.Shirket', on_delete=models.CASCADE, null=True, related_name="shirket_mehsul")
    is_hediyye = models.BooleanField(default=False)

    kartric_novu =  models.CharField(
        max_length=50,
        choices=KARTRIC_NOVU_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ("pk",)
        default_permissions = []
        permissions = (
            ("view_mehsullar", "Mövcud məhsullara baxa bilər"),
            ("add_mehsullar", "Məhsul əlavə edə bilər"),
            ("change_mehsullar", "Məhsul məlumatlarını yeniləyə bilər"),
            ("delete_mehsullar", "Məhsul silə bilər")
        )

    # def __str__(self) -> str:
    #     return f"{self.shirket} şirkəti {self.mehsulun_adi} - {self.qiymet} AZN"
