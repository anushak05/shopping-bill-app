from app import calculate_total

def test_calculate_total():
    assert calculate_total(10.0, 2) == 20.0
    assert calculate_total(5.5, 4) == 22.0