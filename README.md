# AWS Lambda Rest Api

## What is "AWS Lambda Rest Api"
It makes rest api lambda simple and readable.

## How To Install

```shell
$ pip install aws-lambda-rest-api
```

or 

```txt
# requirements.txt
︙
aws-lambda-rest-api
︙
```

## How To Use

Suppose write resource file as below,

```yaml
Resources:
  QuestionApi:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: questions/
      Handler: rest.lambda_handler
      Runtime: python3.8
      Events:
        GetQuestions:
          Type: Api
          Properties:
            Path: /questions
            Method: get
        GetQuestion:
          Type: Api
          Properties:
            Path: /questions/{question_id}
            Method: get
        CreateQuestion:
          Type: Api
          Properties:
            Path: /questions
            Method: post
        UpdateQuestion:
          Type: Api
          Properties:
            Path: /questions/{question_id}
            Method: put
        PartialUpdateQuestion:
          Type: Api
          Properties:
            Path: /questions/{question_id}
            Method: put
        DestroyQuestion:
          Type: Api
          Properties:
            Path: /questions/{question_id}
            Method: delete
```

You can write rest.py as below.

```python

from aws_lambda_rest_api import RestApi

class QuestionApi(RestApi):
    detail_key = 'question_id'

    def list(self, event, context):
        return {
            'statusCode': 200,
            'body': [1, 2, 3],
        }

    def retrieve(self, event, context):
      question_id = event['pathParameters'].get('question_id')
      return {
          'statusCode': 200,
          'body': {'id': question_id, 'title': 'Hello Question'},
      }

    def create(self, event, context):
        return {
            'statusCode': 200,
            'body': 'Done create.',
        }

    def update(self, event, context):
      question_id = event['pathParameters'].get('question_id')
      return {
          'statusCode': 200,
          'body': 'Done update.',
      }

    def partial_update(self, event, context):
        question_id = event['pathParameters'].get('question_id')
        return {
            'statusCode': 200,
            'body': 'Done update partially.',
        }

    def destroy(self, event, context):
      question_id = event['pathParameters'].get('question_id')
      return {
          'statusCode': 200,
          'body': 'Done destroy.'
      }

lambda_handler = QuestionApi().create_handler()

```

The chart below shows the relationship between the http method and overrided method.

|Http Method|Detail?|Overrided Method|
|:----|:----|:----|
|GET|TRUE|retrieve|
|GET|FALSE|list|
|POST|TRUE|-|
|POST|FALSE|create|
|PUT|TRUE|update|
|PUT|FALSE|-|
|PATCH|TRUE|partial_update|
|PATCH|FALSE|-|
|DELETE|TRUE|destroy|
|DELETE|FALSE|-|
|ANY|ANY|default|


## How To Release

```python
$ pipenv run clean
$ pipenv run package
$ pipenv run publish
```