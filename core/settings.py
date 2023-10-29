import pathlib
from typing import Final, TypeAlias

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
ADDRESSES_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('data').joinpath('addresses.txt')
ERC20_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('data').joinpath('erc20.json')



# T_WEB3_CLIENT: TypeAlias = classmethod





# Example

OUTPUT_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('results')
INPUT_PATH: Final[pathlib.Path] = ROOT_PATH.joinpath('app/input_urls.txt')

T_URL: TypeAlias = str
T_URLS: TypeAlias = list[T_URL]

T_HTML_TEXT: TypeAlias = str
T_HTML_TEXTS: TypeAlias = list[T_HTML_TEXT]

T_FILE_NAME: TypeAlias = str
T_TXT_FILE: TypeAlias = str
T_JSON_FILE: TypeAlias = str
