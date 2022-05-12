FROM python:3.9-slim

RUN useradd -r -s /bin/bash/ bot


ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R bot:bot /app
USER bot

# ARG AWS_ACCESS_KEY_ID
# ARG AWS_SECRET_ACCESS_KEY
# ARG AWS_DEFAULT_REGION

ARG WEBEX_BOT_TOKEN
ARG WEBEX_BOT_EMAIL
ARG WEBEX_BOT_APP_NAME

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION

ENV WEBEX_BOT_TOKEN $WEBEX_BOT_TOKEN
ENV WEBEX_BOT_EMAIL $WEBEX_BOT_EMAIL
ENV WEBEX_BOT_APP_NAME $WEBEX_BOT_APP_NAME

ADD ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user

COPY --chown=bot:bot . /app
WORKDIR /app

CMD ["python", "bot.py"]