# Deploy a REST API with CDK in Python

YouTube Video: [REST API with CDK in Python](https://youtu.be/kWED0OwpUb0)

Learn how to use AWS CDK in Python to define and deploy infrastructure resources. In this video, we deploy a stack for a demo inventory service API.

For more information on the demo inventory API and API testing, check this video:
[OpenAPI, AWS, Postman - Building a REST API](https://youtu.be/3h-anwBFio8)

## Steps

### Requirements

Requirements for any CDK app, in general, check out: [Getting Started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

Specific to CDK apps in Python: [Working with the AWS CDK in Python
](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)

### Clone the repository

cd into the project

### Create a virtual environment with venv

```sh
python3 -m venv .venv
```

### Activate venv environment

```sh
source .venv/bin/activate
```

### Install package dependencies

Install into the venv virtual environment for this project:

```sh
pip install -r requirements.txt
```

### Deploy to AWS account/region

```sh
cdk deploy
```
