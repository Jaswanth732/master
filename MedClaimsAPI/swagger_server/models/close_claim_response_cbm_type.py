# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.queue_item_type import QueueItemType  # noqa: F401,E501
from swagger_server import util


class CloseClaimResponseCBMType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, queue_item: QueueItemType=None):  # noqa: E501
        """CloseClaimResponseCBMType - a model defined in Swagger

        :param queue_item: The queue_item of this CloseClaimResponseCBMType.  # noqa: E501
        :type queue_item: QueueItemType
        """
        self.swagger_types = {
            'queue_item': QueueItemType
        }

        self.attribute_map = {
            'queue_item': 'queueItem'
        }
        self._queue_item = queue_item

    @classmethod
    def from_dict(cls, dikt) -> 'CloseClaimResponseCBMType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CloseClaimResponseCBMType of this CloseClaimResponseCBMType.  # noqa: E501
        :rtype: CloseClaimResponseCBMType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def queue_item(self) -> QueueItemType:
        """Gets the queue_item of this CloseClaimResponseCBMType.


        :return: The queue_item of this CloseClaimResponseCBMType.
        :rtype: QueueItemType
        """
        return self._queue_item

    @queue_item.setter
    def queue_item(self, queue_item: QueueItemType):
        """Sets the queue_item of this CloseClaimResponseCBMType.


        :param queue_item: The queue_item of this CloseClaimResponseCBMType.
        :type queue_item: QueueItemType
        """
        if queue_item is None:
            raise ValueError("Invalid value for `queue_item`, must not be `None`")  # noqa: E501

        self._queue_item = queue_item
