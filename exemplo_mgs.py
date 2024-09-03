from loguru import logger

logger.add("meu_msg.log")

logger.debug("Um aviso para o desenvolverdor")
logger.info("Informação importante do proceso")
logger.warning("Um aviso que algo vai parar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma que aborta a aplicação")
