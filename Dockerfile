FROM python:3.12

WORKDIR /Diabetes

COPY . /Diabetes

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app/main.py"]
