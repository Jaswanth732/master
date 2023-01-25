# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.adjust_claim_reserve_cbm_type import AdjustClaimReserveCBMType  # noqa: E501
from swagger_server.models.adjust_claim_reserve_response_cbm_type import AdjustClaimReserveResponseCBMType  # noqa: E501
from swagger_server.models.close_claim_cbm_type import CloseClaimCBMType  # noqa: E501
from swagger_server.models.close_claim_response_cbm_type import CloseClaimResponseCBMType  # noqa: E501
from swagger_server.models.create_claim_details_cbm_type import CreateClaimDetailsCBMType  # noqa: E501
from swagger_server.models.create_claim_reserve_cbm_type import CreateClaimReserveCBMType  # noqa: E501
from swagger_server.models.create_claim_reserve_response_cbm_type import CreateClaimReserveResponseCBMType  # noqa: E501
from swagger_server.models.inline_response202 import InlineResponse202  # noqa: E501
from swagger_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from swagger_server.models.reopen_claim_cbm_type import ReopenClaimCBMType  # noqa: E501
from swagger_server.models.reopen_claim_response_cbm_type import ReopenClaimResponseCBMType  # noqa: E501
from swagger_server.models.search_claim_cbm_type import SearchClaimCBMType  # noqa: E501
from swagger_server.models.search_claim_response_cbm_type import SearchClaimResponseCBMType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClaimController(BaseTestCase):
    """ClaimController integration test stubs"""

    def test_adjust_claim_reserve(self):
        """Test case for adjust_claim_reserve

        Adjust Claim Reserve
        """
        body = AdjustClaimReserveCBMType()
        response = self.client.open(
            '/mednext/claim/claim/reserve',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_close_claim(self):
        """Test case for close_claim

        Close Claim
        """
        body = CloseClaimCBMType()
        response = self.client.open(
            '/mednext/claim/claim/',
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_claim_reserve(self):
        """Test case for create_claim_reserve

        Create Claim Reserve
        """
        body = CreateClaimReserveCBMType()
        response = self.client.open(
            '/mednext/claim/claim/reserve',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_details(self):
        """Test case for create_details

        Create Claim
        """
        body = CreateClaimDetailsCBMType()
        response = self.client.open(
            '/mednext/claim/claim/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reopen_claim(self):
        """Test case for reopen_claim

        Reopen Claim
        """
        body = ReopenClaimCBMType()
        response = self.client.open(
            '/mednext/claim/claim/reopen',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_claim(self):
        """Test case for search_claim

        Search Claim
        """
        body = SearchClaimCBMType()
        response = self.client.open(
            '/mednext/claim/claim/search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
