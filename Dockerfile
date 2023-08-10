
#sets the base image for the Docker container, it's using the official Python 3.10 image as the base
FROM python:3.10        

#This sets the working directory within the container to /EmotionDetection, 
#where the application code and related files will be placed.
WORKDIR /EmotionDetection

#This copies the requirements.txt file from the host (your local machine) to the current working directory in the container.
COPY ./requirements.txt ./requirements.txt

#This installs the Python dependencies listed in the requirements.txt
RUN pip install -r ./requirements.txt

#This copies the content of the ./app directory from the host to the /EmotionDetection/app directory within the container.
COPY ./app /EmotionDetection/app

#This specifies the command to run when the container starts. 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]