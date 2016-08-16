import sys #For command line arguments
import os.path #For managing files
from urllib import urlopen #For opening URLs
from twilio.rest import TwilioRestClient #For sending sms using twilio
from bs4 import BeautifulSoup #For getting raw text from html


USN = sys.argv[1] #VTU University Seat Number
accountSID = sys.argv[2] #Account SID for Twilio
authToken = sys.argv[3] #Auth Token for Twilio
twilioNum = sys.argv[4] #Your Twilio Phone Number
toNum = sys.argv[5] #To Phone Number

URL = "http://results.vtu.ac.in/?submit=1&rid={}".format(USN)    
webpage = urlopen(URL)   

#convert the webpage to html text
html = BeautifulSoup(webpage,"html.parser")

#convert the html to required string
raw = html.getText()

#check if flag file exists, if exists then sms is already send so exit script
if os.path.isfile('flagfile') == False:
	
	if raw.find("Results are not yet available") >= 0: #Results are not declared yet
		print("Results are not declared yet")
	
	elif raw.find("Total Marks") >= 0: #Results are declared
		print("Results are declared")
		trc = TwilioRestClient(accountSID, authToken)
		message = trc.messages.create(body="Results Are Declared visit : http://results.vtu.ac.in/?submit=1&rid={}".format(USN),to=toNum,from_=twilioNum)
		open('flagfile','w')
	
	else:
		print("Couldnt fetch data") #Error From VTU Website

else:
	print("Job Done") #flagfile exists and no need to check if results have been declared