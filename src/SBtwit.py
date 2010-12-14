#! /usr/bin/env python
'''
Created on 01-Feb-2010

@author: rohanbk
'''
import tweetstream
import simplejson
import urllib
import time
import datetime
import sched
import os, sys
from BeautifulSoup import BeautifulSoup

class twit: 
    def __init__(self,uname,pswd,filepath,run_time_hours,run_time_minutes):
        self.uname=uname
        self.password=pswd
        self.filepath=open(filepath,"a")
        now = datetime.datetime.now()
        current_hour= int(now.strftime("%H"))
        current_minutes=int(now.strftime("%M"))
        
        self.endtime_hour=((current_hour+run_time_hours)%24)
        self.endtime_minutes=((current_minutes+run_time_minutes)%60)
        self.current_hour=current_hour
        
    def main(self):
        i=0
        output=self.filepath
        words=[]
        words=["Super Bowl","Colts","Saints"]
        tph=open("sbtweetsph.txt","a")
        current_hour=self.current_hour
        #Grab every tweet using Streaming API
        with tweetstream.TrackStream(self.uname, self.password,words) as stream:
#            s.enter(10, 1, t.timestamp, (s,))
#            s.run()
            for tweet in stream:
                if tweet.has_key("text"):
                    #Write tweet to file and print it to STDOUT
                    if tweet['geo'] is not None:
                        coordinates="%s,%s"%(tweet['geo']['coordinates'][0],tweet['geo']['coordinates'][1])
                        try:
                            soup=BeautifulSoup(source)
                            source=soup.a.contents[0]
                        except AttributeError:
                            pass
                        message=message.encode('utf-8')
                    
                    else:
						coordinates=None
                        
                        try:
                            soup=BeautifulSoup(source)
                            source=soup.a.contents[0]
                        except AttributeError:
                            pass

						
                        
					message="%s!~%s!~%s!~%s!~%s!~%s!~%s!~%s\n"%(tweet['user']['screen_name'],tweet['created_at'],tweet['user']['followers_count'],tweet['user']['friends_count'],coordinates,tweet['user']['time_zone'],tweet['source'],tweet['text'])
					print message
                    output.write(message)
                    i+=1
                    now = datetime.datetime.now()
                    if int(now.strftime("%H"))>=self.endtime_hour and int(now.strftime("%M"))>=self.endtime_minutes:
                        output.close()
                        break
                    if int(now.strftime("%H")) == current_hour+1:
                        tph.write("%s - %s"%(current_hour,i))
                        current_hour+=1
            print "Total number of tweets: ",i
        
            
if __name__=='__main__':
	if len(argv)!=5:
		print "Wrong number of arguments--> python SBtwit.py [twitter_username] [twitter_password] [output-filename] [runtime hours] [runtime minutes]"
	else:
		uname=argv[0]
		password=argv[1]
		fname=argv[2]
		runhour=argv[3]
		runmin=argv[4]
	
	
    try:
        t=twit(uname,password,fname,runhour,runmin)
        t.main()
    except KeyboardInterrupt:
        t.filepath.close()
        print "Goodbye\n"