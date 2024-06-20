FROM python:3.12

WORKDIR /Deposit

COPY . .
RUN pip3 install -r requirements.txt
RUN pytest -v
CMD ["fastapi", "run", "main.py", "--port", "8000"]

