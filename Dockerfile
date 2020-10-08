FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

RUN pip install --target=/app requests

FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]