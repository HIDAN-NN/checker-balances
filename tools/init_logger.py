import sys

from loguru import logger

from core import LOGS_PATH


# import logging
# from colorlog import ColoredFormatter

# logging
# def init_logging(is_verbose: bool = False):
#     formatter = ColoredFormatter(
#         "%(log_color)s[%(asctime)s.%(msecs)03d] "
#         # "[PROCESS %(process)d %(processName)s] "
#         # "[%(threadName)-10s] "
#         "%(levelname)s - %(message)s",
#         datefmt="%Y-%m-%d %H:%M:%S",
#         log_colors={
#             'DEBUG': 'cyan',
#             # 'INFO': 'green',
#             'WARNING': 'yellow',
#             'ERROR': 'red',
#             'CRITICAL': 'red,bg_white',
#         },
#         secondary_log_colors={},
#         style='%'
#     )
#
#     console = logging.StreamHandler(sys.stdout)
#     console.setFormatter(formatter)
#
#     root_logger = logging.getLogger()
#     root_logger.addHandler(console)
#
#     root_logger.setLevel(logging.DEBUG if is_verbose else logging.INFO)

# Example for start file
# if __name__ == "__main__":
#     init_logging(is_verbose=False)


# logger from loguru
def init_logger():
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
        "| <level>{level}</level> "
        "| <cyan>{function}</cyan> "
        "| <level>{message}</level>"
    )
    logger.configure(
        handlers=[
            dict(sink=sys.stderr, format=log_format),
            dict(sink=LOGS_PATH, enqueue=True),  # serialize=True
        ],
        # levels=[dict(name="NEW", no=13, icon="¤", color="")],
        extra={"common_to_all": "default"},
        activation=[("my_module.secret", False), ("another_library.module", True)],
    )
