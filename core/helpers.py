from datetime import date


# método que transforma uma string para uma data
def transform_date(input_date: str):
    # 1 - split data string '1987-10-28' isso vira um array de string ['1987', '10', '28']
    # 2 - map para tranformar o array de string para inteiro [1987, 10, 28]
    date_bith = map(lambda item: int(item), input_date.split('-'))
    # cria uma data a partir de cada possição array
    # index 0 = ano
    # index 1 = mês
    # index 2 = dia
    return date(
        year=next(date_bith),
        month=next(date_bith),
        day=next(date_bith)
    )
