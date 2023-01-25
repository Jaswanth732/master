# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.claim_type import ClaimType  # noqa: F401,E501
from swagger_server import util


class UpdateClaimResponseCBMType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, claim: ClaimType=None):  # noqa: E501
        """UpdateClaimResponseCBMType - a model defined in Swagger

        :param claim: The claim of this UpdateClaimResponseCBMType.  # noqa: E501
        :type claim: ClaimType
        """
        self.swagger_types = {
            'claim': ClaimType
        }

        self.attribute_map = {
            'claim': 'claim'
        }
        self._claim = claim

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateClaimResponseCBMType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateClaimResponseCBMType of this UpdateClaimResponseCBMType.  # noqa: E501
        :rtype: UpdateClaimResponseCBMType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def claim(self) -> ClaimType:
        """Gets the claim of this UpdateClaimResponseCBMType.


        :return: The claim of this UpdateClaimResponseCBMType.
        :rtype: ClaimType
        """
        return self._claim

    @claim.setter
    def claim(self, claim: ClaimType):
        """Sets the claim of this UpdateClaimResponseCBMType.


        :param claim: The claim of this UpdateClaimResponseCBMType.
        :type claim: ClaimType
        """
        if claim is None:
            raise ValueError("Invalid value for `claim`, must not be `None`")  # noqa: E501

        self._claim = claim
