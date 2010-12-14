#! /usr/bin/env python
'''
Created on 01-Feb-2010

@author: rohanbk
'''

import urllib
import time
import datetime
import sched
import os, sys


class twit: 
    def __init__(self,uname,pswd,filepath,run_time_hours,run_time_minutes,words):
        self.uname=uname
        self.password=pswd
        self.filepath=open(filepath,"a")
        now = datetime.datetime.now()
        current_hour= int(now.strftime("%H"))
        current_minutes=int(now.strftime("%M"))
        
        self.endtime_hour=((current_hour+run_time_hours)%24)
        self.endtime_minutes=((current_minutes+run_time_minutes)%60)
        self.current_hour=current_hour
        self.words=words
        
    def main(self):
        i=0
        output=self.filepath
        words=[]
        words=self.words.split(',')
        current_hour=self.current_hour
        #Grab every tweet using Streaming API
        with tweetstream.TrackStream(self.uname, self.password,words) as stream:
            for tweet in stream:
                if tweet.has_key("text"):
                    #Write tweet to file and print it to STDOUT
                    if tweet['geo'] is not None:
                        coordinates="%s,%s"%(tweet['geo']['coordinates'][0],tweet['geo']['coordinates'][1])
                    else:
						coordinates=None
                        
                        
                    source=tweet['source']
                    try:
                        soup=BeautifulSoup(source)
                        source=soup.a.contents[0]
                    except AttributeError:
                        pass
                    message="%s!~%s!~%s!~%s!~%s!~%s!~%s!~%s\n"%(tweet['user']['screen_name'],tweet['created_at'],tweet['user']['followers_count'],tweet['user']['friends_count'],coordinates,tweet['user']['time_zone'],tweet['source'],tweet['text'])
                    message=message.encode('utf-8')
                    print message
                    output.write(message)
                    i+=1
                    now = datetime.datetime.now()
                    if int(now.strftime("%H"))>=self.endtime_hour and int(now.strftime("%M"))>=self.endtime_minutes:
                        output.close()
                        break
                    if int(now.strftime("%H")) == current_hour+1:
                        current_hour+=1
            print "Total number of tweets: ",i
        
            
if __name__=='__main__':
    try:
        import tweetstream
        from BeautifulSoup import BeautifulSoup
    except ImportError, e:
        print 'You are missing or more of the following python packages:'
        print 'tweetstream'
        print 'Beautiful Soup'
        print 'All packages may be installed using Easy Install'
        sys.exit(0)
    sys.argv = raw_input('Enter command line arguments: ').split()
    if len(sys.argv)==5:
        uname=sys.argv[0]
        password=sys.argv[1]
        fname=sys.argv[2]
        runhour=sys.argv[3]
        runmin=sys.argv[4]
    else:
        print "Wrong number of arguments--> python SBtwit.py [twitter_username] [twitter_password] [output-filename] [runtime hours] [runtime minutes]"

    words=raw_input('Please enter the list of search words separated with commas (,):')
        
    try:
        t=twit(uname,password,fname,runhour,runmin,words)
        t.main()
    except KeyboardInterrupt:
        t.filepath.close()
        print "Goodbye\n"