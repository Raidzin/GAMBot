import datetime as dt

from PIL import ImageDraw

DATE_FORMAT = '%a %d-%m-%Y\n%H:%M %S'
"""
пример:
Fri 01-04-2022
17:25 24
"""


def process_frame(frame, filters):
    for image_filter in filters:
        frame = image_filter(frame)
    return frame


"""
Дальше идут различные фильтры
фильтр на вход должен принимать кадр типа PIL Image и возвращать обработанный
"""


def add_datetime(frame):
    draw_text = ImageDraw.Draw(frame)
    draw_text.text(
        (10, 10),
        f'{dt.datetime.now().strftime(DATE_FORMAT)}',
        fill='#F8F8FF',  # призрачно белый
    )
    return frame
