# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.report_invoices_cbm_type import ReportInvoicesCBMType  # noqa: E501
from swagger_server.models.report_invoices_response_cbm_type import ReportInvoicesResponseCBMType  # noqa: E501
from swagger_server.models.search_invoice_report_response_cbm_type import SearchInvoiceReportResponseCBMType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInvoiceReportController(BaseTestCase):
    """InvoiceReportController integration test stubs"""

    def test_query_report_run_info_by_id(self):
        """Test case for query_report_run_info_by_id

        Search Report
        """
        query_string = [('run_number', 8)]
        response = self.client.open(
            '/mednext/claim/claim/invoice/report',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_report_invoices(self):
        """Test case for report_invoices

        Report Invoices
        """
        body = ReportInvoicesCBMType()
        response = self.client.open(
            '/mednext/claim/claim/invoice/report',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
