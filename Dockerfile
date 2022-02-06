#Set base image (host OS)
FROM python:3.8-slim-buster

#Set the working directory in the container
WORKDIR /code

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-tk


#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install dependencies
RUN pip install -r requirements.txt

#Copy the content of the local src directory to the working directory
COPY src/ .

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]