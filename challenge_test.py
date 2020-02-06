from objects import Stocks

def test_case_1():
    assert Stocks.calc_max_interest([7,1,5,3,6,4]) == 5

def test_case_2():
    assert Stocks.calc_max_interest([7,6,4,3,1]) == 0

def test_case_3():
    assert Stocks.calc_max_interest([8,6,9,5,4,2,7]) == 5

def test_case_4():
    assert Stocks.calc_max_interest([10,1,16,5,8,31,20]) == 30

def test_case_5():
    assert Stocks.calc_max_interest([15,23,58,65,48]) == 50
    
