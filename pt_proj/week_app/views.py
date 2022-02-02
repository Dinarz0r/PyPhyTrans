from datetime import date

from django.shortcuts import render
from django.views.generic import FormView

from week_app.forms import WeekForms


def week_counter(date_c: date) -> int:
    start_2019 = date(year=2019, month=1, day=1)
    week_number = ((date_c - start_2019).days + 9) // 7
    return week_number


class WeekCounterView(FormView):
    """
    Класс представления главной страницы который считает количество неделей
    начиная с 01-01-2019 вторник (по условию каждое ВС считается началом новой недели).
    """
    template_name = 'main/index.html'
    form_class = WeekForms

    def form_valid(self, form):
        date_1 = form.cleaned_data.get('date')
        context = super(WeekCounterView, self).get_context_data()
        context['date'] = week_counter(date_1)
        context['sel_date'] = date_1.strftime(format='%d.%m.%Y')
        return render(self.request, 'main/index.html', context)

    def form_invalid(self, form):
        context = super(WeekCounterView, self).get_context_data()
        return render(self.request, 'main/index.html', context=context, status=324)
