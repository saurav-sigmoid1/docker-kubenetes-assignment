from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator


defalut_args = {
    'owner': 'Airflow',
    'start_date': datetime(2022, 3, 13),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}
with DAG("Execution_Dag",default_args=defalut_args, schedule_interval='* 6 * * *', template_searchpath=['/usr/local/airflow/sql_files'],catchup=False) as dag:
    t1 = PostgresOperator(task_id="create_new_table",postgres_conn_id='postgres_conn',sql="create_new_table.sql")
    t2 = PostgresOperator(task_id="validate_entry", postgres_conn_id="postgres_conn",sql="create Table log_table as select * from dag_run;")
    t1>>t2