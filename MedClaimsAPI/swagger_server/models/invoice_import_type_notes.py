# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.invoice_import_note_type import InvoiceImportNoteType  # noqa: F401,E501
from swagger_server import util


class InvoiceImportTypeNotes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, note: List[InvoiceImportNoteType]=None):  # noqa: E501
        """InvoiceImportTypeNotes - a model defined in Swagger

        :param note: The note of this InvoiceImportTypeNotes.  # noqa: E501
        :type note: List[InvoiceImportNoteType]
        """
        self.swagger_types = {
            'note': List[InvoiceImportNoteType]
        }

        self.attribute_map = {
            'note': 'note'
        }
        self._note = note

    @classmethod
    def from_dict(cls, dikt) -> 'InvoiceImportTypeNotes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvoiceImportType_notes of this InvoiceImportTypeNotes.  # noqa: E501
        :rtype: InvoiceImportTypeNotes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def note(self) -> List[InvoiceImportNoteType]:
        """Gets the note of this InvoiceImportTypeNotes.


        :return: The note of this InvoiceImportTypeNotes.
        :rtype: List[InvoiceImportNoteType]
        """
        return self._note

    @note.setter
    def note(self, note: List[InvoiceImportNoteType]):
        """Sets the note of this InvoiceImportTypeNotes.


        :param note: The note of this InvoiceImportTypeNotes.
        :type note: List[InvoiceImportNoteType]
        """

        self._note = note
