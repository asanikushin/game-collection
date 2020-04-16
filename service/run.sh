#!/bin/sh
while true; do
    echo Migrating database
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec python runner.py runserver -h 0.0.0.0 -p 8000