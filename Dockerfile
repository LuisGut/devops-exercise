FROM python:3.8.1-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt 
EXPOSE 5000
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 