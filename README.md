# DEEP-LEARNING

상명대학교 졸업 프로젝트 팀 피팅페어의 딥러닝 서버 레포지토리입니다. 이 프로젝트는 의류 피팅 시뮬레이션을 위한 딥러닝 모델을 개발 및 배포하기 위해 만들어졌습니다.

## 저작권

저작권은 모두 [DavidBoja/SMPL-Anthropometry](https://github.com/DavidBoja/SMPL-Anthropometry) 분에게 있습니다. 저희는 해당 레포지토리를 약간 변형하여 상업적 용도가 아닌 졸업 프로젝트 용도로 사용함을 명시합니다.

## 개요

이 프로젝트는 SMPL(Statistical Model of Human Shape) 모델을 기반으로 하여 사용자의 체형을 분석하고, 이를 통해 가상 피팅을 시뮬레이션합니다. 주요 기능은 다음과 같습니다:

- 사용자 체형 데이터 수집 및 전처리
- SMPL 모델을 사용한 체형 분석
- 가상 피팅 결과 시각화
## 기술 스택

- **FastAPI**: Python을 기반으로 한 고성능 웹 프레임워크
- **Uvicorn**: ASGI 서버 구현체로 FastAPI 애플리케이션을 실행
- **Pydantic**: 데이터 유효성 검사 및 설정 관리
- **Torch**: 딥러닝 프레임워크
- **Trimesh**: 3D 메시 처리 라이브러리

## 설치

### 필수 요구사항

- Python 3.7 이상
- 필요한 Python 패키지들은 `requirements.txt`에 명시되어 있습니다.

### 설치 방법

1. 이 레포지토리를 클론합니다.

    ```bash
    git clone https://github.com/your-repository/deep-learning.git
    cd deep-learning
    ```

2. anaconda 가상 환경을 설정하고 활성화합니다.

    ```bash
   conda activate smpl
    ```
3. 필요한 패키지들을 설치합니다.

    ```bash
    pip install -r requirements.txt
    ```

## 사용 방법

1. 서버 실행

    ```bash
    uvicorn main:app --reload
    ```

2. API 엔드포인트를 통해 데이터를 주고받습니다. 주요 엔드포인트는 다음과 같습니다:

    - `/create/json`: obj 파일을 업로드하고 JSON 데이터를 생성합니다.
    - `/get/json`: 생성된 JSON 데이터를 받아서 처리합니다.

## 프로젝트 구조

- `main.py`: FastAPI 서버의 메인 파일입니다.
- `measure.py`: SMPL 모델을 사용하여 체형 데이터를 분석하는 코드가 포함되어 있습니다.

## 라이선스

이 프로젝트는 [MIT 라이선스](LICENSE)를 따릅니다.

## 문의

문제가 된다면 해당 이메일로 문의 주시면 감사하겠습니다.
[202010852@sangmyung.kr](202010852@sangmyung.kr)
