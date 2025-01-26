from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standart_deviation(self, numbers: List[float]) -> float:
        return 3

# Teste de integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest(body={ 'numbers': [2.12, 4.62, 1.32] })

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    formated_response = calculator_2.calculate(mock_request)

    # Formatação da resposta
    assert isinstance(formated_response, dict)
    assert formated_response == { 'data': { 'Calculator': 2, 'result': 0.08 } }

# Teste unitário de Calculator2
def test_calculate():
    mock_request = MockRequest(body={ 'numbers': [2.12, 4.62, 1.32] })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)

    formated_response = calculator_2.calculate(mock_request)

    # Formatação da resposta
    assert isinstance(formated_response, dict)
    assert formated_response == { 'data': { 'Calculator': 2, 'result': 0.33 } }