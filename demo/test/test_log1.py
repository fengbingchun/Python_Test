import logging
logger = logging.getLogger(__name__)

def fun(x, y):
	logger.debug("x=%s, y=%s", x, y)
	logger.info("x=%s, y=%s", x, y)
	logger.warning("x=%s, y=%s", x, y)
	logger.error("x=%s, y=%s", x, y)
	logger.critical("x=%s, y=%s", x, y)
