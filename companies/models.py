from django.db import models


class District(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CompanyNet(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    districts = models.ManyToManyField(District, related_name='companies')
    company_net = models.ForeignKey(CompanyNet, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Good(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ManyToManyField(Company, related_name='goods')

    def __str__(self):
        return self.title


