FROM python:3.8-slim

WORKDIR /app

# Copy the directory
COPY . $WORKDIR

# RUN apt-get update && \
#     apt-get install -y build-essential gcc


WORKDIR /app/todo_project

# Install requirements
RUN pip install -r requirements.txt && \
    chmod +x ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]