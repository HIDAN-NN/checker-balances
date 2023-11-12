from web3 import Web3, AsyncHTTPProvider
from web3.eth import AsyncEth

from apps.checker_balances_web3.config import MULTICALL_ABI


class Web3Middleware:

    def __init__(self, rpc):
        self.rpc = rpc
        self.web3 = Web3(AsyncHTTPProvider(self.rpc), modules={"eth": AsyncEth}, middlewares=[])
        # self.web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=self.rpc))
        # self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.web3.eth.account.enable_unaudited_hdwallet_features()
        self.checksum_address = self.web3.to_checksum_address

    def get_native_balance(self, address: str) -> float:
        gwei_balance = self.web3.eth.get_balance(self.checksum_address(address))

        return float(Web3.from_wei(gwei_balance, 'ether'))

    def get_token_balance(self, token_address: str, erc20_abi: list, address: str) -> float:
        token_contract = self.web3.eth.contract(address=token_address, abi=erc20_abi)
        decimals = token_contract.functions.decimals().call()
        gwei_token_balance = token_contract.functions.balanceOf(self.checksum_address(address)).call()

        return gwei_token_balance / 10 ** decimals

    async def get_native_balance_multicall(self, multicall_eth_contracts: str, address_list: list[str], ) -> list:
        checksum_address_list = [self.checksum_address(address) for address in address_list]
        checksum_tokens_address = [self.checksum_address('0x0000000000000000000000000000000000000000')]
        multicall_contract = self.web3.eth.contract(
            address=self.checksum_address(multicall_eth_contracts), abi=MULTICALL_ABI
        )
        multicall_balances = await multicall_contract.functions.balances(
            checksum_address_list, checksum_tokens_address
        ).call()
        return [
            [address, float(Web3.from_wei(balance, 'ether'))]
            for balance, address in zip(multicall_balances, checksum_address_list)
        ]

    async def get_token_balance_multicall(self,
                                          multicall_eth_contracts: str,
                                          address_list: list[str],
                                          erc20_data_list: list,
                                          tokens_tickets_list: list,
                                          tokens_address_list: [list[str], None] = None,
                                          ) -> bool and list:
        checksum_address_list = [self.checksum_address(address) for address in address_list]
        if len(tokens_address_list) == 0:
            return False, checksum_address_list
        checksum_tokens_address_list = [self.checksum_address(token_address) for token_address in tokens_address_list]
        contracts_list = [
            self.web3.eth.contract(address=token_address, abi=erc20_data_list)
            for token_address in checksum_tokens_address_list
        ]
        decimals_list = [await contract.functions.decimals().call() for contract in contracts_list]
        multicall_contract = self.web3.eth.contract(
            address=self.checksum_address(multicall_eth_contracts), abi=MULTICALL_ABI
        )
        multicall_balances = await multicall_contract.functions.balances(
            checksum_address_list, checksum_tokens_address_list
        ).call()
        tokens_balances_multicall_data = [[address] for address in checksum_address_list]
        for i_one, i_two in zip(
                range(0, len(multicall_balances), len(tokens_tickets_list)),
                range(len(checksum_address_list))
        ):
            balance_by_address = multicall_balances[i_one:i_one + len(tokens_tickets_list)]
            for i in range(len(tokens_tickets_list)):
                tokens_balances_multicall_data[i_two].append(
                    {tokens_tickets_list[i]: balance_by_address[i] / 10 ** decimals_list[i]}
                )
        return True, tokens_balances_multicall_data
