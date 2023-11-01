from json import load

import requests

from core.settings import ADDRESSES_PATH, ERC20_PATH


def _get_addresses_from_txt_file_as_list(path: str = ADDRESSES_PATH) -> list[str]:
    with open(path) as f:
        wallets_list = [row.strip() for row in f.readlines()]
    return wallets_list


def _get_erc20_data_from_json_file_as_list(path: str = ERC20_PATH) -> list[dict]:
    with open(path, "r", encoding='utf-8') as f:
        ERC20_ABI = load(f)
    return ERC20_ABI


def _get_trading_pairs_data_as_list() -> list[dict]:
    return requests.get(url='https://api.gateio.ws/api/v4/spot/tickers').json()


def _convert_balance_to_dollar(trading_pairs_data: list, symbol: str, balance: [float, int]) -> [float, None]:
    return next(
        (
            round(balance * float(trading_pair['last']), 2)
            for trading_pair in trading_pairs_data
            if trading_pair['currency_pair'] == f"{symbol}_USDT"
        ),
        None,
    )
