# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.exchange_rate_type import ExchangeRateType  # noqa: F401,E501
from swagger_server import util


class InvoiceTypeExchangeRates(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, exchange_rate: List[ExchangeRateType]=None):  # noqa: E501
        """InvoiceTypeExchangeRates - a model defined in Swagger

        :param exchange_rate: The exchange_rate of this InvoiceTypeExchangeRates.  # noqa: E501
        :type exchange_rate: List[ExchangeRateType]
        """
        self.swagger_types = {
            'exchange_rate': List[ExchangeRateType]
        }

        self.attribute_map = {
            'exchange_rate': 'exchangeRate'
        }
        self._exchange_rate = exchange_rate

    @classmethod
    def from_dict(cls, dikt) -> 'InvoiceTypeExchangeRates':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvoiceType_exchangeRates of this InvoiceTypeExchangeRates.  # noqa: E501
        :rtype: InvoiceTypeExchangeRates
        """
        return util.deserialize_model(dikt, cls)

    @property
    def exchange_rate(self) -> List[ExchangeRateType]:
        """Gets the exchange_rate of this InvoiceTypeExchangeRates.


        :return: The exchange_rate of this InvoiceTypeExchangeRates.
        :rtype: List[ExchangeRateType]
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate: List[ExchangeRateType]):
        """Sets the exchange_rate of this InvoiceTypeExchangeRates.


        :param exchange_rate: The exchange_rate of this InvoiceTypeExchangeRates.
        :type exchange_rate: List[ExchangeRateType]
        """

        self._exchange_rate = exchange_rate
