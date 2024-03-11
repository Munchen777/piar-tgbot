from loguru import logger


my_logger = logger
my_logger.add('weather_tgbot.log', format='{time} {level} {message}', level='INFO',
              rotation='30 MB')
