# Static Website Hosting on AWS with S3 + CloudFront

This project demonstrates how to host a **static website** on **Amazon S3** and serve it globally using **Amazon CloudFront (CDN)**. The setup ensures high availability, fast content delivery, and secure access.  

---

## 🚀 Features
- **Static Website Hosting** with Amazon S3  
- **Content Delivery** via Amazon CloudFront  
- **Default Root Object** configuration for clean routing  
- **Public Access Control** using CloudFront Origin Access  

---

## 🏗️ Workflow

- **User Browser** → Sends request to the CloudFront distribution domain.  
- **CloudFront** → Acts as CDN, caches content at edge locations, improves performance.  
- **S3 Bucket** → Stores the static website files (HTML, CSS, JS, images).  

<img width="1536" height="1024" alt="Workflow Diagram" src="https://github.com/user-attachments/assets/061a37ff-e62b-4504-9284-823f33dd8654" />

---

## ⚙️ Deployment Steps

1. **Create S3 Bucket**  
   - Enable **Block Public Access** (all settings ON).  
   - Upload website files.  

2. **Set Up CloudFront Distribution**  
   - Origin → S3 bucket.  
   - Default Root Object → `mxali_index.html`.  
   - Restrict bucket access using **Origin Access Control (OAC)**.  

3. **Update Bucket Policy**  
   - Grant access to CloudFront only.
   -     Note: CloutFront generates access policy under Origin access settings which needs to be applied to S3 bucket.

4. **Test Distribution**  
   - Access your website via the **CloudFront Distribution Domain Name**.  
---
## 🌐 Website

🔗 [View Website](https://d12tpsyqt3v5p6.cloudfront.net/)  

---

## 🧰 Tools & Services Used

- **AWS S3** (Static Website Hosting)  
- **AWS CloudFront** (Content Delivery Network)  
- **AWS IAM** (Access & Security)
    
---

## Screenshots
<img width="1350" height="1462" alt="mxali_index_main_local" src="https://github.com/user-attachments/assets/c17915fd-81e6-432b-8cbc-c23f81aefc12" />

---

## 📖 What I Learned
- Setting up secure static website hosting in AWS.  
- Using CloudFront to improve performance and security.  
- Managing bucket policies and CloudFront OAC.
- Troubleshooting access denied issue when accesing URL.
    . <Default Root Object - Provide html path if nothing else works>.

---

## 👨‍💻 Author
**MXALI**  
