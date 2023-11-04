from apps import CheckerBalancesWeb3

from tools import init_logging


def main() -> None:
    CheckerBalancesWeb3(
        native_balance_bool=True,
        token_balance_bool=False,
        sleep_form=0.5,
        sleep_to=1
    ).main()


if __name__ == "__main__":
    init_logging()
    main()
