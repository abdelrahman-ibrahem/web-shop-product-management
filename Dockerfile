FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set the working directory inside the container
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt /app/

# install dependencies
RUN pip install -r requirements.txt

# copy the rest of the application code
COPY . /app/

# expose the port the app runs on
EXPOSE 8000

# run the django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]