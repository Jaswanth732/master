# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cancel_invoice_cbm_type import CancelInvoiceCBMType  # noqa: E501
from swagger_server.models.cancel_invoice_response_cbm_type import CancelInvoiceResponseCBMType  # noqa: E501
from swagger_server.models.correct_invoice_cbm_type import CorrectInvoiceCBMType  # noqa: E501
from swagger_server.models.create_invoice_cbm_type import CreateInvoiceCBMType  # noqa: E501
from swagger_server.models.create_invoice_response_cbm_type import CreateInvoiceResponseCBMType  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.search_invoice_response_cbm_type import SearchInvoiceResponseCBMType  # noqa: E501
from swagger_server.models.search_invoice_transaction_response_cbm_type import SearchInvoiceTransactionResponseCBMType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInvoiceController(BaseTestCase):
    """InvoiceController integration test stubs"""

    def test_cancel_invoice(self):
        """Test case for cancel_invoice

        Cancel Invoice
        """
        body = CancelInvoiceCBMType()
        response = self.client.open(
            '/mednext/claim/claim/invoice',
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_correct_invoice(self):
        """Test case for correct_invoice

        Correct Invoice
        """
        body = CorrectInvoiceCBMType()
        response = self.client.open(
            '/mednext/claim/claim/invoice',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_invoice(self):
        """Test case for create_invoice

        Create Invoice
        """
        body = CreateInvoiceCBMType()
        response = self.client.open(
            '/mednext/claim/claim/invoice',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_invoice(self):
        """Test case for search_invoice

        Search Invoice
        """
        query_string = [('page_number', 2),
                        ('page_size', 2),
                        ('invoice_id', 'invoice_id_example'),
                        ('batch_id', 'batch_id_example'),
                        ('policy_id', 8),
                        ('member_id', 8),
                        ('status', 'status_example'),
                        ('billing_provider', 'billing_provider_example'),
                        ('external_reference_id', 'external_reference_id_example'),
                        ('service_provider', 'service_provider_example')]
        response = self.client.open(
            '/mednext/claim/claim/invoice',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_searchinvoicetransaction(self):
        """Test case for searchinvoicetransaction

        Search Invoice Transaction
        """
        query_string = [('page_size', 2),
                        ('page_number', 2),
                        ('invoice_nbr', 'invoice_nbr_example'),
                        ('invoice_line_nbr', 'invoice_line_nbr_example')]
        response = self.client.open(
            '/mednext/claim/claim/invoicetransaction',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
