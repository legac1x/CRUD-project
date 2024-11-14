from django.forms import ModelForm, CharField
from .models import Schedule

class ScheduleForm(ModelForm):
    name = CharField(label='Введите название предмета')
    time = CharField(label='Введите время пары через тире')
    teacher = CharField(label='Введите имя и отчество преподавателя')

    class Meta:
        model = Schedule
        fields = ['name', 'time', 'teacher']