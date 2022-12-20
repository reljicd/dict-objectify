FROM python:3.11-alpine

ENV APP_HOME /app
ENV TESTS_PATH /app/tests
ENV PYTHONPATH ${PYTHONPATH}:${APP_HOME}:${TESTS_PATH}

WORKDIR ${APP_HOME}

COPY ./dict_objectify/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./dict-objectify ${APP_HOME}

ENTRYPOINT ["python"]