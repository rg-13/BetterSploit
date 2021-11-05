FROM python:3.8





COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./data /data
COPY ./lib /lib
COPY ./Albert.py /Albert.py


CMD ["python3", "/lib/custom/cmd.py"]