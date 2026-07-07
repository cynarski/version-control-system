FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /opt/vcs

COPY pyproject.toml README.md ./
COPY src ./src

RUN python -m pip install .

WORKDIR /workspace

CMD ["/bin/bash"]
