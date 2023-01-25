import connexion
import six

from swagger_server.models.create_batch_cbm_type import CreateBatchCBMType  # noqa: E501
from swagger_server.models.create_batch_response_cbm_type import CreateBatchResponseCBMType  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.search_batch_response_cbm_type import SearchBatchResponseCBMType  # noqa: E501
from swagger_server import util


def create_batch(body=None):  # noqa: E501
    """Create Batch

    &lt;h3&gt;Purpose&lt;/h3&gt; To provide the consumer with the ability to create a batch in a single call.  &lt;h3&gt;Service Flow Description&lt;/h3&gt; &lt;p&gt;The Create Batch service logic is&lt;/p&gt; &lt;ul&gt;  &lt;li&gt;An API Consumer invokes a service providing a Batch Object   &lt;br/&gt;   &lt;br/&gt;  &lt;/li&gt;  &lt;li&gt;   &lt;strong&gt;Validate Batch Object Structure&lt;/strong&gt;: The Batch object is validated if it is schematically correct   &lt;ul&gt;    &lt;li&gt;If the validation fails, an      &lt;em&gt;HTTP 400 - Bad request error&lt;/em&gt; will be propagated to the caller along with an      &lt;a&gt;Error Information&lt;/a&gt; message :    &lt;/li&gt;   &lt;/ul&gt;   &lt;div class&#x3D;\&quot;table-wrap\&quot;&gt;    &lt;table class&#x3D;\&quot;relative-table wrapped confluenceTable\&quot; style&#x3D;\&quot;width: 43.2785%;\&quot;&gt;     &lt;colgroup&gt;      &lt;col style&#x3D;\&quot;width: 10.7612%;\&quot;/&gt;      &lt;col style&#x3D;\&quot;width: 21.3911%;\&quot;/&gt;      &lt;col style&#x3D;\&quot;width: 15.2231%;\&quot;/&gt;      &lt;col style&#x3D;\&quot;width: 3.80577%;\&quot;/&gt;      &lt;col style&#x3D;\&quot;width: 48.8189%;\&quot;/&gt;     &lt;/colgroup&gt;     &lt;thead&gt;      &lt;tr&gt;       &lt;th colspan&#x3D;\&quot;4\&quot; class&#x3D;\&quot;confluenceTh\&quot;&gt;        &lt;p&gt;Error Code&lt;/p&gt;       &lt;/th&gt;       &lt;th colspan&#x3D;\&quot;1\&quot; class&#x3D;\&quot;confluenceTh\&quot;&gt;        &lt;p&gt;Message&lt;/p&gt;       &lt;/th&gt;      &lt;/tr&gt;     &lt;/thead&gt;     &lt;tbody&gt;      &lt;tr&gt;       &lt;td colspan&#x3D;\&quot;4\&quot; class&#x3D;\&quot;confluenceTd\&quot;&gt;APICLM.BUS.ERROR.00001&lt;/td&gt;       &lt;td colspan&#x3D;\&quot;1\&quot; class&#x3D;\&quot;confluenceTd\&quot;&gt;Invalid object - Unsupported message type&lt;/td&gt;      &lt;/tr&gt;      &lt;tr&gt;       &lt;td colspan&#x3D;\&quot;4\&quot; class&#x3D;\&quot;confluenceTd\&quot;&gt;APICLM.BUS.ERROR.00010&lt;/td&gt;       &lt;td colspan&#x3D;\&quot;1\&quot; class&#x3D;\&quot;confluenceTd\&quot;&gt;Batch amount currency Id is missing&lt;/td&gt;      &lt;/tr&gt;     &lt;/tbody&gt;    &lt;/table&gt;   &lt;/div&gt;  &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt;  &lt;li&gt;   &lt;strong&gt;Payment Date Exist and Valid - Yes : &lt;/strong&gt;If payment Date is provided (eg non-empty) and is greater than Received Date then it will be used as the Batch payment date   &lt;br/&gt;   &lt;strong&gt;    &lt;br/&gt;   &lt;/strong&gt;  &lt;/li&gt;  &lt;li&gt;   &lt;strong&gt;Payment Date Exist and Valid - No : &lt;/strong&gt;If payment Date is not provided or is less than the Received date, then service    &lt;em&gt;BatchBAS.calculatePaymentDate&lt;/em&gt; will be called to calculate it   &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt;  &lt;li style&#x3D;\&quot;list-style-type: none;\&quot;&gt;   &lt;strong&gt;Create Batch&lt;/strong&gt;: The purpose of this step is to persist the Batch object in MedNeXt+DB    &lt;ul&gt;    &lt;li&gt;If Batch object is not persisted due to service exception,  an      &lt;em&gt;HTTP 200&lt;/em&gt; response will be propagated to the caller containing an      &lt;a&gt;Error Information&lt;/a&gt; message    &lt;/li&gt;   &lt;/ul&gt;  &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt;  &lt;li style&#x3D;\&quot;list-style-type: none;\&quot;&gt;   &lt;strong&gt;Create Batch Case : &lt;/strong&gt;The Batch business process (ProcessBatchCase) will be initiated . A new &amp;quot;Create Batch Human Task&amp;quot; will be created and assigned to the least busy user of &amp;quot;Batch Creator&amp;quot; role.    &lt;br/&gt;   &lt;ul&gt;    &lt;li&gt;The Case initiation will be performed asynchronously and will not block the actual service response &lt;/li&gt;   &lt;/ul&gt;  &lt;/li&gt;  &lt;li&gt;The service will reply with the created Batch object enriched by the new batch ID  &lt;/li&gt; &lt;/ul&gt; # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateBatchResponseCBMType
    """
    if connexion.request.is_json:
        body = CreateBatchCBMType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def search_batch(page_number, page_size, batch_id, external_batch__reference_id, submitted_type, submitted_by, payment_date, submission_method, received_date):  # noqa: E501
    """Search Batch

    &lt;h3&gt;Purpose&lt;/h3&gt; To retrieve a list of batches with their related information based on specific criteria.  &lt;h3&gt;Prerequisites&lt;/h3&gt;   &lt;ul&gt;     &lt;li&gt;At least one of the above search criteria must be provided in the service request to restrict the returned results. When no search criteria are provided, the service will respond back an error requesting at least one of the search criteria to be provided.&lt;/li&gt;       &lt;ul&gt;         &lt;li&gt;batchId : The batch unique id  &lt;/li&gt;         &lt;li&gt;submissionMethod : How the batch was created&lt;/li&gt;         &lt;li&gt;receivedDate : The batch received date &lt;/li&gt;         &lt;li&gt;paymentDate : The date the batch will be paid&lt;/li&gt;         &lt;li&gt;submittedType : Indicates whether the batch is submitted by a Provider or Insurance Company&lt;/li&gt;         &lt;li&gt;submittedBy : Provider or Insurance Company&lt;/li&gt;         &lt;li&gt;externalReferenceId : Batch External Reference&lt;/li&gt;                &lt;li&gt;pageNumber : pagination result set number&lt;/li&gt;                &lt;li&gt;pageSize : records in result&lt;/li&gt;                  &lt;/ul&gt;   &lt;/ul&gt;   &lt;h3&gt;Service Flow Description&lt;/h3&gt; &lt;p&gt;The Search Batch service logic is :&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;Service input is validated. At least one search parameter must be provided         &lt;ul&gt;             &lt;li&gt;If no parameter is provided , an &lt;em&gt;HTTP 400 - Bad request&lt;/em&gt; error will be propagated to the caller along with an Error Information message&lt;/li&gt;             &lt;li&gt;If pageSize is greater than the &lt;strong&gt;configured&lt;/strong&gt; maximum page size, an &lt;em&gt;HTTP 400 - Bad request&lt;/em&gt; error will be propagated to the caller along with an Error Information message&lt;/li&gt;             &lt;li&gt;If no pageSize or pageNumber is provided, the default pre-configured values will be applied &lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt;     &lt;li&gt;If the Batch Id is provided, any other search criteria will be ignored&lt;/li&gt;     &lt;li&gt;If no Batch Id is provided, the rest provided input criteria will used&lt;/li&gt;     &lt;li&gt;The result will be mapped to a list of Batch objects and will be returned as the service response&lt;em&gt;.&lt;/em&gt;&lt;/li&gt; &lt;/ul&gt; # noqa: E501

    :param page_number: Page Number
    :type page_number: int
    :param page_size: Page size
    :type page_size: int
    :param batch_id: The batch unique id
    :type batch_id: str
    :param external_batch__reference_id: Batch&#x27;s External Reference Id
    :type external_batch__reference_id: str
    :param submitted_type: Indicates whether the entity  is submitted by a Provider or Insurance Company 
    :type submitted_type: str
    :param submitted_by: Provider or Insurance Company unique id
    :type submitted_by: str
    :param payment_date: Payment Date
    :type payment_date: str
    :param submission_method: 
    :type submission_method: str
    :param received_date: Batch Received Date (DateTime)
    :type received_date: str

    :rtype: SearchBatchResponseCBMType
    """
    payment_date = util.deserialize_date(payment_date)
    received_date = util.deserialize_datetime(received_date)
    return 'do some magic!'
