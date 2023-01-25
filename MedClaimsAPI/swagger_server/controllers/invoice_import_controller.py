import connexion
import six

from swagger_server.models.create_invoice_import_cbm_type import CreateInvoiceImportCBMType  # noqa: E501
from swagger_server.models.create_invoice_import_response_cbm_type import CreateInvoiceImportResponseCBMType  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.search_invoice_import_response_cbm_type import SearchInvoiceImportResponseCBMType  # noqa: E501
from swagger_server import util


def invoice_import(body=None):  # noqa: E501
    """Invoice Import

    &lt;h3&gt;Purpose&lt;/h3&gt; To provide the consumer the ability to create one or more invoices in MedNeXt with an XML file following the structure and functionality as per MedNeXt import process.  &lt;h3&gt;Service Flow Description&lt;/h3&gt; &lt;p&gt;The Invoice Import service logic is&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;An API Consumer invokes a service providing an Batch Number or a List of Invoice unique Ids.         &lt;br/&gt;         &lt;br/&gt;     &lt;/li&gt;     &lt;li&gt;&lt;strong&gt;Validate Invoice Import Message Structure&lt;/strong&gt;: The Input object is validated if it is schematically correct. At least a non empty Import file must be provided         &lt;ul&gt;             &lt;li&gt;If the validation fails, an &lt;em&gt;HTTP 400 - Bad request error&lt;/em&gt; will be propagated to the caller along with an Error Information message&lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;     &lt;br/&gt; &lt;/p&gt; &lt;ul&gt;     &lt;li&gt;&lt;strong&gt;Create Queue Item :&lt;/strong&gt; A new Queue Item will be created to handle the asynchronous Invoice Import process. Service &lt;em&gt;QueueAPIServices.create &lt;/em&gt;will be used and will reply with a Queue Item         &lt;br/&gt;         &lt;br/&gt;     &lt;/li&gt;     &lt;li&gt;&lt;strong&gt;Copy File in Predefined Folder : &lt;/strong&gt;The file will be copied in a predefined and configurable folder used by MedNeXt+ product. Prior to transferring the file to the folder, it will be renamed and prefixed as API_&amp;lt;queueID&amp;gt;_&amp;lt;existing file name&amp;gt;. The existing MedNeXt+ ProcessInvoiceImportCase ACM Process will be initiated as a result of the file processing         &lt;br/&gt;         &lt;br/&gt;     &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt;     &lt;li&gt;The service will reply with &lt;em&gt;HTTP 202 - Accepted&lt;/em&gt; along with the created Queue Item object enriched by the new queue ID&lt;/li&gt; &lt;/ul&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateInvoiceImportResponseCBMType
    """
    if connexion.request.is_json:
        body = CreateInvoiceImportCBMType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def search_invoice_import(page_number, page_size, import_id, batch_id, invoice_id, external_reference_id):  # noqa: E501
    """Search InvoiceImport

    &lt;h3&gt;Purpose&lt;/h3&gt; To retrieve a list of invoice import information with its related information based on specific criteria.  &lt;h3&gt;Prerequisites&lt;/h3&gt;   &lt;ul&gt;     &lt;li&gt;At least one of the above search criteria must be provided in the service request to restrict the returned results. When no search criteria are provided, the service will respond back an error requesting at least one of the search criteria to be provided.&lt;/li&gt;       &lt;ul&gt;         &lt;li&gt;importId : The invoice import id &lt;/li&gt;         &lt;li&gt;batchId : The batch unique id &lt;/li&gt;     &lt;li&gt;invoiceId  : The invoice id&lt;/li&gt;         &lt;li&gt;externalReferenceId : The invoice external reference id &lt;/li&gt;     &lt;li&gt;pageNumber : pagination result set number&lt;/li&gt;                &lt;li&gt;pageSize : records in result&lt;/li&gt;                  &lt;/ul&gt;   &lt;/ul&gt;  &lt;h3&gt;&lt;br/&gt;Service Flow Description&lt;/h3&gt; &lt;p&gt;The Search Invoice Import service logic is :&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;Service input is validated. At least one search parameter must be provided         &lt;ul&gt;             &lt;li&gt;If no parameter is provided , an &lt;em&gt;HTTP 400 - Bad request&lt;/em&gt; error will be propagated to the caller along with an Error Information message&lt;/li&gt;             &lt;li&gt;If pageSize is greater than the &lt;strong&gt;configured&lt;/strong&gt; maximum page size, an &lt;em&gt;HTTP 400 - Bad request&lt;/em&gt; error will be propagated to the caller along with an Error Information message&lt;/li&gt;             &lt;li&gt;If no pageSize or pageNumber is provided, the default pre-configured values will be applied &lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt;     &lt;li&gt;If the Invoice Import Id is provided, any other search criteria will be ignored&lt;/li&gt;     &lt;li&gt;If no Invoice Import Id is provided, the rest input criteria will be used&lt;/li&gt;     &lt;li&gt;The result will be mapped to a list of Invoice Import objects and will be returned as the service response.&lt;/li&gt; &lt;/ul&gt; # noqa: E501

    :param page_number: Page Number
    :type page_number: int
    :param page_size: Page size
    :type page_size: int
    :param import_id: The import unique id
    :type import_id: str
    :param batch_id: The batch unique id
    :type batch_id: str
    :param invoice_id: Invoice unique id
    :type invoice_id: str
    :param external_reference_id: The entity external reference id 
    :type external_reference_id: str

    :rtype: SearchInvoiceImportResponseCBMType
    """
    return 'do some magic!'
