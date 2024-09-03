import time

def calcular_tempo(func):
    def wrapper(*args, **kwargs):
        temp_ini = time.time()
        func(*args)
        temp_fim = time.time()
        print(f"O tempo total foi de {temp_fim - temp_ini}")
    return wrapper 