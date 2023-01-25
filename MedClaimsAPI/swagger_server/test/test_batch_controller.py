# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.create_batch_cbm_type import CreateBatchCBMType  # noqa: E501
from swagger_server.models.create_batch_response_cbm_type import CreateBatchResponseCBMType  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.search_batch_response_cbm_type import SearchBatchResponseCBMType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBatchController(BaseTestCase):
    """BatchController integration test stubs"""

    def test_create_batch(self):
        """Test case for create_batch

        Create Batch
        """
        body = CreateBatchCBMType()
        response = self.client.open(
            '/mednext/claim/claim/batch',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_batch(self):
        """Test case for search_batch

        Search Batch
        """
        query_string = [('page_number', 2),
                        ('page_size', 2),
                        ('batch_id', 'batch_id_example'),
                        ('external_batch__reference_id', 'external_batch__reference_id_example'),
                        ('submitted_type', 'submitted_type_example'),
                        ('submitted_by', 'submitted_by_example'),
                        ('payment_date', '2013-10-20'),
                        ('submission_method', 'submission_method_example'),
                        ('received_date', '2013-10-20T19:20:30+01:00')]
        response = self.client.open(
            '/mednext/claim/claim/batch',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
