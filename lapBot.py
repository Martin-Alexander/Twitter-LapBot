#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy
import time
import sys
 
argfile = str(sys.argv[1])

auth = tweepy.OAuthHandler("hZC2MFLNcQ8GDPAxv3TAX7FJE", "v2c0qZ9iPcPaamdf5T0I4ByZKjrP99hBTLEn9TW3wQja6afazn")
auth.set_access_token("820047544935911426-QxHX7aCIeBtOtvcZrIGsT1a5uW50ML2", "pTOdK8YyPRVE0nQCiu7ddttNECSyPjAi3cBfkH2ez8RsK")
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(10)
