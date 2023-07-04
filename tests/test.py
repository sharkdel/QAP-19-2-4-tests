from app.calc import Calculator


class TestCalc:
    
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 5, 7) == 12

    def test_subtraction(self):
        assert self.calc.subtraction(self, 17, 9) == 8

    def test_multiply(self):
        assert self.calc.multiply(self, 12, 5) == 60

    def test_division(self):
        assert self.calc.division(self, 45, 9) == 5

    def teardown(self):
        print('Выполнение метода Teardown')
