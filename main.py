import asyncio

from apps import CheckerBalancesWeb3
from apps.checker_balances_web3.config import *
from tools import init_logger


def main() -> None:
    asyncio.run(
        CheckerBalancesWeb3(
            check_native_balance_bool=check_native_balance_bool,
            check_token_balance_bool=check_token_balance_bool,
            show_empty_native_balances_bool=show_empty_native_balances_bool,
            show_empty_token_balances_bool=show_empty_token_balances_bool
        ).main()
    )


if __name__ == "__main__":
    init_logger()
    main()
