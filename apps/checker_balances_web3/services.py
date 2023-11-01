from web3 import Web3
from web3.middleware import geth_poa_middleware


class Web3Middleware:
    def __init__(self, rpc):
        self.rpc = rpc
        self.web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=self.rpc))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
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
