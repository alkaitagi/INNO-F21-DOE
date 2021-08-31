FROM python:3.9-slim-buster

# Create user and set ownership and permissions
RUN mkdir app 
RUN adduser --disabled-password guest && chown -R guest /app

# Select user & directory
WORKDIR /app
USER guest

# Install required packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the main code
COPY main.py world_time.py ./

# Expose port
EXPOSE 5000
CMD [ "python", "main.py" ]
