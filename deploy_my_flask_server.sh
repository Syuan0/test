#!/bin/bash
echo 'start to set virtual environment'
mkdir vir_env
tar -zxf new.tar.gz -C vir_env
source vir_env/bin/activate
echo 'finish to set virtual environment'
echo 'start to prepara sqlite3 database and add test data'
touch ceshi.db
python add_db_data.py
echo 'finish to prepara sqlite3 database and add test data'
echo 'start the server'
export FLASK_APP=app_run.py
flask run --port 40000