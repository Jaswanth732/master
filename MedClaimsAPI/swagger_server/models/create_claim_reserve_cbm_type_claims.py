# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.claim_item_info_type import ClaimItemInfoType  # noqa: F401,E501
from swagger_server import util


class CreateClaimReserveCBMTypeClaims(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, claim: List[ClaimItemInfoType]=None):  # noqa: E501
        """CreateClaimReserveCBMTypeClaims - a model defined in Swagger

        :param claim: The claim of this CreateClaimReserveCBMTypeClaims.  # noqa: E501
        :type claim: List[ClaimItemInfoType]
        """
        self.swagger_types = {
            'claim': List[ClaimItemInfoType]
        }

        self.attribute_map = {
            'claim': 'claim'
        }
        self._claim = claim

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClaimReserveCBMTypeClaims':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClaimReserveCBMType_claims of this CreateClaimReserveCBMTypeClaims.  # noqa: E501
        :rtype: CreateClaimReserveCBMTypeClaims
        """
        return util.deserialize_model(dikt, cls)

    @property
    def claim(self) -> List[ClaimItemInfoType]:
        """Gets the claim of this CreateClaimReserveCBMTypeClaims.


        :return: The claim of this CreateClaimReserveCBMTypeClaims.
        :rtype: List[ClaimItemInfoType]
        """
        return self._claim

    @claim.setter
    def claim(self, claim: List[ClaimItemInfoType]):
        """Sets the claim of this CreateClaimReserveCBMTypeClaims.


        :param claim: The claim of this CreateClaimReserveCBMTypeClaims.
        :type claim: List[ClaimItemInfoType]
        """
        if claim is None:
            raise ValueError("Invalid value for `claim`, must not be `None`")  # noqa: E501

        self._claim = claim
