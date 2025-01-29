VENV_DIR = .venv
AIRFLOW_HOME = $(shell pwd)/airflow

install:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r requirements.txt

init:
	export AIRFLOW_HOME=$(AIRFLOW_HOME) && $(VENV_DIR)/bin/airflow db init

create_user:
	export AIRFLOW_HOME=$(AIRFLOW_HOME) && $(VENV_DIR)/bin/airflow users create \
		--username admin \
		--firstname admin \
		--lastname admin \
		--role Admin \
		--email admin@admin.com

scheduler:
	export AIRFLOW_HOME=$(AIRFLOW_HOME) && $(VENV_DIR)/bin/airflow scheduler

webserver:
	export AIRFLOW_HOME=$(AIRFLOW_HOME) && $(VENV_DIR)/bin/airflow webserver --port 8080

copy_dag:
	mkdir -p $(AIRFLOW_HOME)/dags
	cp dags/etl_dag.py $(AIRFLOW_HOME)/dags/

run: install init create_user copy_dag scheduler webserver

.PHONY: install init create_user scheduler webserver copy_dag run
