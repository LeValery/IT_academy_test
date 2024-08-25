# -*- coding: utf-8 -*-

from datetime import date


def day_diff(ISO_date_1:str, ISO_date_2:str):
    try: 
        date1 = date.fromisoformat(ISO_date_1)
        date2 = date.fromisoformat(ISO_date_2)
        print(f'Разница между датами в днях: {abs(date2 - date1).days}')
    except:
        print('Тредуются даты в формате ISO')

"""
day_diff('2024-03-01', '20230301')
day_diff('2024-02-01', '2023-02-01')
"""
