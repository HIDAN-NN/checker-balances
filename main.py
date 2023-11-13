import asyncio

from apps import CheckerBalancesWeb3
from tools import init_logger


def main() -> None:
    asyncio.run(
        CheckerBalancesWeb3(
            check_native_balance_bool=True,
            check_token_balance_bool=True,
            show_empty_native_balances_bool=False,
            show_empty_token_balances_bool=False
        ).main()
    )


if __name__ == "__main__":
    init_logger()
    main()
