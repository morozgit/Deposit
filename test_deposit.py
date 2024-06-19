from datetime import datetime

from main import Deposit, add_months, calc_deposit_

EPS = 0.0001


def test_add_month():
    date = datetime.strptime('31.12.2020', '%d.%m.%Y')
    current_date = add_months(date, 1)
    assert '31.01.2021' == current_date.strftime('%d.%m.%Y')
    current_date = add_months(date, 2)
    assert '28.02.2021' == current_date.strftime('%d.%m.%Y')
    

def test_calc_deposit_():
    deposit = Deposit(date='31.01.2021', period=3, amount=10000, rate=6)
    res = calc_deposit_(deposit)
    assert 3 == len(res)
    assert abs(res['31.01.2021'] - 10050) < EPS
    assert abs(res['28.02.2021'] - 10100.25) < EPS
    assert abs(res['31.03.2021'] - 10150.75) < EPS
    