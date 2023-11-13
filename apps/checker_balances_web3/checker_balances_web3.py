import asyncio
import logging
import random
import time

from loguru import logger

from .config import networks_data
from .services import Web3Middleware
from .utils import (
    get_addresses_from_txt_file_as_list,
    get_erc20_data_from_json_file_as_list,
    get_trading_pairs_data_as_list,
    convert_balance_to_dollar
)


class CheckerBalancesWeb3():
    networks_data = networks_data

    def __init__(self,
                 check_native_balance_bool: bool = True,
                 check_token_balance_bool: bool = False,
                 show_empty_native_balances_bool: bool = False,
                 show_empty_token_balances_bool: bool = False,
                 sleep_form: [float, int] = 0,
                 sleep_to: [float, int] = 0
                 ):

        self.web3_middleware: Web3Middleware = Web3Middleware
        self.check_native_balance_bool: bool = check_native_balance_bool
        self.check_token_balance_bool: bool = check_token_balance_bool
        self.show_empty_native_balances_bool: bool = show_empty_native_balances_bool
        self.show_empty_token_balances_bool: bool = show_empty_token_balances_bool
        self.sleep_form: [float, int] = sleep_form
        self.sleep_to: [float, int] = sleep_to
        self._addresses_list: list = get_addresses_from_txt_file_as_list()
        self.erc20_data_list: list = get_erc20_data_from_json_file_as_list()
        self.trading_pairs_data_list: list = get_trading_pairs_data_as_list()
        self.convert_balance_to_dollar: [float, None] = convert_balance_to_dollar

    def check_native_balance(self, address: str, network_data: list, web3_middleware: Web3Middleware) -> None:
        native_balance = web3_middleware.get_native_balance(address=address)
        balance_to_dollar = self.convert_balance_to_dollar(
            trading_pairs_data=self.trading_pairs_data_list,
            symbol=network_data['coin'],
            balance=native_balance
        )
        time.sleep(random.uniform(self.sleep_form, self.sleep_to))
        logger.success(
            f"{address} - {network_data['chain']} - {round(native_balance, 6)} - {network_data['coin']}"
            f"{balance_to_dollar} $"
        )

    def check_token_balance(self, address: str, network_data: list, web3_middleware: Web3Middleware) -> None:
        for token in network_data['tokens'].items():
            if len(token[1]) >= 42:
                token_balance = web3_middleware.get_token_balance(
                    token_address=web3_middleware.checksum_address(token[1]),
                    erc20_abi=self.erc20_data_list,
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
                    logger.success(
                        f"{address} - {network_data['chain']} - {round(token_balance, 6)} {token[0]} - "
                        f"{balance_to_dollar} $"
                    )

    async def check_native_balance_multicall(self, web3_middleware: Web3Middleware, network_data: list):

        native_balance_multicall_data = await  web3_middleware.get_native_balance_multicall(
            multicall_eth_contracts=network_data['multicall_eth_contracts'],
            address_list=self._addresses_list,
        )
        if native_balance_multicall_data is None:
            return

        for data in native_balance_multicall_data:
            if data[1] > 0:
                balance_to_dollar = self.convert_balance_to_dollar(
                    trading_pairs_data=self.trading_pairs_data_list,
                    symbol=network_data['coin'],
                    balance=data[1]
                )
                logger.info(
                    f"{data[0]} | {network_data['chain']} | {round(data[1], 6)} | {network_data['coin']} |"
                    f" {balance_to_dollar} $ | Native"
                )
            elif self.show_empty_native_balances_bool:
                logger.warning(
                    f"{data[0]} - {network_data['chain']} | {round(data[1], 6)} - {network_data['coin']} | Native"
                )

    async def check_token_balance_multicall(self,
                                            web3_middleware: Web3Middleware,
                                            network_data: list
                                            ):
        is_full_data, tokens_balances_multicall_data = await  web3_middleware.get_token_balance_multicall(
            multicall_eth_contracts=network_data['multicall_eth_contracts'],
            address_list=self._addresses_list,
            erc20_data_list=self.erc20_data_list,
            tokens_tickets_list=[token[0] for token in network_data['tokens'].items() if len(token[1]) >= 42],
            tokens_address_list=[token[1] for token in network_data['tokens'].items() if len(token[1]) >= 42],
        )
        if is_full_data is None and tokens_balances_multicall_data is None:
            return

        if is_full_data:
            for data in tokens_balances_multicall_data:
                for token in data[1:]:
                    for ticket in token:
                        if ticket in ['USDT', 'BUSD', 'DAI', 'USDC']:
                            logger.info(
                                f"{data[0]} | {network_data['chain']} | {round(token[ticket], 6)} {ticket} | Stable"
                            )
                        else:
                            balance_to_dollar = self.convert_balance_to_dollar(
                                trading_pairs_data=self.trading_pairs_data_list,
                                symbol=ticket,
                                balance=token[ticket]
                            )
                            logger.info(
                                f"{data[0]} | {network_data['chain']} | {round(token[ticket], 6)} {ticket} | "
                                f"{balance_to_dollar} $ | Token"
                            )
        if not is_full_data and self.show_empty_token_balances_bool:
            for data in tokens_balances_multicall_data:
                logger.warning(f"{data} | {network_data['chain']} | None | Tokens")

    async def main(self):
        logger.success(
            "Check balance Web3 | Start"
        )
        if self.check_native_balance_bool:
            tasks = [
                self.check_native_balance_multicall(
                    web3_middleware=self.web3_middleware(rpc=network_data['rpc']),
                    network_data=network_data)
                for network_data in self.networks_data
            ]
            await asyncio.gather(*tasks)

        if self.check_token_balance_bool:
            tasks = [
                self.check_token_balance_multicall(
                    web3_middleware=self.web3_middleware(rpc=network_data['rpc']),
                    network_data=network_data)
                for network_data in self.networks_data
            ]
            await asyncio.gather(*tasks)

        logger.success(
            "Check balance Web3 | End"
        )
