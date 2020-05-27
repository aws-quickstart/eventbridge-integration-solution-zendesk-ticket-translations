import os
import json
from zenpy import Zenpy #importing zenpy (https://github.com/facetoe/zenpy)


creds = {
    'email': os.environ['email'],
    'token': os.environ['token'],
    'subdomain': os.environ['subdomain']
}

zenpy_client = Zenpy(**creds)

def lambda_handler(event, context):
    
    print(event)
    
    ticket_id = event['id']
    
    if  event['detail-type'] == "Support Ticket: Comment Created":
        
        if event['content']['comment']['author']['is_staff'] == False:
            
            comment = event['content']['comment']['body']
        
            print("ticket_id: {}".format(ticket_id))
            print("comment: {}".format(comment))
        
            return {
                
                'ticket_id': ticket_id,
                'comment': comment
            }
            
