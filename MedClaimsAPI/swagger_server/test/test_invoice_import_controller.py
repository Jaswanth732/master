# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_invoice_import_cbm_type import CreateInvoiceImportCBMType  # noqa: E501
from swagger_server.models.create_invoice_import_response_cbm_type import CreateInvoiceImportResponseCBMType  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.search_invoice_import_response_cbm_type import SearchInvoiceImportResponseCBMType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInvoiceImportController(BaseTestCase):
    """InvoiceImportController integration test stubs"""

    def test_invoice_import(self):
        """Test case for invoice_import

        Invoice Import
        """
        body = CreateInvoiceImportCBMType()
        response = self.client.open(
            '/mednext/claim/claim/invoice/import',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_invoice_import(self):
        """Test case for search_invoice_import

        Search InvoiceImport
        """
        query_string = [('page_number', 2),
                        ('page_size', 2),
                        ('import_id', 'import_id_example'),
                        ('batch_id', 'batch_id_example'),
                        ('invoice_id', 'invoice_id_example'),
                        ('external_reference_id', 'external_reference_id_example')]
        response = self.client.open(
            '/mednext/claim/claim/invoice/import',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
