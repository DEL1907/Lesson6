from django.db import models


class Disease(models.Model):

    TYPE_CHOICES = (
        ('viral', 'Вирусные'),
        ('bacterial', 'Бактериальные'),
        ('parasitic', 'Паразитарные'),
        ('fungal', 'Грибковые')
    )

    name = models.CharField('Название', max_length=100)
    type = models.CharField('Вид', max_length=100, choices=TYPE_CHOICES, default='Вирусные')
    information = models.TextField('Информация', blank=True)
    infected = models.PositiveIntegerField('Инфицированные', default=0)
    is_cure = models.BooleanField('Неизлечимая болезнь', default=False)

    class Meta:
        verbose_name = 'Болезнь'
        verbose_name_plural = 'Болезни'

    def __str__(self) -> str:
        return self.name


class Patient(models.Model):
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=40, blank=True)
    patronymic = models.CharField('Отчество', max_length=30, blank=True)

    date_of_birth = models.DateField('Дата рождения', default='')
    insurance_policy = models.ImageField('Копия страхового полиса', upload_to='doc', null=True, blank=True)
    cost_treatment = models.DecimalField('Стоимость лечения', max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
