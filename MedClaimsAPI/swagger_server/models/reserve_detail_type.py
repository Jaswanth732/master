# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amount_type import AmountType  # noqa: F401,E501
from swagger_server import util


class ReserveDetailType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, reserve_nbr: int=None, level_id: int=None, level_value: int=None, amount: AmountType=None):  # noqa: E501
        """ReserveDetailType - a model defined in Swagger

        :param reserve_nbr: The reserve_nbr of this ReserveDetailType.  # noqa: E501
        :type reserve_nbr: int
        :param level_id: The level_id of this ReserveDetailType.  # noqa: E501
        :type level_id: int
        :param level_value: The level_value of this ReserveDetailType.  # noqa: E501
        :type level_value: int
        :param amount: The amount of this ReserveDetailType.  # noqa: E501
        :type amount: AmountType
        """
        self.swagger_types = {
            'reserve_nbr': int,
            'level_id': int,
            'level_value': int,
            'amount': AmountType
        }

        self.attribute_map = {
            'reserve_nbr': 'reserveNbr',
            'level_id': 'levelId',
            'level_value': 'levelValue',
            'amount': 'amount'
        }
        self._reserve_nbr = reserve_nbr
        self._level_id = level_id
        self._level_value = level_value
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'ReserveDetailType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReserveDetailType of this ReserveDetailType.  # noqa: E501
        :rtype: ReserveDetailType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reserve_nbr(self) -> int:
        """Gets the reserve_nbr of this ReserveDetailType.


        :return: The reserve_nbr of this ReserveDetailType.
        :rtype: int
        """
        return self._reserve_nbr

    @reserve_nbr.setter
    def reserve_nbr(self, reserve_nbr: int):
        """Sets the reserve_nbr of this ReserveDetailType.


        :param reserve_nbr: The reserve_nbr of this ReserveDetailType.
        :type reserve_nbr: int
        """

        self._reserve_nbr = reserve_nbr

    @property
    def level_id(self) -> int:
        """Gets the level_id of this ReserveDetailType.


        :return: The level_id of this ReserveDetailType.
        :rtype: int
        """
        return self._level_id

    @level_id.setter
    def level_id(self, level_id: int):
        """Sets the level_id of this ReserveDetailType.


        :param level_id: The level_id of this ReserveDetailType.
        :type level_id: int
        """

        self._level_id = level_id

    @property
    def level_value(self) -> int:
        """Gets the level_value of this ReserveDetailType.


        :return: The level_value of this ReserveDetailType.
        :rtype: int
        """
        return self._level_value

    @level_value.setter
    def level_value(self, level_value: int):
        """Sets the level_value of this ReserveDetailType.


        :param level_value: The level_value of this ReserveDetailType.
        :type level_value: int
        """
        if level_value is None:
            raise ValueError("Invalid value for `level_value`, must not be `None`")  # noqa: E501

        self._level_value = level_value

    @property
    def amount(self) -> AmountType:
        """Gets the amount of this ReserveDetailType.


        :return: The amount of this ReserveDetailType.
        :rtype: AmountType
        """
        return self._amount

    @amount.setter
    def amount(self, amount: AmountType):
        """Sets the amount of this ReserveDetailType.


        :param amount: The amount of this ReserveDetailType.
        :type amount: AmountType
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount
