# Set base image (host OS)
FROM python:3.9.6

ENV APP_HOME /app

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR ${APP_HOME}

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /app

# Specify the command to run on container start
CMD [ "python", "App.py" ]