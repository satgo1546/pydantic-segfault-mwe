FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:0.11.3-alpine3.23
COPY app /root/app
WORKDIR /root/app
CMD ["sh", "-c", "uv run main.py; echo Exit code is $?"]
