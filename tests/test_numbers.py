import pytest
from sum_package import sum_functions


class TestClass:
    def test_sum(self):
        expected_result = 2
        function_result = sum_functions.sum_two_numbers(num1=1, num2=1)
        assert expected_result == function_result

    def test_sum_all(self):
        expected_result = 3
        function_result = sum_functions.sum_any_numbers(1, 1, 1)
        assert expected_result == function_result
