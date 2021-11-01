FROM python:3.8





COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./data /data
COPY ./lib /lib
COPY ./Albert.py /Albert.py

EXPOSE 5432
CMD ["python3", "Albert.py"]