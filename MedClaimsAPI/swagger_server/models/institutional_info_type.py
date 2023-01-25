# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InstitutionalInfoType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, invoice_date: datetime=None, service_date_from: datetime=None, service_date_to: datetime=None, claim_frequency_type_id: str=None, place_of_service_id: str=None, country_of_treatment_id: str=None):  # noqa: E501
        """InstitutionalInfoType - a model defined in Swagger

        :param invoice_date: The invoice_date of this InstitutionalInfoType.  # noqa: E501
        :type invoice_date: datetime
        :param service_date_from: The service_date_from of this InstitutionalInfoType.  # noqa: E501
        :type service_date_from: datetime
        :param service_date_to: The service_date_to of this InstitutionalInfoType.  # noqa: E501
        :type service_date_to: datetime
        :param claim_frequency_type_id: The claim_frequency_type_id of this InstitutionalInfoType.  # noqa: E501
        :type claim_frequency_type_id: str
        :param place_of_service_id: The place_of_service_id of this InstitutionalInfoType.  # noqa: E501
        :type place_of_service_id: str
        :param country_of_treatment_id: The country_of_treatment_id of this InstitutionalInfoType.  # noqa: E501
        :type country_of_treatment_id: str
        """
        self.swagger_types = {
            'invoice_date': datetime,
            'service_date_from': datetime,
            'service_date_to': datetime,
            'claim_frequency_type_id': str,
            'place_of_service_id': str,
            'country_of_treatment_id': str
        }

        self.attribute_map = {
            'invoice_date': 'invoiceDate',
            'service_date_from': 'serviceDateFrom',
            'service_date_to': 'serviceDateTo',
            'claim_frequency_type_id': 'claimFrequencyTypeId',
            'place_of_service_id': 'placeOfServiceId',
            'country_of_treatment_id': 'countryOfTreatmentId'
        }
        self._invoice_date = invoice_date
        self._service_date_from = service_date_from
        self._service_date_to = service_date_to
        self._claim_frequency_type_id = claim_frequency_type_id
        self._place_of_service_id = place_of_service_id
        self._country_of_treatment_id = country_of_treatment_id

    @classmethod
    def from_dict(cls, dikt) -> 'InstitutionalInfoType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InstitutionalInfoType of this InstitutionalInfoType.  # noqa: E501
        :rtype: InstitutionalInfoType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice_date(self) -> datetime:
        """Gets the invoice_date of this InstitutionalInfoType.


        :return: The invoice_date of this InstitutionalInfoType.
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date: datetime):
        """Sets the invoice_date of this InstitutionalInfoType.


        :param invoice_date: The invoice_date of this InstitutionalInfoType.
        :type invoice_date: datetime
        """
        if invoice_date is None:
            raise ValueError("Invalid value for `invoice_date`, must not be `None`")  # noqa: E501

        self._invoice_date = invoice_date

    @property
    def service_date_from(self) -> datetime:
        """Gets the service_date_from of this InstitutionalInfoType.


        :return: The service_date_from of this InstitutionalInfoType.
        :rtype: datetime
        """
        return self._service_date_from

    @service_date_from.setter
    def service_date_from(self, service_date_from: datetime):
        """Sets the service_date_from of this InstitutionalInfoType.


        :param service_date_from: The service_date_from of this InstitutionalInfoType.
        :type service_date_from: datetime
        """

        self._service_date_from = service_date_from

    @property
    def service_date_to(self) -> datetime:
        """Gets the service_date_to of this InstitutionalInfoType.


        :return: The service_date_to of this InstitutionalInfoType.
        :rtype: datetime
        """
        return self._service_date_to

    @service_date_to.setter
    def service_date_to(self, service_date_to: datetime):
        """Sets the service_date_to of this InstitutionalInfoType.


        :param service_date_to: The service_date_to of this InstitutionalInfoType.
        :type service_date_to: datetime
        """

        self._service_date_to = service_date_to

    @property
    def claim_frequency_type_id(self) -> str:
        """Gets the claim_frequency_type_id of this InstitutionalInfoType.


        :return: The claim_frequency_type_id of this InstitutionalInfoType.
        :rtype: str
        """
        return self._claim_frequency_type_id

    @claim_frequency_type_id.setter
    def claim_frequency_type_id(self, claim_frequency_type_id: str):
        """Sets the claim_frequency_type_id of this InstitutionalInfoType.


        :param claim_frequency_type_id: The claim_frequency_type_id of this InstitutionalInfoType.
        :type claim_frequency_type_id: str
        """

        self._claim_frequency_type_id = claim_frequency_type_id

    @property
    def place_of_service_id(self) -> str:
        """Gets the place_of_service_id of this InstitutionalInfoType.


        :return: The place_of_service_id of this InstitutionalInfoType.
        :rtype: str
        """
        return self._place_of_service_id

    @place_of_service_id.setter
    def place_of_service_id(self, place_of_service_id: str):
        """Sets the place_of_service_id of this InstitutionalInfoType.


        :param place_of_service_id: The place_of_service_id of this InstitutionalInfoType.
        :type place_of_service_id: str
        """

        self._place_of_service_id = place_of_service_id

    @property
    def country_of_treatment_id(self) -> str:
        """Gets the country_of_treatment_id of this InstitutionalInfoType.


        :return: The country_of_treatment_id of this InstitutionalInfoType.
        :rtype: str
        """
        return self._country_of_treatment_id

    @country_of_treatment_id.setter
    def country_of_treatment_id(self, country_of_treatment_id: str):
        """Sets the country_of_treatment_id of this InstitutionalInfoType.


        :param country_of_treatment_id: The country_of_treatment_id of this InstitutionalInfoType.
        :type country_of_treatment_id: str
        """

        self._country_of_treatment_id = country_of_treatment_id
