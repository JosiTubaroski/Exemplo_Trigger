# Exemplo Trigger

1) Definindo que para a execução da task3, uma das execuções anteriores deve falhar.

<img src="https://github.com/JosiTubaroski/Exemplo_Trigger/blob/main/img/trigger_one.png">

Ao executar a dag, as 2 primeiras tasks foram executadas com sucesso e a ultima foi pulada 'skipped'

<img src="https://github.com/JosiTubaroski/Exemplo_Trigger/blob/main/img/Task3_Skipped.png">

2) Segundo exemplo de Trigger

Forçando uma falha na task1, para então verificar a execução da task3.

<img src="https://github.com/JosiTubaroski/Exemplo_Trigger/blob/main/img/codigo_task2.png">

Resultado da execução

<img src="https://github.com/JosiTubaroski/Exemplo_Trigger/blob/main/img/Result_Exc.png">




