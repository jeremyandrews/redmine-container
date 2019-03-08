FROM python:3

WORKDIR /usr/src/app

#COPY requirements.txt migrate.py ./
RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "python", "migrate.py" ]
# For testing and development purposes, simply launch python container and leave
# running for a full day.
CMD ["sleep", "86400"]
