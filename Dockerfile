FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

RUN pip install --target=/app requests

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
RUN apk add --update python py-pip 
RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt
CMD ["/app/main.py"]