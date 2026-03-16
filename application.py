from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import os
import boto3

# Load env variables
load_dotenv()

BUCKET = os.getenv("AWS_BUCKET")
REGION = os.getenv("AWS_REGION")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Create S3 client
s3 = boto3.client(
    "s3",
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

application = FastAPI()


@application.get("/")
def home():
    return {"message": "FastAPI running on Elastic Beanstalk"}


@application.get("/welcome")
def welcome():
    return {"message": "Welcome to FastAPI"}


@application.post("/upload")
async def upload(file: UploadFile = File(...)):
    s3.upload_fileobj(file.file, BUCKET, f"uploads/{file.filename}")
    return {"uploaded": file.filename}