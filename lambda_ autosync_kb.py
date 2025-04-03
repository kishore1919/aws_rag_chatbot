"""
AWS Lambda function to trigger the ingestion job for a knowledge base
This function uses the Bedrock Agent Runtime to start an ingestion job for a specified knowledge base.
It takes the knowledge base ID and data source ID from environment variables and starts the ingestion job using the Bedrock Agent Runtime. 
If the required environment variables 'KNOWLEDGEBASEID' or 'DATASOURCEID' are missing, the function raises a ValueError with an appropriate error message.
The function is triggered by an event, which contains the user prompt, and returns a response with the generated text.
Configure the Lambda function with the necessary environment variables.
Make sure to set the environment variables KNOWLEDGEBASEID and DATASOURCEID in the Lambda function configuration.
# This function is designed to be deployed on AWS Lambda, and it requires the following environment variables to be set:
- KNOWLEDGEBASEID: The ID of the knowledge base to be used for retrieval.
- DATASOURCEID: The ID of the data source to be used for ingestion. 
"""
import os
import json
import boto3


bedrockClient = boto3.client('bedrock-agent')

def lambda_handler(event, context):
    print('Inside Lambda Handler')
    print('event: ', event)
    dataSourceId = os.environ.get('DATASOURCEID')
    knowledgeBaseId = os.environ.get('KNOWLEDGEBASEID')

    if not dataSourceId or not knowledgeBaseId:
        raise ValueError("Environment variables 'DATASOURCEID' and 'KNOWLEDGEBASEID' must be set.")
    
    print('knowledgeBaseId: ', knowledgeBaseId)
    print('dataSourceId: ', dataSourceId)

    # Verify the method and parameters for the bedrock-agent client
    try:
        response = bedrockClient.start_ingestion_job(
            knowledgeBaseId=knowledgeBaseId,
            dataSourceId=dataSourceId
        )
    except Exception as e:
        print(f"Error starting ingestion job: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
    print('Ingestion Job Response: ', response)


    if response["status"] == "FAILED":
        print('Ingestion Job Failed')
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
    print('Ingestion Job Succeeded')
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }