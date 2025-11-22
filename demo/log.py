from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler

# Blog: https://blog.csdn.net/fengbingchun/article/details/155137379

log_dir = "log"
if not Path(log_dir).exists():
    Path(log_dir).mkdir(parents=True)

formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()
if logger.handlers:
    logger.handlers.clear()

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

log_file = log_dir + "/log.feng"
file_handler = TimedRotatingFileHandler(
    log_file,
    when="midnight",
    interval=1,
    backupCount=100,
    encoding="utf-8",
    delay=False,
    utc=False
)
file_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
