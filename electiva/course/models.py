from django.db import models

# Create your models here.
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image_course = models.ImageField(verbose_name="Imagen del curso", upload_to="courses")
    image_author = models.ImageField(verbose_name="Imagen del autor", upload_to="courses")
    name_author = models.CharField(max_length=100, verbose_name="Nombre del autor")
    price = models.FloatField(verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["created"]

    def __str__(self):
        return self.title
