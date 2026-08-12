FROM python:3.11.15-slim-trixie 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /app



COPY requirements.txt /app/

EXPOSE 8000

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY ./core  /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]