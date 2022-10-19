from .client import Client
from .consts import *


class PublicAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag)

    # Get Instruments
    def get_instruments(self, instType, uly=None, instId=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId}
        return self._request_with_params(GET, INSTRUMENT_INFO, params)

    # Get Delivery/Exercise History
    def get_deliver_history(self, instType, uly, after=None, before=None, limit=None):
        params = {'instType': instType, 'uly': uly, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, DELIVERY_EXERCISE, params)

    # Get Open Interest
    def get_open_interest(self, instType, uly=None, instId=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId}
        return self._request_with_params(GET, OPEN_INTEREST, params)

    # Get Funding Rate
    def get_funding_rate(self, instId):
        params = {'instId': instId}
        return self._request_with_params(GET, FUNDING_RATE, params)

    # Get Funding Rate History
    def funding_rate_history(self, instId, after=None, before=None, limit=None):
        params = {'instId': instId, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, FUNDING_RATE_HISTORY, params)

    # Get Limit Price
    def get_price_limit(self, instId):
        params = {'instId': instId}
        return self._request_with_params(GET, PRICE_LIMIT, params)

    # Get Option Market Data
    def get_opt_summary(self, uly, expTime=None):
        params = {'uly': uly, 'expTime': expTime}
        return self._request_with_params(GET, OPT_SUMMARY, params)

    # Get Estimated Delivery/Excercise Price
    def get_estimated_price(self, instId):
        params = {'instId': instId}
        return self._request_with_params(GET, ESTIMATED_PRICE, params)

    # Get Discount Rate And Interest-Free Quota
    def discount_interest_free_quota(self, ccy=None):
        params = {'ccy': ccy}
        return self._request_with_params(GET, DICCOUNT_INTETEST_INFO, params)

    # Get System Time
    def get_system_time(self):
        return self._request_without_params(GET, SYSTEM_TIME)

    # Get Liquidation Orders
    def get_liquidation_orders(self, instType, mgnMode=None, instId=None, ccy=None, uly=None, alias=None, state=None, before=None,
                               after=None, limit=None):
        params = {'instType': instType, 'mgnMode': mgnMode, 'instId': instId, 'ccy': ccy, 'uly': uly,
                  'alias': alias, 'state': state, 'before': before, 'after': after, 'limit': limit}
        return self._request_with_params(GET, LIQUIDATION_ORDERS, params)

    # Get Mark Price
    def get_mark_price(self, instType, uly=None, instId=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId}
        return self._request_with_params(GET, MARK_PRICE, params)

    # Get Tier
    def get_tier(self, instType, tdMode, uly=None, instId=None, ccy=None, tier=None):
        params = {'instType': instType, 'tdMode': tdMode, 'uly': uly, 'instId': instId, 'ccy': ccy, 'tier': tier}
        return self._request_with_params(GET, MARK_PRICE, params)

    def get_interest_rate(self):
        return self._request_without_params(GET, INTEREST_RATE_LOAN_QUATA)

    def get_vip_interest_rate(self):
        return self._request_without_params(GET, VIP_INTEREST_RATE_LOAN_QUATA)
