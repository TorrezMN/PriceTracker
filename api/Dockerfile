
# DOCKERFILE API



FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update && apt-get -y install cron && apt-get -y install htop


COPY . /code/api/


CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "80"]
