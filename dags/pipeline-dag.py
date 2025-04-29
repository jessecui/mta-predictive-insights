from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),    
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='minimal_boilerplate_dag',
    default_args=default_args,
    description='A minimal boilerplate DAG with start and end tasks.',
    schedule=None,
    catchup=False,
    tags=['boilerplate', 'example'],
) as dag:
    
    start_task = EmptyOperator(
        task_id='start'
    )
    
    processing_task = EmptyOperator(
        task_id='processing_step'
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    start_task >> processing_task >> end_task