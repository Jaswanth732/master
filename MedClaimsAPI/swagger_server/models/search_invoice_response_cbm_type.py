# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.invoice_type import InvoiceType  # noqa: F401,E501
from swagger_server import util


class SearchInvoiceResponseCBMType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice: List[InvoiceType]=None):  # noqa: E501
        """SearchInvoiceResponseCBMType - a model defined in Swagger

        :param invoice: The invoice of this SearchInvoiceResponseCBMType.  # noqa: E501
        :type invoice: List[InvoiceType]
        """
        self.swagger_types = {
            'invoice': List[InvoiceType]
        }

        self.attribute_map = {
            'invoice': 'invoice'
        }
        self._invoice = invoice

    @classmethod
    def from_dict(cls, dikt) -> 'SearchInvoiceResponseCBMType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SearchInvoiceResponseCBMType of this SearchInvoiceResponseCBMType.  # noqa: E501
        :rtype: SearchInvoiceResponseCBMType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice(self) -> List[InvoiceType]:
        """Gets the invoice of this SearchInvoiceResponseCBMType.


        :return: The invoice of this SearchInvoiceResponseCBMType.
        :rtype: List[InvoiceType]
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice: List[InvoiceType]):
        """Sets the invoice of this SearchInvoiceResponseCBMType.


        :param invoice: The invoice of this SearchInvoiceResponseCBMType.
        :type invoice: List[InvoiceType]
        """

        self._invoice = invoice
