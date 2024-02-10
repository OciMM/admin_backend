from django.db import models

class SiteSettings(models.Model):
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.05)
    referral_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    advertising_cost = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

    def __str__(self):
        return "Site Settings"