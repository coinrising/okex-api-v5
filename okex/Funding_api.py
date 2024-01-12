from .client import Client
from .consts import *


class FundingAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag)

    # Get Deposit Address
    def get_deposit_address(self, ccy):
        params = {'ccy': ccy}
        return self._request_with_params(GET, DEPOSIT_ADDRESS, params)

    # Get Balance
    def get_balances(self, ccy=None):
        params = {'ccy': ccy}
        return self._request_with_params(GET, GET_BALANCES, params)

    # Get Account Configuration
    def funds_transfer(self, ccy, amt, froms, to, type='0', subAcct=None, instId=None, toInstId=None):
        params = {'ccy': ccy, 'amt': amt, 'from': froms, 'to': to, 'type': type, 'subAcct': subAcct, 'instId': instId,
                  'toInstId': toInstId}
        return self._request_with_params(POST, FUNDS_TRANSFER, params)

    # Withdrawal
    def coin_withdraw(self, ccy, amt, dest, toAddr, pwd, fee):
        params = {'ccy': ccy, 'amt': amt, 'dest': dest, 'toAddr': toAddr, 'pwd': pwd, 'fee': fee}
        return self._request_with_params(POST, WITHDRAWAL_COIN, params)

    # Get Deposit History
    def get_deposit_history(self, ccy=None, state=None, after=None, before=None, limit=None):
        params = {'ccy': ccy, 'state': state, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, DEPOSIT_HISTORY, params)

    # Get Withdrawal History
    def get_withdrawal_history(self, ccy=None, state=None, after=None, before=None, limit=None):
        params = {'ccy': ccy, 'state': state, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, WITHDRAWAL_HISTORY, params)

    # Get Currencies
    def get_currency(self):
        return self._request_without_params(GET, CURRENCY_INFO)

    # PiggyBank Purchase/Redemption
    def purchase_redempt(self, ccy, amt, side):
        params = {'ccy': ccy, 'amt': amt, 'side': side}
        return self._request_with_params(POST, PURCHASE_REDEMPT, params)

    # Get Withdrawal History
    def get_bills(self, ccy=None, type=None, after=None, before=None, limit=None):
        params = {'ccy': ccy, 'type': type, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, BILLS_INFO, params)

    def eth_staking_purchase(self, amt):
        params = {'amt': amt}
        return self._request_with_params(POST, ETH_STAKING_PURCHASE, params)

    def eth_staking_redeem(self, amt):
        params = {'amt': amt}
        return self._request_with_params(POST, ETH_STAKING_REDEEM, params)

    def get_eth_staking_balance(self):
        return self._request_with_params(GET, ETH_STAKING_BALANCE)

    def get_eth_staking_history(self, type=None, status=None, after=None, before=None, limit=None):
        params = {'type': type, 'status': status, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, ETH_STAKING_HISTORY, params)

    def get_eth_staking_apy_history(self, days=None):
        params = {'days': days}
        return self._request_with_params(GET, ETH_STAKING_APY_HISTORY, params)
