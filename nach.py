#!C:/Users/Rithikshan/Documents/python

# Import modules for CGI handling 
# Import modules for CGI handling 
from flask import Flask
import requests
import cgi, cgitb 
import random
import json
import os
import hashlib
from datetime import datetime
import hmac
import binascii
import sys
import urllib.request
import urllib
from requests_html import HTMLSession
from urllib.parse import urljoin
from urllib.request import urlopen
from requests.exceptions import HTTPError
from json.decoder import JSONDecoder 
from json.encoder import JSONEncoder 
import webbrowser
import datetime
import string

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
ClientMECode=form.getvalue('ClientMECode')
ClientName  =form.getvalue('ClientName')
Email =form.getvalue('Email')
MobileNo  =form.getvalue('MobileNo')
Acname  =form.getvalue('AcHolderName')
Bank_Name=form.getvalue('Bank Name')
Branch_Name=form.getvalue('Branch Name')
Bank_Ac_Number=form.getvalue('Bank A/c Number')
Re_Enter_Ac_No=form.getvalue('Re-Enter A/cNo')
MICR=form.getvalue('MICR')
IFSC_CODE=form.getvalue('IFSC CODE')
Account_Type=form.getvalue('Account Type')
last=form.getvalue('Start')
#Start_Date= datetime.strptime(str(lastconnection), "%yyyy-%mm-%dd").strftime('%dd-%mm-%yyyy')
original_date = datetime.datetime.strptime(str(last), '%Y-%m-%d')
Start_Date = original_date.strftime("%d-%m-%Y")
End=form.getvalue('End Date')
original_date1 = datetime.datetime.strptime(End,'%Y-%m-%d')
End_Date = original_date1.strftime("%d-%m-%Y")
Max_Amount=form.getvalue('MaxAmount')
Frequency=form.getvalue('Frequency')
Frequency="MNTH"
x = "Hello"
y =""
f=bool(y)
t=bool(x)
ha="handleResponse"


var_configJson = {'tarCall': f,'features':{'showPGResponseMsg': t,'enableAbortResponse': t,'enableNewWindowFlow': t,'enableExpressPay':t,'siDetailsAtMerchantEnd':t,'enableSI':t},
                    'consumerData': {'deviceId': 'WEBSH2','token': 'd2d09dd43a6cf0d228637f99f1fc941a1be57af1d3105659ce783317abbc1fff359f0b931ff60228388188db363789e56663c1e47b5d4808ac691846a53b32d2','returnUrl': 'https://www.tekprocess.co.in/MerchantIntegrationClient/MerchantResponsePage.jsp', 
                    'responseHandler': ha,'paymentMode': 'netBanking','merchantLogoUrl': 'https://hooghlypay.com/NACHRegistration/loader.gif','merchantId': 'L656504','currency': 'INR',
                    'consumerId': 'c964634',  
                    'consumerMobileNo': '9876543210',
                    'consumerEmailId': 'test@test.com',
                    'txnId': '1634296000752',  
                    'items': [{'itemId': 'FIRST','amount':'1',
                    'comAmt': '0'}],'customStyle':{'PRIMARY_COLOR_CODE': '#45beaa','SECONDARY_COLOR_CODE': '#FFFFFF','BUTTON_COLOR_CODE_1': '#2d8c8c',  
                    'BUTTON_COLOR_CODE_2': '#FFFFFF'},'accountNo': '1234567890','accountHolderName': 'Name','ifscCode': 'ICIC0000001','accountType': 'Saving','debitStartDate': '10-03-2019','debitEndDate': '01-03-2047','maxAmount': '100','amountType': 'M','frequency': 'ADHO'}};


totalamount='1'
amountType="M"
cardNumber=""
expMonth=""
expYear=""
cvvCode=""



var_configJson['consumerData']['consumerMobileNo']=MobileNo
var_configJson['consumerData']['consumerEmailId']=Email

#var_configJson['consumerData']['items']=ini_dict
#[0]="FIRST"

#var_configJson['consumerData']['items'][1]='1'
#var_configJson['consumerData']['items'][2]="0"
var_configJson['consumerData']['accountNo']=Bank_Ac_Number
var_configJson['consumerData']['accountHolderName']=Acname
var_configJson['consumerData']['ifscCode']=IFSC_CODE
var_configJson['consumerData']['accountType']=Account_Type
var_configJson['consumerData']['debitStartDate']=Start_Date
var_configJson['consumerData']['debitEndDate']=End_Date
var_configJson['consumerData']['maxAmount']=Max_Amount
var_configJson['consumerData']['amountType']=amountType
var_configJson['consumerData']['frequency']=Frequency


txnId=random.randint(10000000,9999999999) 
consumerId="C"+str(random.randint(1000000,9999999999))
bi="L656504"  #MID
bi1=str(txnId)       #transaction id
bi2=str(totalamount)
bi3=str(Bank_Ac_Number)
bi4=str(consumerId)
bi5=str(MobileNo)
bi6=str(Email)
bi7=str(Start_Date)
bi8=str(End_Date)
bi9=str(Max_Amount)
bi11=str(Frequency)
bi16='2038314806HICWXI'
bala=bi+"|"+bi1+"|"+bi2+"|"+bi3+"|"+bi4+"|"+bi5+"|"+bi6+"|"+bi7+"|"+bi8+"|"+bi9+"|"+amountType+"|"+bi11+"|"+cardNumber+"|"+expMonth+"|"+expYear+"|"+cvvCode+"|"+bi16
#result = hashlib.sha512(bala.encode()).hexdigest()
result = (hashlib.sha512(bala.encode())).hexdigest()

#print (bala)
var_configJson['consumerData']['token']=result
var_configJson['consumerData']['txnId']=str(txnId)
var_configJson['consumerData']['consumerId']=consumerId

headers={'Content-type':'application/json','Accept':'application/json'}
#serializer = SnippetSerializer(var_configJson)

#payload = json.dumps(var_configJson,indent = 4)
#dataJSON = dumps(dataDictionary)

with open('data.json', 'w', encoding='utf-8') as f:
   json.dump(var_configJson, f, ensure_ascii=False, indent=4)

print("Content-type: text/html\r")
print("Location: http://localhost:8080/2nd.html\r\n\r")
#eval_res, tempfile = js2py.run_file("https://www.paynimo.com/paynimocheckout/server/lib/checkout.js")
#tempfile.configJson("payload")

#API_ENDPOINT="C:\xampp\htdocs\set.html"
#r = requests.post(url = API_ENDPOINT, data =payload,headers=headers)

"""



print("Location: http://python.org/\r\n\r")

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Welocome to the payment Page</title>")
print ("</head>")
print ("<body>")
#print ("localhost:8080/2nd.html")
#print (result)
#print (r5i)
print ("</body>")
print ("</html>")"""