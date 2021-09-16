from django.db import models

# Create your models here.


class OperatingSystem(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class InstallationMethod(models.Model):
    operating_system = models.ForeignKey(
        OperatingSystem, on_delete=models.CASCADE)
    package_manager = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return "%s-%s" % (self.operating_system, self.package_manager)


class Software(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    website = models.URLField()
    linux = models.BooleanField(default=False)
    mac_OS = models.BooleanField(default=False)
    windows = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class InstallationInfo(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    method = models.ForeignKey(InstallationMethod, on_delete=models.DO_NOTHING)
    package_name = models.CharField(max_length=255, blank=True, null=True)
    download_url = models.URLField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s-%s" % (self.software.name, self.method.operating_system.name)
