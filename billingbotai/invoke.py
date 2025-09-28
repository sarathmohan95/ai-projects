#Imports
import boto3
import json

#Create the bedrock client
bedrock = boto3.client('bedrock-runtime')

#Setting the prompt
prompt_data = """Command: Write me a summary about 3I/Atlas comet in 50 words.

Blog:
"""

#Model specification
modelId = "amazon.nova-micro-v1:0"
accept = "application/json"
contentType = "application/json"

#Configuring parameters to invoke the model
body = json.dumps({
  "inputText" : prompt_data,
  "textGenerationConfig" : {
    "maxTokenCount" : 1000
  }
})

#Invoke the model
response = bedrock.invoke_model(
  body = body, modelId = modelId, accept = accept, contentType = contentType
)

#Parsing and displaying the output
response_body = json.loads(response.get('body').read())
output = response_body.get('results')[0].get("outputText")
print(output)