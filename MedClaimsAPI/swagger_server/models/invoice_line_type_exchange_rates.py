# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.invoice_line_exchange_rate_type import InvoiceLineExchangeRateType  # noqa: F401,E501
from swagger_server import util


class InvoiceLineTypeExchangeRates(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, exchange_rate: List[InvoiceLineExchangeRateType]=None):  # noqa: E501
        """InvoiceLineTypeExchangeRates - a model defined in Swagger

        :param exchange_rate: The exchange_rate of this InvoiceLineTypeExchangeRates.  # noqa: E501
        :type exchange_rate: List[InvoiceLineExchangeRateType]
        """
        self.swagger_types = {
            'exchange_rate': List[InvoiceLineExchangeRateType]
        }

        self.attribute_map = {
            'exchange_rate': 'exchangeRate'
        }
        self._exchange_rate = exchange_rate

    @classmethod
    def from_dict(cls, dikt) -> 'InvoiceLineTypeExchangeRates':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvoiceLineType_exchangeRates of this InvoiceLineTypeExchangeRates.  # noqa: E501
        :rtype: InvoiceLineTypeExchangeRates
        """
        return util.deserialize_model(dikt, cls)

    @property
    def exchange_rate(self) -> List[InvoiceLineExchangeRateType]:
        """Gets the exchange_rate of this InvoiceLineTypeExchangeRates.


        :return: The exchange_rate of this InvoiceLineTypeExchangeRates.
        :rtype: List[InvoiceLineExchangeRateType]
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate: List[InvoiceLineExchangeRateType]):
        """Sets the exchange_rate of this InvoiceLineTypeExchangeRates.


        :param exchange_rate: The exchange_rate of this InvoiceLineTypeExchangeRates.
        :type exchange_rate: List[InvoiceLineExchangeRateType]
        """

        self._exchange_rate = exchange_rate
