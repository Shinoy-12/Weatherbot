import pymongo

from pymongo import MongoClient

#Specify your host name with your port number
url= 'mongodb://localhost:27017'

#Authentication ur mongodb and specify your username along with your password
client = MongoClient(url ,username='shinoy',password='shinoy123')

#Name of your database
mydb = client["rasa"]

#Collection Name
coll = mydb["conversations"]

x = coll.find_one()
for z in x['events']:
    if (z['event']) == 'user':
        print(z['text'])
    elif (z['event']) == 'bot':
        print(z['text'])

## Conversation--
#hi
#Hey! Weather Bot here. What is ur name?
#my name is shinoy
#Shinoy which city weather you want to know?
#/get_weather{"current":"current"}
#Temp in your city is 18.06
#thank you
#Have a nice day
#/restart
#hy
#hello
#Hey! Weather Bot here. What is ur name?
#my name is shinoy
#Shinoy which city weather you want to know?
#/get_weather{"others":"other"}
#Select state
#jaipur
#Temp in your city is 25