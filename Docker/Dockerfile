FROM postgres
USER postgres
COPY submission.sql /docker-entrypoint-initdb.d/submission.sql
COPY create_db.sh /docker-entrypoint-initdb.d/create_db.sh
EXPOSE 5432
CMD ["postgres"]
