#!/bin/bash

dropdb --if-exists autograder
dropuser --if-exists grader_user

createdb autograder
psql autograder < submission.sql

psql --no-psqlrc template1 -c "create user grader_user;"
psql --no-psqlrc template1 -c "alter user grader_user password 'thewindisblowing';"
psql --no-psqlrc template1 -c "grant all on DATABASE autograder to grader_user;"
psql --no-psqlrc autograder -c "GRANT ALL on ALL tables IN SCHEMA public to grader_user"
