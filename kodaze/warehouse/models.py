import django
from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import User
from core.image_validator import file_size
from django.contrib.auth import get_user_model

User = get_user_model()

class Anbar(models.Model):
    ad = models.CharField(max_length=100)
    ofis = models.ForeignKey('company.Ofis', on_delete=models.CASCADE, null=True, related_name="ofis_anbar")
    shirket = models.ForeignKey('company.Shirket', on_delete=models.CASCADE, null=True, related_name="shirket_anbar")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.ad} - {self.ofis}"


class AnbarQeydler(models.Model):
    gonderen_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="anbar_sorgu")
    mehsul_ve_sayi = models.CharField(max_length=250, null=True, blank=True)
    qeyd = models.TextField()
    anbar = models.ForeignKey(Anbar, on_delete=models.CASCADE, related_name="anbar_qeyd")
    yerine_yetirildi = models.BooleanField(default=False)
    gonderilme_tarixi = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-pk",)

    def __str__(self) -> str:
        return f"{self.anbar} - {self.qeyd[:30]}"

class Stok(models.Model):
    anbar = models.ForeignKey(Anbar, null=True, on_delete=models.CASCADE)
    mehsul = models.ForeignKey("product.Mehsullar", null=True, on_delete=models.CASCADE)
    say = models.IntegerField(default=0)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"stok -> {self.anbar} - {self.mehsul} - {self.say}"

class Emeliyyat(models.Model):
    # mehsulun_sayi = models.IntegerField(default=0)
    # gonderilen_mehsul = models.ManyToManyField(Mehsullar, related_name="gonderilen_mehsul")

    gonderen = models.ForeignKey(Anbar, on_delete=models.CASCADE, null=True, related_name="gonderen")
    qebul_eden = models.ForeignKey(Anbar, on_delete=models.CASCADE, null=True, related_name="qebul_eden")

    mehsul_ve_sayi = models.CharField(max_length=500, null=True, blank=True)

    qeyd = models.TextField(default="", null=True, blank=True)
    emeliyyat_tarixi = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"Əməliyyat ==> {self.gonderen} - {self.qebul_eden} {self.emeliyyat_tarixi}"
