import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

# 선택적으로 default_args 정의
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

with DAG(
    dag_id="my_dag_name",
    default_args=default_args,
    start_date=datetime.datetime(2024, 5, 1),
    schedule_interval="@daily",  # 'schedule' 대신 'schedule_interval' 사용
    catchup=False,  # catchup을 원하지 않는 경우, 기본값은 True
) as dag:
    task1 = EmptyOperator(task_id="task")

# 의존성을 정의하는 코드가 있으면 추가하는 것이 좋습니다.
# 예를 들어, task1 -> task2 로의 의존성이 있는 경우 아래와 같이 표현할 수 있습니다.
# task2 = EmptyOperator(task_id="task2")
# task1 >> task2
