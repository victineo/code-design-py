from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splitted_number = input_data / 3

        first_proccess_result = self.__first_proccess(splitted_number)
        second_proccess_result = self.__second_proccess(splitted_number)
        calc_result = first_proccess_result + second_proccess_result + splitted_number

        response = self.__format_response(calc_result)

        return response
    
    def __validate_body(self, body: Dict) -> float:
        if 'number' not in body:
            raise HttpUnprocessableEntityError('body mal formatado!')
        
        input_data = body['number']
        return input_data
    
    def __first_proccess(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_proccess(self, second_number: float) -> float:
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part

    def __format_response(self, calc_result: float) -> Dict:
        return { 'data': {
            'Calculator': 1,
            'result': round(calc_result, 2)
        } }