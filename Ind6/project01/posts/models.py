from django.db import models


# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120, verbose_name='Name')
    second_name = models.CharField(max_length=120, verbose_name='Last Name')
    pseudonym = models.CharField(max_length=120, verbose_name='Pseudonym')
    date_birth = models.DateField()

    author_obj = models.Manager()

    def __unicode__(self):
        return f"{self.pseudonym}"

    def __str__(self):
        return f"{self.pseudonym}"


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name='Name')
    address = models.CharField(max_length=120, verbose_name='Address')

    gallery_obj = models.Manager()

    def __str__(self):
        return f"{self.name}"


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name='Name')
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=60, verbose_name='Genre')
    id_gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    timestamp = models.DateField()

    picture_obj = models.Manager()

    def __unicode__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"
