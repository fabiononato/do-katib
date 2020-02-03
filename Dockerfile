FROM tensorflow/tensorflow:1.13.1-gpu-py3

LABEL maintener="Fabio Nonato (@nonatofabio)"

ARG http_proxy
ARG https_proxy
ARG no_proxy

ADD Container-Root /

RUN export http_proxy=$http_proxy; export https_proxy=$https_proxy; export no_proxy=$no_proxy; /setup.sh; rm -f /setup.sh

WORKDIR /src

CMD /startup.sh
