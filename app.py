from fastapi import FastAPI, UploadFile
import boto3

app = FastAPI()

s3 = boto3.client("s3")
BUCKET = "my-fastapi-upload-bucket"

@app.get("/")
def home():
    return {"message": "FastAPI running on Elastic Beanstalk"}

@app.post("/upload")
async def upload(file: UploadFile):
    s3.upload_fileobj(file.file, BUCKET, file.filename)
    return {"uploaded": file.filename}