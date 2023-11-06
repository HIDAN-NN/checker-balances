import logging
import sys

from colorlog import ColoredFormatter


def init_logging(is_verbose: bool = False):
    formatter = ColoredFormatter(
        "%(log_color)s[%(asctime)s.%(msecs)03d] "
        "[PROCESS %(process)d %(processName)s] "
        "[%(threadName)-10s] "
        "%(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            'DEBUG': 'cyan',
            # 'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(console)

    root_logger.setLevel(logging.DEBUG if is_verbose else logging.INFO)
