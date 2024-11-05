class Decs:
    @staticmethod
    def statuscode(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            # Получаем статус-код из результата, если он является объектом Response
            print(f'\nЭто отработал декоартор!\nСтатус-код: {result.status_code}')
            return result
        return wrapper