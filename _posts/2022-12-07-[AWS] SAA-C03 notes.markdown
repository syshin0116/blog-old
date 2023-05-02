---
layout: post
title: Architect Associate Certification SAA-C03 Notes
date: 2022-12-07 16:50:23 +0900
category: AWS
---
# Architect Associate Certification SAA-C03 Notes

AWS: Amazon Web Services

Services covered in this course:

* EC2
* CVR
* ECS
* Elastic Beanstalk
* Lambda
* Auto Scaling
* IAM
* KMS
* S3
* SES
* RDS
* Aurora
* DymamoDB
* ElastiCache
* SQS
* SNS
* Step Functions
* CloudWatch
* CloudFormation
* CloudTrail
* API Gateway
* Elastic Load Balancing
* CloudFront
* Kinesis
* Route 53

### How to choose an AWS Region?

Question: If you need to launch a new application, where should you do it?

1. Compliance with data governmance and legal requirements:
	* ex) if you want your data to leave a specific region
2. Proximity to customers(close to target users):
	* reduced latency
3. Available Services witin a region:
	* new services and new feature aren't available in very Region
4. Pricing: 
	* pricing varies region to region and is transparent in the sevice pricing page 

### AWS Availability Zones

* Each region has multiple ZA(availability zones) example:
	* ap-southeast-2a
	* ap-southeast-2b

Each availability zones(ZA):

* is one or more discrete data centers with redundant power, networking, and connectivity
* is sesparate from each other -> isolated from disasters
* is connected with high bandwidth, ultra-low latency networking


## IAM & AWS CLI
### IAM: Users & Groups

* IAM : Identity and Access Management, Gloabal service
* Root account : created by default, shouldn't be used or shared
* Users are people within your organization, and can be grouped
* Groups can only contain users, not other groups
* Users don't have to belong to a group
* Users can belong to multiple groups

<img width="722" alt="image" src="https://user-images.githubusercontent.com/99532836/206182859-b503470c-8d5b-4b25-ae36-36702cedfab7.png">

### IAM: Permissions
* Users or Groups can be assigned JSON documents called policies(defines permissions of users)

<img width="431" alt="image" src="https://user-images.githubusercontent.com/99532836/206183704-42b5d5c5-8afd-4a18-9e93-261f8b9d4c78.png">

Organizing Users:
* best not to use Root id (security reasons)
* instead, create a group called admin with all permissions and create a user in it

Account Alias: an account nickname user can create

* once created, sign-in url is created below

<img width="355" alt="image" src="https://user-images.githubusercontent.com/99532836/206187759-94cdaac2-4ab6-45b9-a9c0-793541006ea0.png">
<img width="355" alt="image" src="https://user-images.githubusercontent.com/99532836/206188142-2a239fb9-266b-4fa3-ae4d-a8d921fdb994.png">

### IAM Policies inheritance
