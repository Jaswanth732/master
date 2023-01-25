# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.error_info_type import ErrorInfoType  # noqa: F401,E501
from swagger_server import util


class Error400InfoType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error: ErrorInfoType=None):  # noqa: E501
        """Error400InfoType - a model defined in Swagger

        :param error: The error of this Error400InfoType.  # noqa: E501
        :type error: ErrorInfoType
        """
        self.swagger_types = {
            'error': ErrorInfoType
        }

        self.attribute_map = {
            'error': 'error'
        }
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'Error400InfoType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error400InfoType of this Error400InfoType.  # noqa: E501
        :rtype: Error400InfoType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error(self) -> ErrorInfoType:
        """Gets the error of this Error400InfoType.


        :return: The error of this Error400InfoType.
        :rtype: ErrorInfoType
        """
        return self._error

    @error.setter
    def error(self, error: ErrorInfoType):
        """Sets the error of this Error400InfoType.


        :param error: The error of this Error400InfoType.
        :type error: ErrorInfoType
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error
