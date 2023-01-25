import connexion
import six

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.report_invoices_cbm_type import ReportInvoicesCBMType  # noqa: E501
from swagger_server.models.report_invoices_response_cbm_type import ReportInvoicesResponseCBMType  # noqa: E501
from swagger_server.models.search_invoice_report_response_cbm_type import SearchInvoiceReportResponseCBMType  # noqa: E501
from swagger_server import util


def query_report_run_info_by_id(run_number):  # noqa: E501
    """Search Report

    &lt;h3&gt;Purpose&lt;/h3&gt; To retrieve a list of invoice report information with its related information based on specific criteria.  &lt;h3&gt;Prerequisites&lt;/h3&gt;   &lt;ul&gt;     &lt;li&gt;At least one of the above search criteria must be provided in the service request to restrict the returned results. When no search criteria are provided, the service will respond back an error requesting at least one of the search criteria to be provided.&lt;/li&gt;       &lt;ul&gt;         &lt;li&gt;runNumber : The invoice report unique run number&lt;/li&gt;       &lt;/ul&gt;   &lt;/ul&gt;  &lt;h3 &gt;Service Flow Description&lt;/h3&gt; &lt;p&gt;The Search Invoice Report service logic is :&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;Service input is validated. Report Run Number is mandatory         &lt;ul&gt;             &lt;li&gt;If no parameter is provided , an &lt;em&gt;HTTP 400 - Bad request&lt;/em&gt; error will be propagated to the caller along with an Error Information message&lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt;     &lt;li&gt;If the Report Run Number is is provided it will be used to retrieve the Invoice Report Object.         &lt;ul&gt;             &lt;li&gt;If no result is returned , an &lt;em&gt;HTTP 404 - Not Found &lt;/em&gt;error will be propagated to the caller along with an Error Information message&lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt;     &lt;li&gt;The result will be returned as the service response&lt;em&gt;.&lt;/em&gt;&lt;/li&gt; &lt;/ul&gt; # noqa: E501

    :param run_number: Report run number
    :type run_number: int

    :rtype: SearchInvoiceReportResponseCBMType
    """
    return 'do some magic!'


def report_invoices(body=None):  # noqa: E501
    """Report Invoices

    &lt;h3&gt;Purpose&lt;/h3&gt; To provide the consumer with the ability to report a list of invoices under the same batch or individually specified, in a single call.  &lt;h3&gt;Service Flow Description&lt;/h3&gt; &lt;p&gt;The Invoice Report service logic is&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;An API Consumer invokes a service providing an Batch Number or a List of Invoice unique Ids.         &lt;br/&gt;         &lt;br/&gt;     &lt;/li&gt;     &lt;li&gt;&lt;strong&gt;Validate Batch Object Structure&lt;/strong&gt;: The Input object is validated if it is schematically correct. One of Batch Id or List of Invoice Ids should be present. If none or both exists the input will be regarded as invalid         &lt;ul&gt;             &lt;li&gt;If the validation fails, an &lt;em&gt;HTTP 400 - Bad request error&lt;/em&gt; will be propagated to the caller along with an Error Information message&lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt;     &lt;li&gt;&lt;strong&gt;Validate Batch Invoices or Invoices List : &lt;/strong&gt;Depending on the input (Batch or Invoice List) a search is performed over the given set of invoices (Invoice List or Batch) . If at least one of the following criteria is true, then an &lt;em&gt;HTTP 400 - Bad request error&lt;/em&gt; will be propagated to the caller along with an Error Information message. The criteria are :         &lt;ul&gt;             &lt;li&gt;At least one invoice is found which is either Cancelled or a Pre-invoice is linked with an Authorisation&lt;/li&gt;             &lt;li&gt;At least one invoice is found with a running Invoice Process which is in status other than &amp;quot;Ready for Reporting&amp;quot;                 &lt;br/&gt;&lt;strong&gt;&lt;br/&gt;&lt;/strong&gt;&lt;/li&gt;         &lt;/ul&gt;     &lt;/li&gt;     &lt;li&gt;&lt;strong&gt;Create Queue Item :&lt;/strong&gt; A new Queue Item will be created to handle the asynchronous Invoice Report process.&lt;/li&gt; &lt;/ul&gt; &lt;ul&gt;     &lt;li&gt;The service will reply with &lt;em&gt;HTTP 202 - Accepted&lt;/em&gt; along with the created Queue Item object enriched by the new queue ID&lt;/li&gt; &lt;/ul&gt;  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ReportInvoicesResponseCBMType
    """
    if connexion.request.is_json:
        body = ReportInvoicesCBMType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
