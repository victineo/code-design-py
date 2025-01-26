from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calc_result = self.__proccess_data(input_data)

        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('body mal formatado!')
        
        input_data = body['numbers']
        return input_data
    
    def __proccess_data(self, input_data: List[float]) -> float:
        first_proccess_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standart_deviation(first_proccess_result)
        return 1/result
    
    def __format_response(self, calc_result: float) -> Dict:
        return { 'data': {
            'Calculator': 2,
            'result': round(calc_result, 2)
        } }