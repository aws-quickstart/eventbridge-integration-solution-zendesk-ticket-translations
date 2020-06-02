import json
import boto3
import re
import os

client = boto3.client('translate')

def lambda_handler(event, context):
    
    print(event)
    
    comment = event['Input']['comment']
    edited_comment = re.sub(r'(.*?)\(.*?\)', '', comment)
    
    translation = client.translate_text(
        Text=edited_comment,
        SourceLanguageCode='auto',
        TargetLanguageCode=os.environ['target_language']
    )

    print(translation)
    
    TranslatedText = translation['TranslatedText']
    SourceLanguageCode = translation['SourceLanguageCode']
    Ticket_Id = event['Input']['ticket_id']
    TargetLanguageCode = translation['TargetLanguageCode']
    
    return {
        'Ticket_Id': Ticket_Id,
        'Original_Text': comment,
        'Original_Langugage': SourceLanguageCode,
        'To_Language': TargetLanguageCode,
        'TranslatedText': TranslatedText
    }
    

