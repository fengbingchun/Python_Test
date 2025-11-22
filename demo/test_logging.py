import argparse
import colorama
import log
import logging
from test import test_log1, test_log2

logger = logging.getLogger(__name__)

def parse_args():
	parser = argparse.ArgumentParser(description="logging test code")
	parser.add_argument("--level", type=str, default="WARNING", choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="specify log level")

	args = parser.parse_args()
	return args

def fun(x, y):
	logger.debug("x=%s, y=%s", x, y)
	logger.info("x=%s, y=%s", x, y)
	logger.warning("x=%s, y=%s", x, y)
	logger.error("x=%s, y=%s", x, y)
	logger.critical("x=%s, y=%s", x, y)

def main():
	x = {"a": 1, "b": 2}; y = ("abc", 123)
	fun(x, y)

	x = 1; y = [1, 2, 3]
	test_log1.fun(x, y)

	x = 3.45678; y = "hello"
	test_log2.fun(x, y)

if __name__ == "__main__":
	colorama.init(autoreset=True)
	args = parse_args()

	logging.getLogger().setLevel(args.level)

	main()

	print(colorama.Fore.GREEN + "====== execution completed ======")
