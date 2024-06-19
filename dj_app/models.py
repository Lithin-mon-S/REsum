from django.db import models


# Create your models here.


class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self):
        return self.job_title


class Education(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()

    def __str__(self):
        return self.degree


class Project(models.Model):
    personal_detail = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='assets')

    def __str__(self):
        return self.title
