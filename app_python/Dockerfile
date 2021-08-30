FROM python:3.9-slim-buster

# Update all dependencies
RUN apt-get update && apt-get install

# Create user and set ownership and permissions
RUN mkdir app 
RUN adduser --disabled-password guest && chown -R guest /app

WORKDIR /app

# Install required packages
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the main code
COPY main.py world_time.py /app/

# Select unprivileged user
USER guest
ENTRYPOINT ["/app"]

# Configure environement variables
ENV FLASK_ENV=development

# Expose port
EXPOSE 5000

CMD [ "python", "main.py" ]
