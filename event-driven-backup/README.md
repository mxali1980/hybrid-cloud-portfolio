## 🚀 Event-Driven Backup System (AWS)

## 📌 Overview

Serverless event-driven file backup system using AWS S3 and Lambda.

## 🏗️ Architecture

* S3 (Source Bucket)
* Lambda
* S3 (Backup Bucket)
* Lifecycle Rule

## 📦 How It Works

1. Upload file to source bucket
2. S3 triggers Lambda
3. Lambda copies file to backup bucket
4. Lifecycle rule deletes old files

## ⚙️ Key Components/Services Used

* AWS S3
* AWS Lambda
* IAM
* Python (boto3)

## 👨‍💻 Author
**MxALI**  
