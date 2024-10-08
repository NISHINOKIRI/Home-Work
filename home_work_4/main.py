import datetime
from os import remove

from lib.client.client import App

app = App(
    username='Nishinokiri',
    age=227,
)

app.create_task(
    name='test_1',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

app.create_task(
    name='test_2',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

app.create_task(
    name='test_3',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

app.create_task(
    name='test_4',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

app.create_task(
    name='test_5',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)


app.create_task(
    name='test_6',
    priority='medium',
    deadline=datetime.datetime(
        year=2024,
        month=10,
        day=1,
        hour=19,
        minute=0,
    )
)

print(app.remove_task(6))
print(app.get_profile())




