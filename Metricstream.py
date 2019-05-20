import requests
import xml.etree.ElementTree as ET
from xml.sax.saxutils import unescape
import pprint

class Metricstream:

	def get_exception_details(self,from_date,to_date,status=''):
	#function to get the exception details from Metricstream SOAP API.
	#params:
	#from_date - string DD-MON-YYYY (eg. 06-JUN-2018)
	#to_date - string DD-MON-YYYY (eg. 06-JUN-2018)
	#status - string (optional parameter), possible values are as follows:
	#'CS Approved'
	#'CS Approved (BU Head Pending)'
	#'CSCT Rejected'
	#'ETAT Rejected'
	#'IRM Rejected'
	#'Pending with CSCT'
	#'Pending with ETAT'
	#'Pending with IRM'
	#'Pending with Requestor - IRM Clarification'
	#'Pending with Requestor - CSCT Clarification'
	#'Pending with Requestor - ETAT Clarification'
	#'Queued with Cyber'
	#'Queued with IRM'
	#'Resolved  by NSS'
	#'Revoked'

	
	
		url="http://CSCHDV-MSAPP001:8090/Exception_Api/services/Exception_api?wsdl"
		headers={
					'content-type':'text/xml',
					'SOAPAction':''			
				}

		data="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
					<soapenv:Header></soapenv:Header>
						<soapenv:Body>
							<exceptionDetails>
								<Status>"""+status+"""</Status>
								<Request_from_date>"""+from_date+"""</Request_from_date>
								<Request_to_date>"""+to_date+"""</Request_to_date>
							</exceptionDetails>
						</soapenv:Body>
				</soapenv:Envelope>"""

		response=requests.post(url,data,headers=headers)
		if response.status_code==200:
			try:
				#declaring list to hold the exception details
				exception_details_list=[]
				
				#response.content contains required xml with escape characters
				raw_xml_string=response.content
				
				#replacing escape characters using unescape method from xml.sax.saxutils
				processed_xml_string=unescape(raw_xml_string)
				
				#getting Element by parsing the xml from string
				parsed_xml_element=ET.fromstring(processed_xml_string)
				
				#getting the 'Exception' element which contains exception details
				for exception_xml_element in parsed_xml_element.iter('Exception'):
					#extracting exception details from 'Exception' element
					for child in exception_xml_element.iter('Exception_Details'):
						tree=ET.ElementTree(child)
						root=tree.getroot()
						exception_dict={}
						for item in root:
							exception_dict.update({item.tag:item.text})
						exception_details_list.append(exception_dict)
						
				return exception_details_list
			except:
				return False
		else:
			return False
			
#Code for testing
"""			
output_with_status=Metricstream().get_exception_details('04-JUN-2018','10-DEC-2018','CS Approved')		
pprint.pprint(output_with_status)
output_without_status=Metricstream().get_exception_details('04-JUN-2018','10-DEC-2018')
pprint.pprint(output_without_status)
print 'output_with_status : ', len(output_with_status)
print 'output_without_status : ', len(output_without_status)"""