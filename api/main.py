from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import qrcode
import boto3
from io import BytesIO
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# CORS configuration for local testing
origins = [
    "http://localhost:3000" # Replace with actual Public IP when deploying
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS S3 client initialization
s3 = boto3.client('s3')

# Option 1: Reading AWS credentials from .env file (using dotenv)
# Comment out this section if using Option 2

"""
# AWS S3 Configuration
s3 = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ACCESS_KEY"), aws_secret_access_key=os.getenv("AWS_SECRET_KEY"))
"""

# Option 2: Reading AWS credentials from pipeline environment variables
# Uncomment this section if using Option 2

# AWS S3 Configuration
s3 = boto3.client('s3', aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"))


# Bucket name for storing QR codes
bucket_name = 'pmgoriya-qr' # Replace with your actual bucket name

@app.post("/generate-qr/")
async def generate_qr(url: str):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR Code to BytesIO object
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Generate file name for S3
    file_name = f"qr_codes/{url.split('//')[-1]}.png"

    try:
        # Upload QR code image to S3 bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=img_byte_arr, ContentType='image/png', ACL='public-read')

        # Generate the S3 URL for the uploaded QR code
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        return {"qr_code_url": s3_url}
    except Exception as e:
        # Raise HTTPException if an error occurs during the upload process
        raise HTTPException(status_code=500, detail=str(e))

   
