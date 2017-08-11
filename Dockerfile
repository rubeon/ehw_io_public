FROM myrepo/suc:latest
MAINTAINER Eric Williams <eric@subcritical.org>


RUN [ -d /srv/subc/ ] || mkdir /srv/subc/
WORKDIR /srv/subc/
ADD . /srv/subc/
RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential \
   software-properties-common  \
   git htop man unzip joe wget \
   libjpeg-dev libmysqlclient-dev \
   python-pip uwsgi-plugin-python
RUN pip install -r /srv/subc/requirements/requirements.txt

CMD ['/srv/subc/start.sh']
EXPOSE 8001
