# Serverless Task API (AWS)

## 📌 Project Overview

This project demonstrates a fully serverless backend application built on AWS. It allows users to create and retrieve tasks using a RESTful API powered by API Gateway, AWS Lambda, and DynamoDB.

---

## 🏗️ Architecture

Client → API Gateway → Lambda → DynamoDB

---

## ⚙️ AWS Services Used

* API Gateway (HTTP API)
* AWS Lambda (Python)
* DynamoDB (NoSQL database)
* IAM (Permissions & Roles)
* CloudWatch (Logs & Monitoring)

---

## 🚀 Features

* Create tasks (POST /tasks)
* Retrieve tasks (GET /tasks)
* Serverless architecture (no servers to manage)
* Fully integrated AWS services

---

## 📂 Project Structure

```
serverless-api/
 ├── README.md
 ├── screenshots/
```

---

## 🧪 Testing

### POST /tasks

Creates a new task.

Request body:

```json
{
  "taskName": "Build AWS portfolio"
}
```

Response:

```json
{
  "message": "Task created successfully",
  "taskId": "generated-id",
  "taskName": "Build AWS portfolio"
}
```

---

### GET /tasks

Returns all tasks.

Response:

```json
[
  {
    "taskId": "abc-123",
    "taskName": "Study AWS"
  }
]
```

---

## 📸 Screenshots

### DynamoDB Table

![DynamoDB](screenshots/01-dynamodb-table.png)

### Lambda Function

![Lambda](screenshots/02-lambda-overview.png)

### Lambda Code

![Lambda Code](screenshots/04-lambda-code.png)

### API Gateway Routes

![API Gateway](screenshots/12-api-routes-get-post.png)

### POST Request Test

![POST Test](screenshots/09-api-post-test.png)

### GET Request Test

![GET Test](screenshots/13-api-get-test.png)

---

## ⚠️ Troubleshooting

* Fixed IAM permission issue for Lambda → DynamoDB access
* Verified Lambda execution via test events
* Resolved API request formatting issues (JSON body format)
* GET failed initially but resolved it by adding Integration details under GET Route

---

## 🔮 Future Improvements

* Add PUT and DELETE endpoints
* Add task status (completed/pending)
* Add authentication (Cognito / JWT)
* Add frontend UI (React)

---

## 👨‍💻 Author

MxAli
