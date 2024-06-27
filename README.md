# Deploy REST API with CDK in Python

YouTube Video: [Deploy a REST API with CDK in Python]()

In this video, we are using CDK in Python to define and deploy infrastructure resources for a demo inventory service API.

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
