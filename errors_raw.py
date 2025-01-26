# 400 -> Bad Request
# 422 -> Unprocessable Entity

class HttpUnprocessableEntity(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('Estou no bloco try')
    raise HttpUnprocessableEntity('Estou lançando uma exceção')
except Exception as e:
    print(f'Estou no tratamento de erro')
    print(f'{e.name}\n{e.status_code}\n{e.message}')