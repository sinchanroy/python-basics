#! /usr/bin/env python 

import json 
import datetime
import sys 

number = int(sys.argv[1])

for i in range(number):
 sensor = 'sensor' + str(i)
 temperature = 100+int(i)
 message = (sensor + str(temperature) + str(datetime.datetime.utcnow()))
 json_message = json.dumps(message)
 print(json_message)


