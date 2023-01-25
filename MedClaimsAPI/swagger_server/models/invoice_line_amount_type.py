# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amount_type import AmountType  # noqa: F401,E501
from swagger_server import util


class InvoiceLineAmountType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amount_id: str=None, invoice_amount: AmountType=None, payment_amount: AmountType=None, product_amount: AmountType=None):  # noqa: E501
        """InvoiceLineAmountType - a model defined in Swagger

        :param amount_id: The amount_id of this InvoiceLineAmountType.  # noqa: E501
        :type amount_id: str
        :param invoice_amount: The invoice_amount of this InvoiceLineAmountType.  # noqa: E501
        :type invoice_amount: AmountType
        :param payment_amount: The payment_amount of this InvoiceLineAmountType.  # noqa: E501
        :type payment_amount: AmountType
        :param product_amount: The product_amount of this InvoiceLineAmountType.  # noqa: E501
        :type product_amount: AmountType
        """
        self.swagger_types = {
            'amount_id': str,
            'invoice_amount': AmountType,
            'payment_amount': AmountType,
            'product_amount': AmountType
        }

        self.attribute_map = {
            'amount_id': 'amountId',
            'invoice_amount': 'invoiceAmount',
            'payment_amount': 'paymentAmount',
            'product_amount': 'productAmount'
        }
        self._amount_id = amount_id
        self._invoice_amount = invoice_amount
        self._payment_amount = payment_amount
        self._product_amount = product_amount

    @classmethod
    def from_dict(cls, dikt) -> 'InvoiceLineAmountType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvoiceLineAmountType of this InvoiceLineAmountType.  # noqa: E501
        :rtype: InvoiceLineAmountType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount_id(self) -> str:
        """Gets the amount_id of this InvoiceLineAmountType.


        :return: The amount_id of this InvoiceLineAmountType.
        :rtype: str
        """
        return self._amount_id

    @amount_id.setter
    def amount_id(self, amount_id: str):
        """Sets the amount_id of this InvoiceLineAmountType.


        :param amount_id: The amount_id of this InvoiceLineAmountType.
        :type amount_id: str
        """

        self._amount_id = amount_id

    @property
    def invoice_amount(self) -> AmountType:
        """Gets the invoice_amount of this InvoiceLineAmountType.


        :return: The invoice_amount of this InvoiceLineAmountType.
        :rtype: AmountType
        """
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, invoice_amount: AmountType):
        """Sets the invoice_amount of this InvoiceLineAmountType.


        :param invoice_amount: The invoice_amount of this InvoiceLineAmountType.
        :type invoice_amount: AmountType
        """

        self._invoice_amount = invoice_amount

    @property
    def payment_amount(self) -> AmountType:
        """Gets the payment_amount of this InvoiceLineAmountType.


        :return: The payment_amount of this InvoiceLineAmountType.
        :rtype: AmountType
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount: AmountType):
        """Sets the payment_amount of this InvoiceLineAmountType.


        :param payment_amount: The payment_amount of this InvoiceLineAmountType.
        :type payment_amount: AmountType
        """

        self._payment_amount = payment_amount

    @property
    def product_amount(self) -> AmountType:
        """Gets the product_amount of this InvoiceLineAmountType.


        :return: The product_amount of this InvoiceLineAmountType.
        :rtype: AmountType
        """
        return self._product_amount

    @product_amount.setter
    def product_amount(self, product_amount: AmountType):
        """Sets the product_amount of this InvoiceLineAmountType.


        :param product_amount: The product_amount of this InvoiceLineAmountType.
        :type product_amount: AmountType
        """

        self._product_amount = product_amount
