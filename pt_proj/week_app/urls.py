from django.urls import path

from week_app.views import WeekCounterView


urlpatterns = [
    path('', WeekCounterView.as_view(), name='main'),
]
