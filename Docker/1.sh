cp ../submission.sql .
cp ../create_db.sh .
docker build -t postgres_image .
docker run --name sbt_postgres postgres_image

