FROM python:3.8





COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./data /data
COPY ./albert.py /albert/
WORKDIR /albert


CMD ["python3", "albert.py"]