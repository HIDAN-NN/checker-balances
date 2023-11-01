from apps.checker_balances_web3.checker_balances_web3 import CheckerBalancesWeb3
from apps.checker_balances_web3.config import networks_data

from tools.init_logging import init_logging


def main(networks_data) -> None:
    CheckerBalancesWeb3(
        networks_data=networks_data,
        native_balance_bool=True,
        token_balance_bool=False,
        sleep_form=0.5,
        sleep_to=1
    ).main()


if __name__ == "__main__":
    init_logging()
    main(networks_data)
