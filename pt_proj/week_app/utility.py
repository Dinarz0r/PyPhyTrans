from datetime import date


def week_counter(date_c: date) -> int:
    """
    Функцция которая принимает дату и высчитывает кол-во неделей
    в соответствии с тз первым днём недели считаем воскресенье;
    точка отсчета: 1 января 2019г, вт (т.е. считаем Неделей #1 все дни до 5го января
    2019г включительно. 6 января 2019г - первый день Недели #2.)
    :param date_c:
    :return int:
    """
    start_2019 = date(year=2019, month=1, day=1)
    week_number = ((date_c - start_2019).days + 9) // 7
    return week_number
