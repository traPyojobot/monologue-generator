FROM python:3.8-alpine
RUN apk add build-base
RUN apk add --update bash git curl build-base swig gfortran linux-headers
RUN cd /tmp \
    && git clone https://github.com/taku910/mecab.git \
    && cd mecab/mecab/ \
    && ./configure --enable-utf8-only --with-charset=utf8 \
    && make \
    && make install \
    && cd ../mecab-ipadic \
    && ./configure --with-charset=utf8 \
    && make \
    && make install

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app/
RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]