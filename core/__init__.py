import datetime


class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f'São {now.hour} horas e {now.minute} minutos'
        return answer

    @staticmethod
    def get_date():
        hoje = datetime.date.today()
        answer = f'Hoje é {hoje.day} do {hoje.month} de {hoje.year}'
        return answer
