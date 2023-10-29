from web3 import Web3
from web3.middleware import geth_poa_middleware


def web3_node_connect(rpc: str) -> Web3:
    web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=rpc))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.account.enable_unaudited_hdwallet_features()

    return web3


def check_native_balance(web3_node_connect, address: str) -> float:
    checksum_address = web3_node_connect.to_checksum_address(address)
    gwei_balance = web3_node_connect.eth.get_balance(checksum_address)
    return float(Web3.from_wei(gwei_balance, 'ether'))


def check_token_balance(web3_node_connect, token_address: str, ERC20_ABI: list, address: str) -> float:
    token_contract = web3_node_connect.eth.contract(address=token_address, abi=ERC20_ABI)
    decimals = token_contract.functions.decimals().call()
    gwei_token_balance = token_contract.functions.balanceOf(address).call()

    return gwei_token_balance / 10 ** decimals


def convert_balance_to_dollar(trading_pairs_data: list, symbol: str, balance: [float, int]) -> [float, None]:
    for trading_pair in trading_pairs_data:
        if trading_pair['currency_pair'] == f"{symbol}_USDT":
            return round(balance * float(trading_pair['last']), 2)
    return None
