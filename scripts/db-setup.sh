#!/bin/sh

export PGUSER="postgres"

psql -c "CREATE DATABASE fortune_frame"

psql fortune_frame -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"
