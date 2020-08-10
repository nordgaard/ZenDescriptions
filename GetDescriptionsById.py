import requests
import json, csv
from pprint import pprint
import os

import sys
import re



# authorization = os.environ.get('AUTHORIZATION')

with open(r'Descriptions_8_10.csv', 'a+') as csvfile:

    fieldnames = ['id','description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    with open('ids.tsv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:

            id = row[0]
            line_count+=1
            PAYLOAD = {}

            url = "https://ouraringhelp.zendesk.com/api/v2/tickets/"
            # HEADERS = {
            #  'Authorization': authorization
            # }
            HEADERS = {
            # Pasted from postman
            }

            URL = url +str(id)
            print URL
            response = requests.request("GET", URL, json=PAYLOAD, headers=HEADERS)
            i=0
            for row in response.text.strip().splitlines():
               _parsed = json.loads(row)
               ticket_id = _parsed['ticket']['id']

               description = _parsed['ticket']['description'].encode("utf8")
               writer.writerow({'id':ticket_id,
                               'description':description})

               i+=1
