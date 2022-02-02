from datetime import date

from django import forms
from django.utils.translation import gettext_lazy as _


class WeekForms(forms.Form):
    """
    Форма ввода поля даты.
    Специалтно добавил минимальную дату от 2018 года, что бы продемонстрировать работу
    вывода ошибки что можем использовать начало дати с 2019 года.
    """
    date = forms.DateField(label=_('Date'), widget=forms.DateInput(
        attrs={'min': '2018-01-01', 'type': 'date', 'class': 'form-input'}))

    def clean_date(self):
        get_date = self.cleaned_data.get('date')
        if (get_date - date(year=2019, month=1, day=1)).days < 0:
            raise forms.ValidationError(_("The date can't be earlier 01.01.2019"))
        return get_date
