import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 15 == calculator.multiplication(5,3)
    def  test_division(self):
        assert 2 == calculator.division(10,5)