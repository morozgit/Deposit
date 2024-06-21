FROM python:3.12

WORKDIR /Deposit

COPY . .
RUN pip3 install -r requirements.txt
RUN pytest -v
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

