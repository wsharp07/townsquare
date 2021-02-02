FROM python:3.9-slim
ADD . /app
WORKDIR /app
RUN pip install -e .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:application"]