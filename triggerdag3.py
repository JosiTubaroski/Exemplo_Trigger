from airflow import DAG
from airflow.operators.bash import  BashOperator 
from pendulum import DateTime
from datetime import datetime

dag = DAG('triggerdag3', description= "Nossa triggerdag", schedule_interval=None,
          start_date=datetime(2024,1,15),catchup=False)


task1 = BashOperator(task_id="tsk1",bash_command="exit 1", dag=dag)
task2 = BashOperator(task_id="tsk2",bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3",bash_command="sleep 5", dag=dag,
                     trigger_rule = 'all_failed')

# Sequencia de execução das tasks

[task1, task2] >> task3