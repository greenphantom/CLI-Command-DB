FROM python:3.10.9-bullseye
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]