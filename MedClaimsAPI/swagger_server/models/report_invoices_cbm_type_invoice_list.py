# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReportInvoicesCBMTypeInvoiceList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice_id: List[str]=None):  # noqa: E501
        """ReportInvoicesCBMTypeInvoiceList - a model defined in Swagger

        :param invoice_id: The invoice_id of this ReportInvoicesCBMTypeInvoiceList.  # noqa: E501
        :type invoice_id: List[str]
        """
        self.swagger_types = {
            'invoice_id': List[str]
        }

        self.attribute_map = {
            'invoice_id': 'invoiceId'
        }
        self._invoice_id = invoice_id

    @classmethod
    def from_dict(cls, dikt) -> 'ReportInvoicesCBMTypeInvoiceList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportInvoicesCBMType_invoiceList of this ReportInvoicesCBMTypeInvoiceList.  # noqa: E501
        :rtype: ReportInvoicesCBMTypeInvoiceList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice_id(self) -> List[str]:
        """Gets the invoice_id of this ReportInvoicesCBMTypeInvoiceList.


        :return: The invoice_id of this ReportInvoicesCBMTypeInvoiceList.
        :rtype: List[str]
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id: List[str]):
        """Sets the invoice_id of this ReportInvoicesCBMTypeInvoiceList.


        :param invoice_id: The invoice_id of this ReportInvoicesCBMTypeInvoiceList.
        :type invoice_id: List[str]
        """

        self._invoice_id = invoice_id
