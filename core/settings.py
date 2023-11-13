import pathlib
import sys
from pathlib import Path
from typing import Final

if getattr(sys, 'frozen', False):
    ROOT_PATH = Path(sys.executable).parent.absolute()
else:
    ROOT_PATH = Path(__file__).parent.parent.absolute()

ADDRESSES_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('data/addresses.txt')
ERC20_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('data/erc20.json')
LOGS_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('results/logfile.log')

# Example Path
# ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]

# Example typing
# T_URL: TypeAlias = str
# T_URLS: TypeAlias = list[T_URL]
#
# T_HTML_TEXT: TypeAlias = str
# T_HTML_TEXTS: TypeAlias = list[T_HTML_TEXT]
#
# T_FILE_NAME: TypeAlias = str
# T_TXT_FILE: TypeAlias = str
# T_JSON_FILE: TypeAlias = str
