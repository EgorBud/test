# our base image
FROM python:3.10

# specify the port number the container should expose
EXPOSE 3003

COPY . .

# run the application
CMD ["python", "serv.py"]
