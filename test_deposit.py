from datetime import datetime
from main import Deposit, add_months, calc_deposit_

EPS = 0.01


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

def test_calc_deposit_min_period():
    deposit = Deposit(date='31.01.2021', period=1, amount=10000, rate=6)
    res = calc_deposit_(deposit)
    assert len(res) == 1
    assert abs(res['31.01.2021'] - 10050) < EPS 

def test_calc_deposit_max_period():
    deposit = Deposit(date='31.01.2021', period=60, amount=10000, rate=6)
    res = calc_deposit_(deposit)
    assert len(res) == 60
    assert abs(res['31.01.2021'] - 10050) < EPS 
    expected_amount = 10000 * (1 + 0.06 / 12) ** 60
    assert abs(res['31.12.2025'] - expected_amount) < EPS

def test_calc_deposit_min_amount():
    deposit = Deposit(date='31.01.2021', period=3, amount=10000, rate=6)
    res = calc_deposit_(deposit)
    assert len(res) == 3
    assert abs(res['31.01.2021'] - 10050) < EPS
    assert abs(res['28.02.2021'] - 10100.25) < EPS
    assert abs(res['31.03.2021'] - 10150.75) < EPS

def test_calc_deposit_max_amount():
    deposit = Deposit(date='31.01.2021', period=3, amount=3000000, rate=6)
    res = calc_deposit_(deposit)
    assert len(res) == 3
    assert abs(res['31.01.2021'] - 3015000) < EPS
    assert abs(res['28.02.2021'] - 3030075) < EPS
    assert abs(res['31.03.2021'] - 3045225.37) < EPS

def test_calc_deposit_min_rate():
    deposit = Deposit(date='31.01.2021', period=3, amount=10000, rate=1)
    res = calc_deposit_(deposit)
    assert len(res) == 3
    assert abs(res['31.01.2021'] - 10008.33) < EPS
    assert abs(res['28.02.2021'] - 10016.67) < EPS
    assert abs(res['31.03.2021'] - 10025.02) < EPS

def test_calc_deposit_max_rate():
    deposit = Deposit(date='31.01.2021', period=3, amount=10000, rate=8)
    res = calc_deposit_(deposit)
    assert len(res) == 3
    assert abs(res['31.01.2021'] - 10066.67) < EPS
    assert abs(res['28.02.2021'] - 10133.78) < EPS
    assert abs(res['31.03.2021'] - 10201.34) < EPS