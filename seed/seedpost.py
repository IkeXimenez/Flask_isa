'''
Test project by Isaac Jimenez 1 09 2021
Stage 1 test seed script for POSTGRESQL database data loading 

Copy from seed.py extend to Seed PostgreSQL database using config.py to read database.ini
param files for connection

'''
import requests
import json
# import sqlite3
import psycopg2
from config import config

# Command line arguments
import getopt, sys

# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "t:"
 
# Long options
long_options = ["Total ="]

# Number of records to seed in the database, 150 by default
num_records = 150

#comand line management
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:

            if currentArgument.strip() in ("-t", "--Total") and currentValue.isdigit() :
                    num_records=int(currentValue)
            else :  
                print (" USAGE seed.py -t <Number of records> or seed.py --Total <Number of records>")
                sys.exit()
          
            print(currentArgument)            
            print(currentValue)
           

except getopt.error as err:
    # output error, and return with an error code
    print (str(err)," USAGE seed.py -t <Number of records> or seed.py --Total <Number of records>")
    sys.exit()

print("Number of records to seed PostgreSQL Database",num_records) 

# Calling the github Users API based in the number of records
# I configured the api call for 100 records per call
# I am using the parameter called since to continue with the records calling from the Next_id variable

# How many times I have to call the API based in number of records to seed
Calls_to_api = num_records / 100
if num_records % 100 > 0 : Calls_to_api = int(Calls_to_api) + 1

print("Calling the API ",Calls_to_api," Times")

# DataBase Management for postgreSQL

conn =None

params = config()

print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(**params)

#conn = sqlite3.connect('./database/github_users.db')
c = conn.cursor()
print("Opened database successfully")

# in PostGreSQL you must have created the GITHUB_USERS table first

c.execute(''' DELETE FROM public."GITHUB_USERS" ''')

# Try connect to web service

Next_id = 0

Pro_record = 1  # Number of proccesed records accounting 

for loop_num in range(int(Calls_to_api)):

    response = requests.get("https://api.github.com/users?per_page=100&since=" + str(Next_id))

    # Dump file like cache file for json loading
    with open("./seed/data_users_"+str(loop_num)+".json", "w") as users_file:
        json.dump(response.json(), users_file)

    with open("./seed/data_users_"+str(loop_num)+".json","r") as json_file:
        data = json.load(json_file)

    # Create loading file 
 
    
    for i in range(len(data)) :
        if Pro_record <= num_records :
           print(str(Pro_record),data[i]['id'],data[i]['login'],data[i]['avatar_url'],data[i]['type'],data[i]['url'])
           data_tuple = (str(Pro_record),str(data[i]['id']),data[i]['login'],data[i]['avatar_url'],data[i]['type'],data[i]['url'])

           c.execute('''  INSERT INTO public."GITHUB_USERS"
           ( "ID", "ID_USER", "USER_NAME", "AVATAR", "USER_TYPE", "URL")
	       VALUES (%s, %s, %s, %s, %s, %s) ''',data_tuple)


           Pro_record += 1
    conn.commit()    
    Next_id = data[i]['id']

    print("Next id = ",Next_id,"Processed Records =",str(Pro_record-1))

c.execute(''' SELECT count(*) FROM public."GITHUB_USERS" ''')
for row in c : 
    print("Number of records in DataBase = ",row[0])
#close the connection
conn.close()   
