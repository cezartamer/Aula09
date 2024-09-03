from loguru import logger
from decorator import calcular_tempo
#Para log também posso usar o Sentry/ Sentury sdk - manda as mensagens de erro para um servidor

logger.add("meu_app.log", level="CRITICAL")

@calcular_tempo
def soma(x,y):
    try:
        logger.info(f"Soma correta!{x + y}")
        return x + y
    except:
        logger.critical("Problema no tipo de dado")
        
 

soma(2,33)
soma(2,3)
 

