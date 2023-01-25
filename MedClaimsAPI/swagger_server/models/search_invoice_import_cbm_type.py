# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.paging_type import PagingType  # noqa: F401,E501
from swagger_server import util


class SearchInvoiceImportCBMType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, paging: PagingType=None, import_id: str=None, batch_id: str=None, invoice_id: str=None, external_reference_id: str=None, import_status: str=None):  # noqa: E501
        """SearchInvoiceImportCBMType - a model defined in Swagger

        :param paging: The paging of this SearchInvoiceImportCBMType.  # noqa: E501
        :type paging: PagingType
        :param import_id: The import_id of this SearchInvoiceImportCBMType.  # noqa: E501
        :type import_id: str
        :param batch_id: The batch_id of this SearchInvoiceImportCBMType.  # noqa: E501
        :type batch_id: str
        :param invoice_id: The invoice_id of this SearchInvoiceImportCBMType.  # noqa: E501
        :type invoice_id: str
        :param external_reference_id: The external_reference_id of this SearchInvoiceImportCBMType.  # noqa: E501
        :type external_reference_id: str
        :param import_status: The import_status of this SearchInvoiceImportCBMType.  # noqa: E501
        :type import_status: str
        """
        self.swagger_types = {
            'paging': PagingType,
            'import_id': str,
            'batch_id': str,
            'invoice_id': str,
            'external_reference_id': str,
            'import_status': str
        }

        self.attribute_map = {
            'paging': 'paging',
            'import_id': 'importId',
            'batch_id': 'batchId',
            'invoice_id': 'invoiceId',
            'external_reference_id': 'externalReferenceId',
            'import_status': 'importStatus'
        }
        self._paging = paging
        self._import_id = import_id
        self._batch_id = batch_id
        self._invoice_id = invoice_id
        self._external_reference_id = external_reference_id
        self._import_status = import_status

    @classmethod
    def from_dict(cls, dikt) -> 'SearchInvoiceImportCBMType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SearchInvoiceImportCBMType of this SearchInvoiceImportCBMType.  # noqa: E501
        :rtype: SearchInvoiceImportCBMType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def paging(self) -> PagingType:
        """Gets the paging of this SearchInvoiceImportCBMType.


        :return: The paging of this SearchInvoiceImportCBMType.
        :rtype: PagingType
        """
        return self._paging

    @paging.setter
    def paging(self, paging: PagingType):
        """Sets the paging of this SearchInvoiceImportCBMType.


        :param paging: The paging of this SearchInvoiceImportCBMType.
        :type paging: PagingType
        """

        self._paging = paging

    @property
    def import_id(self) -> str:
        """Gets the import_id of this SearchInvoiceImportCBMType.


        :return: The import_id of this SearchInvoiceImportCBMType.
        :rtype: str
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id: str):
        """Sets the import_id of this SearchInvoiceImportCBMType.


        :param import_id: The import_id of this SearchInvoiceImportCBMType.
        :type import_id: str
        """

        self._import_id = import_id

    @property
    def batch_id(self) -> str:
        """Gets the batch_id of this SearchInvoiceImportCBMType.


        :return: The batch_id of this SearchInvoiceImportCBMType.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id: str):
        """Sets the batch_id of this SearchInvoiceImportCBMType.


        :param batch_id: The batch_id of this SearchInvoiceImportCBMType.
        :type batch_id: str
        """

        self._batch_id = batch_id

    @property
    def invoice_id(self) -> str:
        """Gets the invoice_id of this SearchInvoiceImportCBMType.


        :return: The invoice_id of this SearchInvoiceImportCBMType.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id: str):
        """Sets the invoice_id of this SearchInvoiceImportCBMType.


        :param invoice_id: The invoice_id of this SearchInvoiceImportCBMType.
        :type invoice_id: str
        """

        self._invoice_id = invoice_id

    @property
    def external_reference_id(self) -> str:
        """Gets the external_reference_id of this SearchInvoiceImportCBMType.


        :return: The external_reference_id of this SearchInvoiceImportCBMType.
        :rtype: str
        """
        return self._external_reference_id

    @external_reference_id.setter
    def external_reference_id(self, external_reference_id: str):
        """Sets the external_reference_id of this SearchInvoiceImportCBMType.


        :param external_reference_id: The external_reference_id of this SearchInvoiceImportCBMType.
        :type external_reference_id: str
        """

        self._external_reference_id = external_reference_id

    @property
    def import_status(self) -> str:
        """Gets the import_status of this SearchInvoiceImportCBMType.


        :return: The import_status of this SearchInvoiceImportCBMType.
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status: str):
        """Sets the import_status of this SearchInvoiceImportCBMType.


        :param import_status: The import_status of this SearchInvoiceImportCBMType.
        :type import_status: str
        """

        self._import_status = import_status
