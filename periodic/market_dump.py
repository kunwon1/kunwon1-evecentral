#import pylab
#import matplotlib

#import matplotlib.text
#import matplotlib.dates

import psycopg
import sys
from mx.DateTime import *
import datetime
import pickle
from numpy import *
sys.path.append('../lib/')

from evecentral import display

#import evec_func
db = psycopg.connect(database='evec', user='evec', host = 'localhost', port = '9999', serialize = 0)



#    Column    |	    Type	     |	     Modifiers
#--------------+-----------------------------+------------------------
#    regionid	  | bigint			| not null
#    systemid	  | bigint			| not null
#    stationid	  | bigint			| not null
#    typeid	  | bigint			| not null
#    bid	  | integer			| not null default 0
#    price	  | double precision		| not null
#    orderid	  | bigint			| not null
#    minvolume	  | integer			| not null
#    volremain	  | integer			| not null
#    volenter	  | integer			| not null
#    issued	  | date			| not null
#    duration	  | interval			| not null
#    range	  | integer			| not null
#    reportedby	  | bigint			| not null
#    reportedtime | timestamp without time zone | not null default now()


def write_dump(file,date):
    global db
    of = open(file, 'w')
    cur = db.cursor()
    cur.execute("SELECT orderid,regionid,systemid,stationid,typeid,bid,price,minvolume,volremain,volenter,issued,duration,range,reportedby,reportedtime FROM archive_market WHERE (reportedtime) > %s and (reportedtime) <= %s ", [date+" 00:00:00", date+" 23:59:59"])
    a = cur.fetchone()
    print >> of, "orderid, regionid, systemid, stationid, typeid, bid, price, minvolume, volremain, volenter, issued, duration, range, reportedby, reportedtime"
    record = 0
    while a:
	record += 1
	for x in a:
	    print >> of, x, ",",
	a = cur.fetchone()
	if record % 1000 == 0:
	    print record,
	print >> of
    print



def do_date(data):

    date = Date(2008,1,15)


    while date < now() - RelativeDateTime(days = 1):
	try:
	    if data[date] == True:
#		print "Skipping ",date.date
		date += RelativeDateTime(days=1)
		continue
	except:
	    pass

	print "Working on",date.date
	if date not in data.keys():
	    write_dump(date.date+".dump",date.date)
	    data[date] = True
	date += RelativeDateTime(days=1)




cur = db.cursor()



dumps_data = {}

try:
    f = open('dumps.pickle', 'r')
    dumps_data = pickle.load(f)
    f.close()
except:
    dumps_data = {}



do_date(dumps_data)

f = open('dumps.pickle', 'w')
pickle.dump(dumps_data, f)
f.close()

cur = db.cursor()
cur.execute("DELETE FROM archive_market WHERE reportedtime < NOW() - INTERVAL '1 month'")
cur.commit()
