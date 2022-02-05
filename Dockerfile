#Set base image (host OS)
FROM python

#Set the working directory in the container
WORKDIR /code

#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install dependencies
RUN pip install -r requirements.txt

#Copy the content of the local src directory to the working directory
COPY src/ .

#Command to run on container start
CMD ["Python3", "./app.py"]