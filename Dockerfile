FROM alpine:latest

RUN apk update && apk add --no-cache --upgrade bash
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add --update --no-cache py3-numpy

COPY ./first_program.py ./first_program.py
COPY ./second_program.py ./second_program.py

RUN chmod u+x ./second_program.py

CMD ["python3", "second_program.py"]