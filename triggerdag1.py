from airflow import DAG
from airflow.operators.bash import  BashOperator 
from pendulum import DateTime
from datetime import datetime

dag = DAG('triggerdag1', description= "Nossa triggerdag1", schedule_interval=None,
          start_date=datetime(2024,1,15),catchup=False)


task1 = BashOperator(task_id="tsk1",bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="tsk2",bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="tsk3",bash_command="sleep 5", dag=dag,
                     trigger_rule = 'one_failed')

# Sequencia de execução das tasks

[task1, task2] >> task3