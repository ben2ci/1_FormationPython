import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='test.log',
                    filemode="a",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('La fonction a bien été exécutée')
logging.info("Message d'information générale")
logging.warning("Attention")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")