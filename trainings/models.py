from django.db import models

# Create your models here.
sections = (
    ("fitness", "Фитнес"),
    ("crossfit", "Кросфит"),
    ("yoga", "Йога"),
    ("shaping", "Шейпинг"),
    ("stretching", "Стретчинг"),
    ("acrobatics", "Акробатика"),
)


class Training(models.Model):

    name = models.CharField(max_length=20, choices=sections)
    time = models.DateTimeField()

    def __str__(self):

        return "{0} [{1}.{2}]".format(self.name, self.time.day, self.time.month)
