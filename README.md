# AWS RAG Chatbot

This project is an implementation of a Retrieval-Augmented Generation (RAG) chatbot using AWS BEDROCK services. The chatbot leverages retrieval-based techniques to provide accurate and context-aware responses.

![Architecture](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/AWS%20RAG%20Chat%20bot.png?raw=true)

## Prerequisites

- AWS account with necessary permissions.
- Python 3.8 or later.
- AWS CLI configured with your credentials.

## Building the Backend on AWS: S3 and Amazon Bedrock

To build the backend of the application, we will interact with two AWS services: S3 and Amazon Bedrock. We will upload documents to an S3 bucket, which will serve as the knowledge source for our knowledge base (KB). Then, we will create the knowledge base in Bedrock, connecting it to the S3 bucket.

### 1. Creating the Knowledge Source (S3 Bucket)

1.  Navigate to the S3 service in the AWS Management Console.
2.  Choose the region.
3.  Create a new S3 bucket, keeping the default settings unless specific configurations are required.
4.  Upload the documents that will serve as the knowledge source to the newly created S3 bucket.

    _Example:_

    ![S3 Bucket with Documents](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/10.jpeg?raw=true)

### 2. Creating the Knowledge Base in Bedrock

1.  Go to the Amazon Bedrock service in the AWS Management Console.
2.  In the left navigation pane, under **Builder tools**, find and click on **Knowledge base**.
3.  Click on **Create knowledge base**.

4.  **Configure the Knowledge Base:**

    - Provide a name for the knowledge base and an optional description.
    - Unless you have specific requirements for IAM permissions and tags, you can leave the default settings and proceed to the next step.

    ![Knowledge Base Configuration](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/6.jpeg?raw=true)

5.  **Connect to the S3 Bucket:**

    - In this step, connect the S3 bucket created earlier. Ensure that you are in the region, as only buckets from that region will be visible.
    - You can choose to connect the entire bucket or select specific documents within it.
    - Under **Advanced settings**, you can customize the chunking strategy. Options include:

    **Note:- Unless you have specific chunking requirements or have pre-processed your documents, the **Default chunking** option is usually sufficient. Proceed to the next step.**


6.  **Select Embedding Model and Vector Database:**

    - Choose an embedding model for the documents and a vector database to store, manage, and update the embeddings. AWS can automatically create the vector database for you.
    - For the vector store, you can either let Bedrock create a new vector store in Amazon OpenSearch or connect to a previously created vector store in OpenSearch, Aurora, Pinecone, or Redis.
    - If you don't have specific requirements, creating a new vector store is a good option.

    ![Vector Store Options](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/9.jpeg?raw=true)

7.  **Review and Create:**

    - Review all the information provided.
    - Click **Create Knowledge base**. This will initiate the preparation of the vector database in Amazon OpenSearch Serverless.

    ![Creating Knowledge Base](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/7.jpeg?raw=true)

8.  **Locate the Vector Store:**

    - The vector store can be found under **Collections** in the Amazon OpenSearch Service.

    ![Amazon OpenSearch Service Collections](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/1.jpeg?raw=true)

9.  **Sync the Data Source:**

    - After the knowledge base is created, you must sync the data source to populate the vector store.

    ![Syncing Data Source](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/4.jpeg?raw=true)

10. **Understanding the Sync Process:**

    - The sync process is crucial for creating the knowledge base.
    - It involves:
      - Looking up documents in the S3 bucket.
      - Preprocessing and extracting text from the documents.
      - Creating smaller chunks of data based on the defined chunking strategy.
      - Passing the chunks to the selected embedding model.
      - Storing the resulting embeddings in the vector store.
    - Whenever data in the S3 bucket is modified, added, or removed, the data source must be re-indexed by syncing the data again. This can be done manually from the console or automated.

11. **Testing the Knowledge Base:**
    - Once the sync is complete, you can test the knowledge base from the console or query the documents using Bedrock clients from an application.
    ![example1](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/screenshot-1.png?raw=true)
    - The RAG chatbot can only retrieve information from the data it has been provided; it cannot answer general knowledge questions.
    ![example2](https://github.com/kishore1919/aws_rag_chatbot/blob/main/images/screenshot-2.png?raw=true)

## Lambda

The AWS RAG Chatbot leverages AWS Lambda functions to handle requests and responses efficiently. These Lambda functions are designed to process incoming queries, interact with the knowledge base, and return context-aware responses to the user.

### Key Features of Lambda Integration:

1. **Request Handling:**
    - The Lambda function receives user queries through an API Gateway or other triggering mechanisms.
    - It parses the input and prepares the query for interaction with the knowledge base.

2. **Knowledge Base Interaction:**
    - The Lambda function communicates with the Amazon Bedrock knowledge base to retrieve relevant information.
    - It ensures that the query is processed using the embedding model and vector database for accurate results.

3. **Response Generation:**
    - After retrieving the relevant data, the Lambda function formats the response and sends it back to the user.
    - The response is designed to be concise, context-aware, and aligned with the user's query.

4. **Resyncing the Knowledge Base:**
    - The Lambda function interacts with the Amazon Bedrock knowledge base and S3 to synchronize updated data with the knowledge base.
    - Configure a trigger to execute the Lambda function automatically whenever new data is added to the S3 bucket.

### Lambda Function Deployment:

- Ensure that the Lambda functions have the necessary IAM permissions to interact with the S3 bucket, Amazon Bedrock, and other AWS services used in the application.

By integrating Lambda functions, the AWS RAG Chatbot achieves a scalable and serverless architecture, enabling efficient query processing and response generation.


## Acknowledgments

- Inspired by advancements in RAG techniques.
- Built with AWS services for seamless cloud integration.
- Special thanks to the open-source community.
