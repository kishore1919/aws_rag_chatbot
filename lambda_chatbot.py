"""
This is a simple AWS Lambda function that uses the Bedrock Agent Runtime to retrieve and generate responses from a knowledge base.
It takes a user prompt as input, retrieves relevant information from the knowledge base, and generates a response using a specified model.
The function is triggered by an event, which contains the user prompt, and returns a response with the generated text.
The function uses the Boto3 library to interact with AWS services, specifically the Bedrock Agent Runtime.
The function is designed to be deployed on AWS Lambda, and it requires the following environment variables to be set:
- KNOWLEDGEBASEID: The ID of the knowledge base to be used for retrieval.
- MODELARN: The Amazon Resource Name (ARN) of the model to be used for generation.
"""

import json
import boto3
import os

client_bedrock_knowledgebase = boto3.client('bedrock-agent-runtime')
def lambda_handler(event, context):
    # Validate environment variables
    knowledge_base_id = os.environ.get('KNOWLEDGEBASEID')
    model_arn = os.environ.get('MODELARN')
    if not knowledge_base_id or not model_arn:
        raise ValueError("Environment variables 'KNOWLEDGEBASEID' and 'MODELARN' must be set.")
    print(f"Received user prompt: {event['prompt']}")
    user_prompt = event['prompt']
    client_knowledgebase = client_bedrock_knowledgebase.retrieve_and_generate(
        input={
            'text': user_prompt
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': os.environ['KNOWLEDGEBASEID'],
                'modelArn': os.environ['MODELARN'],
            }
        })

        
    try:
        response_kbase_final = client_knowledgebase['output']['text']
    except KeyError as e:
        print(f"KeyError: Missing key in response - {e}")
        return {'statusCode': 500,'body': response_kbase_final}
        
    print(f"Generated response: {response_kbase_final}")

    return {
        'statusCode': 200,
        'body': response_kbase_final
    }