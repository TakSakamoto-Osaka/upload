FROM python:3.11.9

COPY ./ /root/
WORKDIR /root/
RUN pip install --upgrade pip --proxy=http://gwproxy.daikin.co.jp:3128
RUN pip install -r requirements.txt --proxy=http://gwproxy.daikin.co.jp:3128
