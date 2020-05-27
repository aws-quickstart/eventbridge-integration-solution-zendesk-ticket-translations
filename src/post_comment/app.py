import os
from zenpy import Zenpy #importing zenpy (https://github.com/facetoe/zenpy)
from zenpy.lib.api_objects import Comment


creds = {
    'email': os.environ['email'],
    'token': os.environ['token'],
    'subdomain': os.environ['subdomain']
}

zenpy_client = Zenpy(**creds)

def lambda_handler(event, context):

    ticket = zenpy_client.tickets(id=event['Input']['Ticket_Id'])
    
    og_lang = event['Input']['Original_Langugage']
    tolang = os.environ['TargetLanguage']
    new_lang = event['Input']['TranslatedText']
    
    ticket.comment = Comment(body=event['Input']['TranslatedText'], html_body='<h4>Translated by Amazon Translate from {} to {}</h4><p>{}</p>'.format(og_lang, tolang, new_lang), public=False)
    
    zenpy_client.tickets.update(ticket)