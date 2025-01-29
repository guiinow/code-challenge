from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

# Imports dos scripts de ETL, cada um em um arquivo separado
from scripts.extract_csv import extract_csv
from scripts.extract_postgres import extract_postgres
from scripts.load_postgres import load_postgres
from scripts.transform_data import transform_data

""" # Adicione o diretório de scripts ao sistema de path
scripts_path = os.path.join(os.path.dirname(__file__), '..', 'scripts')
if scripts_path not in sys.path:
    sys.path.append(scripts_path) """


# Definição do DAG
with DAG('etl_dag', start_date=datetime(2025, 1, 26), schedule_interval='0 8 * * *', catchup=False) as dag: #essa cron do unix é pra rodar todo dia as 8 da manhã
    extract_csv_task = PythonOperator(
        task_id='extract_csv',
        python_callable=extract_csv,
        op_kwargs={'file_path': './data/order_details.csv', 'output_path': 'data/extracted_data.csv'}
    )

    extract_postgres_task = PythonOperator(
        task_id='extract_postgres',
        python_callable=extract_postgres,
        op_kwargs={'output_path': 'data/extracted_postgres_data.csv'}
    )

    transform_data_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    load_postgres_task = PythonOperator(
        task_id='load_postgres',
        python_callable=load_postgres
    )

    # Define a ordem das tarefas no grafo
    extract_csv_task >> extract_postgres_task >> transform_data_task >> load_postgres_task
