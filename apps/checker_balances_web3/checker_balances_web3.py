import logging
import random
import time

from apps.checker_balances_web3.services import Web3Middleware
from apps.checker_balances_web3.utils import (
    get_addresses_from_txt_file_as_list,
    get_erc20_data_from_json_file_as_list,
    get_trading_pairs_data_as_list,
    convert_balance_to_dollar
)


class CheckerBalancesWeb3():
    def __init__(self,
                 networks_data: list,
                 native_balance_bool: bool,
                 token_balance_bool: bool,
                 sleep_form: [float, int] = 0,
                 sleep_to: [float, int] = 0
                 ):

        self.web3_middleware: Web3Middleware = Web3Middleware
        self.networks_data: list = networks_data
        self.native_balance_bool: bool = native_balance_bool
        self.token_balance_bool: bool = token_balance_bool
        self.sleep_form: [float, int] = sleep_form
        self.sleep_to: [float, int] = sleep_to
        self._addresses_list: list = get_addresses_from_txt_file_as_list()
        self.erc20_data_as_list: list = get_erc20_data_from_json_file_as_list()
        self.trading_pairs_data_list: list = get_trading_pairs_data_as_list()
        self.convert_balance_to_dollar: [float, None] = convert_balance_to_dollar

    def check_native_balance(self, address: str, network_data: list, web3_middleware) -> None:
        native_balance = web3_middleware.get_native_balance(address=address)
        balance_to_dollar = self.convert_balance_to_dollar(
            trading_pairs_data=self.trading_pairs_data_list,
            symbol=network_data['coin'],
            balance=native_balance
        )
        time.sleep(random.uniform(self.sleep_form, self.sleep_to))
        logging.info(
            f"{address} - {network_data['chain']} - {round(native_balance, 6)} {network_data['coin']} - "
            f"{balance_to_dollar} $"
        )

    def check_token_balance(self, address: str, network_data: list, web3_middleware) -> None:
        for token in network_data['tokens'].items():
            if len(token[1]) >= 42:
                token_balance = web3_middleware.get_token_balance(
                    token_address=web3_middleware.checksum_address(token[1]),
                    erc20_abi=self.erc20_data_as_list,
                    address=address
                )
                if token[0] in ['USDT', 'BUSD', 'DAI', 'USDC']:
                    time.sleep(random.uniform(self.sleep_form, self.sleep_to))
                    logging.info(f"{address} - {network_data['chain']} - {round(token_balance, 2)} {token[0]}")
                else:
                    balance_to_dollar = self.convert_balance_to_dollar(
                        trading_pairs_data=self.trading_pairs_data_list,
                        symbol=token[0],
                        balance=token_balance
                    )
                    time.sleep(random.uniform(self.sleep_form, self.sleep_to))
                    logging.info(
                        f"{address} - {network_data['chain']} - {round(token_balance, 6)} {token[0]} - "
                        f"{balance_to_dollar} $"
                    )

    def main(self):
        for network_data in self.networks_data:
            web3_middleware = self.web3_middleware(rpc=network_data['rpc'])
            for address in self._addresses_list:
                if self.native_balance_bool:
                    self.check_native_balance(
                        address=web3_middleware.checksum_address(address),
                        network_data=network_data,
                        web3_middleware=web3_middleware
                    )
                if self.token_balance_bool:
                    self.check_token_balance(
                        address=web3_middleware.checksum_address(address),
                        network_data=network_data,
                        web3_middleware=web3_middleware
                    )
