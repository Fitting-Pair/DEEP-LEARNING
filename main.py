from fastapi import FastAPI, File, UploadFile,Form
import uvicorn
import subprocess
import json
import os
import torch
import trimesh
from measure import generate_json
from measurement_definitions import SMPLXMeasurementDefinitions, STANDARD_LABELS
import requests
import shutil
from pydantic import BaseModel
from pydantic_core import from_json


app = FastAPI()

class UserSize(BaseModel):
    chestSize:float
    hipSize:float
    shoulderSize:float
    waistSize:float

class UserBodySizeRequestDto(BaseModel):
    userId:int
    userSize:UserSize

#Spring obj file -> Python
@app.post("/create/json")
async def analyze_obj(user_id: int = Form(...), file: UploadFile = File(...)):
    # contents = await file.read()
    upload_dir = "/Users/vecherish/Desktop/deep/DEEP-LEARNING/SMPL-Anthropometry/data/obj"
    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # JSON 데이터 생성
        json_data = generate_json(file_path)
        #json -> 딕셔너리
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        #후에 모델로 변환
        user_size = UserSize(**json_data)
        user_body_size_request_dto = UserBodySizeRequestDto(userId=user_id,userSize=user_size)
        
        response_data = user_body_size_request_dto.json()

        # JSON 데이터를 다른 Spring 엔드포인트로 전송
        url = 'http://localhost:8080/get/json'
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, data=response_data, headers=headers)
        
        if response.status_code == 200:
            return {"status_code": response.status_code, "message": "Data sent successfully"}
        else:
            return {"status_code": response.status_code, "message": "Failed to send data"}
    finally:
        # 파일 삭제
        if os.path.exists(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/")
def read_root():
    return {"hello":"world"}
