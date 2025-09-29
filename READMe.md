# Serverless Contact Form with AWS

## Project Overview

This is a **serverless contact form** built using **AWS S3, Lambda, API Gateway, and SES**.  
It allows users to submit messages through a web form, which are then sent as emails without the need for a backend server.  

**Key Features:**
- Fully serverless architecture
- Email notifications via AWS SES
- Hosted static website on AWS S3
- API Gateway triggers Lambda functions for email processing
- Beginner-friendly and portfolio-ready AWS project

---

## Architecture Diagram
[User Browser]
|
v
[S3 Static Website]
|
v
[API Gateway POST /contact]
|
v
[Lambda Function]
|
v
[AWS SES Email Delivery]


**Explanation:**
1. User fills out the form hosted on **S3**.
2. Form submission triggers **API Gateway** POST request.
3. **Lambda function** processes the request and sends email via **SES**.
4. User sees a confirmation message on the website.

---

## Project Files

- `index.html` – Contact form HTML page
- `form.js` – JavaScript code to send form data to API Gateway
- `lambda_function.py` – Python Lambda function code
- `README.md` – Project documentation

---

## Setup Instructions

### 1. Verify Email in AWS SES
1. Go to **AWS SES → Verified Identities → Verify email address**.
2. Check your inbox and verify the email.

### 2. Create Lambda Function
1. Go to **AWS Lambda → Functions → Create Function → Author from scratch**.
2. Runtime: **Python 3.11**.
3. Attach **AmazonSESFullAccess** policy to Lambda execution role.

### 3. Add Lambda Code
- Use the `lambda_function.py` code provided in this repository.
- Deploy the function.

### 4. Create API Gateway
1. Go to **API Gateway → HTTP API → Create API**.
2. Integrate Lambda function.
3. Create route: `POST /contact`.
4. Copy the **Invoke URL**.

### 5. Update HTML Form
- In `form.js`, replace `YOUR_API_GATEWAY_INVOKE_URL/contact` with your API Gateway URL.

### 6. Upload to S3
1. Upload HTML, JS, and CSS to your **S3 static website bucket**.
2. Enable public access and website hosting.

### 7. Test the Form
- Open your S3 website.
- Submit the form.
- Check your verified email for the message.

---

## Screenshots

![Website Screenshot](screenshots/website.png)  
![Form Submission Screenshot](screenshots/form_submission.png)  

*(Add screenshots in `screenshots/` folder)*

---

## Technologies Used

- AWS S3 (Static Website Hosting)
- AWS Lambda (Serverless Function)
- AWS API Gateway (HTTP API)
- AWS SES (Simple Email Service)
- HTML / CSS / JavaScript

---

## Portfolio Notes

This project demonstrates:
- End-to-end serverless application architecture
- AWS cloud services integration
- Event-driven architecture using Lambda & API Gateway
- Beginner-friendly portfolio-ready cloud project

---
## Challenges and Solutions

- CloudFront will not show the updated html file content