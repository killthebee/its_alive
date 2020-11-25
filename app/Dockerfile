FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /app/app
RUN python3.7 -m pip install --upgrade pip
RUN pip install -r app/requirements.txt
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]