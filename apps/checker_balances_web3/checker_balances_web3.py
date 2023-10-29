import logging
import random
import time

from apps.checker_balances_web3.config import networks_data
from apps.checker_balances_web3.services import web3_node_connect, check_native_balance, check_token_balance, \
    convert_balance_to_dollar
from apps.checker_balances_web3.utils import (
    _get_addresses_from_txt_file_as_list,
    _get_erc20_data_from_json_file_as_list, _get_trading_pairs_data_as_list
)


def checker_balances_web3(
        native_balance_bool: bool = True,
        token_balance_bool: bool = True,
        sleep_form: [float, int] = 0.5,
        sleep_to: [float, int] = 1
) -> None:
    addresses_list = _get_addresses_from_txt_file_as_list()
    erc20_data_as_list = _get_erc20_data_from_json_file_as_list()
    trading_pairs_data_list = _get_trading_pairs_data_as_list()

    for network_data in networks_data:
        web3 = web3_node_connect(rpc=network_data['rpc'])
        for address in addresses_list:
            if native_balance_bool:
                native_balance = check_native_balance(web3_node_connect=web3, address=address)
                balance_to_dollar = convert_balance_to_dollar(
                    trading_pairs_data=trading_pairs_data_list,
                    symbol=network_data['coin'],
                    balance=native_balance
                )
                time.sleep(random.uniform(sleep_form, sleep_to))
                logging.info(
                    f"{address} - {network_data['chain']} - {round(native_balance, 6)} {network_data['coin']} - {balance_to_dollar} $"
                )
            if token_balance_bool:
                for token in network_data['tokens'].items():
                    if len(token[1]) >= 42:
                        token_balance = check_token_balance(
                            web3_node_connect=web3,
                            token_address=web3.to_checksum_address(token[1]),
                            ERC20_ABI=erc20_data_as_list,
                            address=address
                        )
                        if token[0] in {'USDT', 'BUSD', 'DAI', 'USDC'}:
                            time.sleep(random.uniform(sleep_form, sleep_to))
                            logging.info(f"{address} - {network_data['chain']} - {round(token_balance, 2)} {token[0]}")
                        else:
                            balance_to_dollar = convert_balance_to_dollar(
                                trading_pairs_data=trading_pairs_data_list,
                                symbol=token[0],
                                balance=token_balance
                            )
                            time.sleep(random.uniform(sleep_form, sleep_to))
                            logging.info(
                                f"{address} - {network_data['chain']} - {round(token_balance, 2)} {token[0]} - {balance_to_dollar} $"
                            )
