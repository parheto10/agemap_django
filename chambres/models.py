from django.db import models

class Locale(models.Model):
    ville = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    libelle = models.CharField(max_length=255)
    type_equipement = models.CharField(max_length=255)
    profondeur_cable = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    latitude = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.CharField(max_length=12, null=True, blank=True)
    concessionnaire = models.CharField(max_length=255)
    chbre_proche = models.ForeignKey("locale", on_delete=models.CASCADE, blank=True, null=True, related_name="locale_proches")
    dtce_chambre_proche = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return ('%s') %(self.libelle)

    class Meta:
        verbose_name_plural = "CHAMBRES TECHNIQUES"
        verbose_name = "chambre techniques"
        ordering = ["libelle"]

    def save(self, force_insert=False, force_update=False):
        self.ville = self.ville.upper()
        self.commune = self.commune.upper()
        self.libelle = self.libelle.upper()
        self.concessionnaire = self.concessionnaire.upper()
        self.type_equipement = self.type_equipement.upper()
        super(Locale, self).save(force_insert, force_update)

# Create your models here.
