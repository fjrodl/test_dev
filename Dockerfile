# Dockerfile
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
# Copy application files
COPY . /app/
# Install dependencies
RUN pip install flask

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000", "--debugger", "--reload" ]
