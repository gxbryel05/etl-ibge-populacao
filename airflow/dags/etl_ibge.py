from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, '/opt/airflow/dags/etl')

default_args = {
    'owner': 'gabryel',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extrair():
    from extracao import extrair_municipios
    dados = extrair_municipios()
    return dados

def transformar(**context):
    from transform import transformar
    import pandas as pd
    dados = context['task_instance'].xcom_pull(task_ids='extrair')
    df = pd.DataFrame(dados)
    return df.to_json()

def carregar(**context):
    import pandas as pd
    from load import carregar
    json_data = context['task_instance'].xcom_pull(task_ids='transformar')
    df = pd.read_json(json_data)
    carregar(df)

with DAG(
    dag_id='etl_ibge_municipios',
    default_args=default_args,
    description='Pipeline ETL - Municípios Brasileiros (IBGE)',
    schedule_interval='@daily',
    start_date=datetime(2024, 6, 1),
    catchup=False,
    tags=['etl', 'ibge', 'dados'],
) as dag:
    t1 = PythonOperator(
        task_id='extrair',
        python_callable=extrair,
    )

    t2 = PythonOperator(
        task_id='transformar',
        python_callable=transformar,
        provide_context=True,
    )

    t3 = PythonOperator(
        task_id='carregar',
        python_callable=carregar,
        provide_context=True,
    )

    t1 >> t2 >> t3