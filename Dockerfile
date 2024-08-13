FROM apache/airflow:2.9.3-python3.8

RUN mkdir -p /srv
WORKDIR /srv
COPY .env /srv
RUN bash -c "source .env"
COPY requirements.txt /srv
RUN pip install -r requirements.txt

COPY src/ /srv
COPY entrypoint.sh /srv
RUN chmod +x /srv/entrypoint.sh

EXPOSE 8080

CMD ["/srv/entrypoint.sh"]
# CMD ["airflow", "standalone"]
