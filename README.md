📄 AWS Text Detection & Translation using Rekognition and Translate

This project demonstrates how to extract text from an image stored in Amazon S3 using **AWS Rekognition** and then translate the detected text into English using **AWS Translate**.
It is a simple yet practical cloud-based application showcasing the use of multiple AWS AI services together.

---

🚀 Features

- 📷 Detects text from images stored in Amazon S3  
- 🔍 Uses AWS Rekognition for Optical Character Recognition (OCR)  
- 🌍 Automatically detects source language  
- 🔁 Translates extracted text into English using AWS Translate  
- ☁️ Fully cloud-based and serverless-friendly  

---

🛠️ Tech Stack

- **Python**
- **AWS Rekognition**
- **AWS Translate**
- **Amazon S3**
- **Boto3 (AWS SDK for Python)**

---

📂 Project Workflow

1. Image is uploaded to an Amazon S3 bucket  
2. AWS Rekognition scans the image and detects text lines  
3. Detected text is combined into a single string  
4. AWS Translate converts the text into English  
5. Output is displayed in the console  

---

 🧩 Prerequisites

- AWS Account
- Python 3.x installed
- AWS CLI configured
- An S3 bucket with an image containing text
- IAM user with permissions:
  rekognition:DetectText
  translate:TranslateText
  s3:GetObject
