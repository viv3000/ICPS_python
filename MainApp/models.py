from django.db import models
from django.contrib.auth.models import User

from django.db.models.base import ValidationError

import datetime


class SchoolClass(models.Model):

    title = models.CharField(max_length=255, verbose_name='Буква класса')
    year  = models.IntegerField(verbose_name='Год набора')

    def _getClassNumber(self, year):
        date = datetime.datetime.now()
        thisYear = date.year
        thisMonth = date.month
        september = 9
        return thisYear - int(year.__str__()) + (1 if thisMonth >= september else 0)

    def __str__(self):
        classNumber = self._getClassNumber( int(str(self.year)) )
        classNumber = (
                (classNumber 
                    if classNumber <= 11 else f"(Класс выпустился в {datetime.datetime.now().year - classNumber + 11})" ) 
                        if classNumber >= 0 else f"(Класс приступит к обучению в {self.year}!)")
        classLetter = "" if self.title==None else self.title
        return f"{classNumber}{classLetter}"

class Subject(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=0)
    fullName    = models.CharField(max_length=255, verbose_name='ФИО', null=True, blank=True)
    phoneNumber = models.CharField(max_length=15, verbose_name='Телефонный номер', null=True, blank=True)
    classes = models.ManyToManyField(SchoolClass, verbose_name='Классы', blank=True)
    subject = models.ManyToManyField(Subject, verbose_name='Предметы', blank=True)

    def __str__(self):
        return self.fullName

class Attestation(models.Model):
    teacher     = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Учитель', default=0)
    subject     = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет', default=0)
    schoolClass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='Класс', default=0)
    theme = models.CharField(max_length=255, verbose_name='Тема', null=True, blank=True)
    type  = models.CharField(max_length=255, verbose_name='Тип', null=True, blank=True)
    date  = models.DateTimeField(verbose_name='Дата проведения', null=True, blank=True)
    minimumPercentageFor5 = models.IntegerField(verbose_name='% для 5', null=True, blank=True)
    minimumPercentageFor4 = models.IntegerField(verbose_name='% для 4', null=True, blank=True)
    minimumPercentageFor3 = models.IntegerField(verbose_name='% для 3', null=True, blank=True)

    def __str__(self):
        return f"{self.schoolClass}: {self.theme} {self.date}"

class Task(models.Model):
    attestation     = models.ForeignKey(Attestation, on_delete=models.CASCADE, verbose_name='Работа', default=0)
    title = models.CharField(max_length=255, verbose_name='Текст', null=True, blank=True)
    skill = models.CharField(max_length=255, verbose_name='Проверяемый навык', null=True, blank=True)
    maxPoint = models.IntegerField(verbose_name='Максимальный балл', null=True, blank=True)

    def __str__(self):
        return self.title

class TaskResult(models.Model):
    task    = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание', default=0)
    point   = models.IntegerField(verbose_name='Баллы', null=True, blank=True)

    def __str__(self):
        return f"{self.task}: {self.point}"

class Student(models.Model):
    schoolClass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='Класс', default=0)
    fullName    = models.CharField(max_length=255, verbose_name='ФИО', null=True, blank=True)
    results     = models.ManyToManyField(TaskResult, blank=True, verbose_name='Результаты заданий')

    def __str__(self):
        return self.fullName
