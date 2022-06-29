FROM python:3-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements* ./

RUN apt-get update && apt-get install -y mariadb-client libmariadb-dev libfreetype6-dev libtiff-dev libjpeg-dev libwebp-dev \
 libopenjp2-7-dev libffi-dev libssl-dev zlib1g-dev libpcre3-dev libffi-dev liblcms2-dev python3-dev

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]