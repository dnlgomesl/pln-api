FROM python:3.8-slim-buster

ARG KEY

ENV KEY_API=$KEY

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["src/__main__.py"]