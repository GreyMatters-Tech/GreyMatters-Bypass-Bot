FROM python:3.11.1-slim-bullseye
# python3.11 -m venv venv && . ./venv/bin/activate
ENV VIRTUAL_ENV=/opt/venv
RUN python3.11 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /bypass
ENV TZ=Asia/Kolkata PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get upgrade -y
RUN python3.11 -m pip install -U pip
RUN pip3 install -U setuptools wheel
RUN apt-get install -y bash sudo git
RUN sudo apt-get install -y apt-utils build-essential
RUN apt-get install libxml2-dev libxslt-dev python3-dev -y
COPY . .
RUN pip3 install --no-cache-dir -U -r requirements.txt
RUN rm -rf requirements.txt
RUN apt-get update && apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
CMD ["python3.11", "main.py"]
