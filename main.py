from apps.checker_balances_web3.checker_balances_web3 import checker_balances_web3

from tools.init_logging import init_logging


def main() -> None:
    checker_balances_web3(native_balance_bool=False, token_balance_bool=True)


if __name__ == "__main__":
    init_logging()
    main()
