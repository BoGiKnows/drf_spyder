FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/drf_spyder

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/drf_spyder

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]