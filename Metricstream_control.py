from Metricstream import *
from datetime import datetime as DT
from flask import jsonify

class Metricstream_control:

	def get_exception_details(self,from_date,to_date,status=''):
		#function to get the exception details
		
		if len(from_date)>0 and len(to_date)>0:
			if self.validdate(from_date):
				if self.validdate(to_date):
					#converting dates from DD-MM-YYYY to DD-MMM-YYYY
					date1=DT.strptime(from_date,'%d-%m-%Y')
					from_date=date1.strftime('%d-%b-%Y')
					date2=DT.strptime(to_date,'%d-%m-%Y')
					to_date=date2.strftime('%d-%b-%Y')
				
					if from_date<to_date:
						api_response=Metricstream().get_exception_details(from_date,to_date,status)
						if api_response!=False:
							"""exception_details=[]
							for item in api_response:
								exception=[
											item['MS_TICKET_ID'],
											item['REQUESTOR_USER_ID'],
											item['REQUESTOR_NAME'],
											item['PROJECT_NAME'],
											item['REQUEST_RAISED_ON'],
											item['ITEM'],
											item['STATUS'],
											item['DD_MODIFIED_ON'],
											item['EXCEPTION_VALID_TILL'],
											item['REQUEST_SUMMARY']
					
											]
								exception_details.append(exception)
							return jsonify({'pdf1':'Success','pdf2':exception_details})"""
							return jsonify({'pdf1':'Success','pdf2':api_response)	
						else:
							print "Data could not be fetched!!"
							return jsonify({'pdf1':'Failure','pdf2':'Data could not be fetched!!')
					
					else:
						print "From date cannot be later than To date!!"
						return jsonify({'pdf1':'Failure','pdf2':'From date cannot be later than To date!!')
				else:
					print "Please enter To date in DD-MM-YYYY format!!"
					return jsonify({'pdf1':'Failure','pdf2':'Please enter To date in DD-MM-YYYY format!!')
				
			else:
				print "Please enter From date in DD-MM-YYYY format!!"
				return jsonify({'pdf1':'Failure','pdf2':'Please enter From date in DD-MM-YYYY format!!')
				
		elif len(from_date)>0 and len(to_date)==0:
			print "Please enter To date!!"
			return jsonify({'pdf1':'Failure','pdf2':'Please enter To date!!')
		elif len(to_date)>0 and len(from_date)==0:
			print "Please enter From date!!"
			return jsonify({'pdf1':'Failure','pdf2':'Please enter From date!!')
		else:
			print "Please enter From date and To date!!"
			return jsonify({'pdf1':'Failure','pdf2':'Please enter From date and To date!!')
	
	def validdate(self,date_str):
		if date_str.count('-')==2:
			try:
				datetime.strptime(date_str,'%Y-%m-%d')
				return True
			except:
				return False
		else:
			return False