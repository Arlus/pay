# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import settings
import urllib
import urllib2
from django.utils import simplejson
import ast

headers = {
    "X-PAYPAL-SECURITY-USERID": "arlusishmael_api1.ymail.com",
    "X-PAYPAL-SECURITY-PASSWORD": "1378158935",
    "X-PAYPAL-SECURITY-SIGNATURE": "Al4U.YSVxBesXAKATYmzOhAsLzOwA9k6kc4p1fO8kXiWXKJkiAjZaatv",
    "X-PAYPAL-REQUEST-DATA-FORMAT": "JSON",
    "X-PAYPAL-RESPONSE-DATA-FORMAT": "JSON",
    "X-PAYPAL-APPLICATION-ID": "APP-80W284485P519543T",

}

#data = {"scope":"EXPRESS_CKECKOUT", "callback":"http://www.example.com/success.html", "requestEnvelope": {"errorLanguage":"en_US"}}

def home(request):
    headers = {
    "X-PAYPAL-SECURITY-USERID": settings.USERNAME,
    "X-PAYPAL-SECURITY-PASSWORD": settings.PASSWORD,
    "X-PAYPAL-SECURITY-SIGNATURE": settings.SIGNATURE,
    "X-PAYPAL-REQUEST-DATA-FORMAT": "JSON",
    "X-PAYPAL-RESPONSE-DATA-FORMAT": "JSON",
    "X-PAYPAL-APPLICATION-ID": "APP-80W284485P519543T"
}

    data = {"scope":"TRANSACTION_SEARCH", "callback":"http://www.example.com/success.html", "requestEnvelope": {"errorLanguage":"en_US"}}
    req = urllib2.Request("https://svcs.sandbox.paypal.com/Permissions/RequestPermissions/", simplejson.dumps(data), headers)    
    res = ast.literal_eval(urllib2.urlopen(req).read())
    token = res['token']
    red_url = "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_grant-permission&request_token=%s" % token
    if red_url:
        return HttpResponseRedirect(red_url)
    #token = "AAAAAAAYaraTSVjvkUBT"
    #verification = "DIXWn8uRbKKfz4iXdvx97A"
    #headers2 = {
    #"X-PAYPAL-SECURITY-USERID": settings.USERNAME,
    #"X-PAYPAL-SECURITY-PASSWORD": settings.PASSWORD,
    #"X-PAYPAL-SECURITY-SIGNATURE": settings.SIGNATURE,
    #"X-PAYPAL-REQUEST-DATA-FORMAT": "JSON",
    #"X-PAYPAL-RESPONSE-DATA-FORMAT": "JSON",
    #"X-PAYPAL-APPLICATION-ID": "APP-80W284485P519543T",
#}
    #url = "https://svcs.sandbox.paypal.com/Permissions/GetAccessToken/"
    #url = "https://svcs.sandbox.paypal.com/Permissions/GetAccessToken/"
    #print url
    #dat2 = {
    #    "requestEnvelope": {"errorLanguage":"en_US"}, 
    #    "token": "AAAAAAAYaraTSVjvkUBT", 
    #    "verifier": "DIXWn8uRbKKfz4iXdvx97A"}
    #req2 = urllib2.Request("https://svcs.sandbox.paypal.com/Permissions/GetAccessToken/", simplejson.dumps(dat2), headers2)
    #res2 = urllib2.urlopen(req2).read()    
    
    #return render_to_response("home.html", locals(), context_instance = RequestContext(request))

