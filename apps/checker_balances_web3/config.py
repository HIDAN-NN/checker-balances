networks_data = [
    {
        'chain': 'Ethereum',
        'coin': 'ETH',
        'chain_id': 1,
        'rpc': 'https://rpc.ankr.com/eth',
        'multicall_eth_contracts': "0xb1f8e55c7f64d203c1400b9d8555d050f94adf39",
        'tokens': {
            'USDT': '',
            'USDC': '',
        }
    },
    {
        'chain': 'Arbitrum One',
        'coin': 'ETH',
        'chain_id': 42161,
        'rpc': 'https://arb1.arbitrum.io/rpc',
        'multicall_eth_contracts': "0x151E24A486D7258dd7C33Fb67E4bB01919B7B32c",
        'tokens': {
            'USDT': '',
            'USDC': '0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
            'STG': '0x6694340fc020c5e6b96567843da2df01b2ce1eb6',
        },
    },
    {
        'chain': 'Optimism',
        'coin': 'ETH',
        'chain_id': 10,
        'rpc': 'https://optimism.llamarpc.com',
        'multicall_eth_contracts': "0xB1c568e9C3E6bdaf755A60c7418C269eb11524FC",
        'tokens': {
            'USDT': '',
            'USDC': '',
        }
    },
    {
        'chain': 'Avalanche',
        'coin': 'AVAX',
        'chain_id': 43114,
        'rpc': 'https://api.avax.network/ext/bc/C/rpc',
        'multicall_eth_contracts': "0xD023D153a0DFa485130ECFdE2FAA7e612EF94818",
        'tokens': {
            'USDT': '',
            'USDC': '',
        }
    },
    {
        'chain': 'BSC',
        'coin': 'BNB',
        'chain_id': 56,
        'rpc': 'https://bsc-dataseed.binance.org',
        'multicall_eth_contracts': "0x2352c63A83f9Fd126af8676146721Fa00924d7e4",
        'tokens': {
            'USDT': '',
            'USDC': '',
        }
    },
    {
        'chain': 'Polygon',
        'coin': 'MATIC',
        'chain_id': 137,
        'rpc': 'https://polygon-rpc.com',
        'multicall_eth_contracts': "0x2352c63A83f9Fd126af8676146721Fa00924d7e4",
        'tokens': {
            'USDC': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
            'WMATIC': '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270',
            'AAVE': '0xD6DF932A45C0f255f85145f286eA0b292B21C90B',
        }
    },
    {
        'chain': 'Fantom',
        'coin': 'FTM',
        'chain_id': 250,
        'rpc': 'https://rpc.ankr.com/fantom',
        'multicall_eth_contracts': "0x07f697424ABe762bB808c109860c04eA488ff92B",
        'tokens': {
            'USDT': '',
            'USDC': '',
        }
    },
]

MULTICALL_ETH_CONTRACTS = {
    'Ethereum': '0xb1f8e55c7f64d203c1400b9d8555d050f94adf39',
    'Arbitrum One': '0x151E24A486D7258dd7C33Fb67E4bB01919B7B32c',
    'Optimism': '0xB1c568e9C3E6bdaf755A60c7418C269eb11524FC',
    'Avalanche': '0xD023D153a0DFa485130ECFdE2FAA7e612EF94818',
    'BSC': '0x2352c63A83f9Fd126af8676146721Fa00924d7e4',
    'Polygon': '0x2352c63A83f9Fd126af8676146721Fa00924d7e4',
    'Fantom': '0x07f697424ABe762bB808c109860c04eA488ff92B',

    # 'era': '0x875fb0451fb2787b1924edc1DE4083E5f63D99Df',
    # 'zksync': '0x875fb0451fb2787b1924edc1DE4083E5f63D99Df',
    # 'nova': '0x3008e6ad64a470c47f428e73214c2f1f4e79b72d',
    # 'zora': '0x6830d287fE1dab06ABe252911caD71F37a0514A3',
    # 'linea': '0x3008e6ad64a470c47f428e73214C2F1f4e79b72d',
    # 'base': '0x162708433f00dbc8624795f181ec1983e418ef11',
    # 'polygon_zkevm': '0x162708433F00DBC8624795F181EC1983E418EF11',
    # 'core': '0xdAd633A2Ff9fb3Ab5d7a8bcfd089593c503c11a2',
    # 'gnosis': '0xd08149E71671A284e3F99b371BaF29BB8eEA7387',
    # 'goerli': '0x8242cd33761782f02bf10b7329cea5faf17b2bea',
    # 'moonbeam': '0xf614056a46e293DD701B9eCeBa5df56B354b75f9',
    # 'moonriver': '0xDEAa846cca7FEc9e76C8e4D56A55A75bb0973888',
    # 'aurora': '0x100665685d533F65bdD0BD1d65ca6387FC4F4FDB',
    # 'tron': 'TN8RtFXeQZyFHGmH1iiSRm5r4CRz1yWkCf',
    # 'celo': '0x6830d287fE1dab06ABe252911caD71F37a0514A3',
    # 'harmony': '0x3008e6ad64a470c47f428e73214c2f1f4e79b72d'
}
MULTICALL_ABI = '[{"constant":true,"inputs":[{"name":"user","type":"address"},{"name":"token","type":"address"}],"name":"tokenBalance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"users","type":"address[]"},{"name":"tokens","type":"address[]"}],"name":"balances","outputs":[{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"}]'

# MULTICALL_CONTRACTS = {
#     "Ethereum": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "Arbitrum One": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "Optimism": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "Avalanche": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "BSC": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "Polygon": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "Fantom": "0xcA11bde05977b3631167028862bE2a173976CA11",
#
#     "polygon_zkevm": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "nova": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "zksync": "0xF9cda624FBC7e059355ce98a31693d299FACd963",
#     "celo": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "gnosis": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "core": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "harmony": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "moonbeam": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "moonriver": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "linea": "0xcA11bde05977b3631167028862bE2a173976CA11",
#     "base": "0xcA11bde05977b3631167028862bE2a173976CA11"
# }
