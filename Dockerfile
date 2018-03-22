FROM python:3.5
ENV PYTHONUNBUFFERED 1

# install node
RUN apt-get update
RUN apt-get upgrade -y
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash
RUN apt-get install -y nodejs
RUN apt-get autoremove -y

RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./src /src
COPY django-launcher /
RUN chmod +x /django-launcher
RUN npm install
