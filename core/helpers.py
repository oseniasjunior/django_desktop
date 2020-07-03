from datetime import date


def transform_date(input_date: str):
    date_bith = map(lambda item: int(item), input_date.split('-'))
    return date(
        year=next(date_bith),
        month=next(date_bith),
        day=next(date_bith)
    )
