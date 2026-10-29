rom app import calculate_total

def test_calculate_total_with_discount():
    assert calculate_total(10.0, 2, 10) == 18.0
    assert calculate_total(100.0, 1, 20) == 80.0