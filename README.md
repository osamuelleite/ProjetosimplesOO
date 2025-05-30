# ProjetosimplesOO
Primeiro projeto de Orientação a objetos UnB-Prof Henrique

---------- USO DE CASO -----------
Ator: Médico
    - Cadastrar-se
    - Fazer login
    - Prescrever medicamento para paciente
    - Agendar consulta para paciente
    - Adicionar paciente para acompanhamento
    - Ver lista dos seus pacientes
    - Ver todos os pacientes do sistema

Ator: Paciente
    - Cadastrar-se
    - Fazer login
    - Ver médico responsável
    - Ver prescrições
    - Adicionar informações relevantes (sintomas, etc)
    - Ver consultas agendadas

Ator: Sistema
    - Validar login
    - Armazenar/recuperar dados em JSON

-------------- UML EM TEXTO  ----------------------


+---------------------+
|      Pessoa         |  <<abstract>>
+---------------------+
| - nome: str         |
+---------------------+
           ^
           |
+---------------------+         +----------------------+
|      Medico         |         |      Paciente        |
+---------------------+         +----------------------+
| - crm: str          |         | - email: str         |
| - especialidade: str|         | - data_nascimento: str|
| - pacientes: list   |         | - doenca: str        |
+---------------------+         | - medico_crm: str    |
                                | - prescricoes: list  |
                                | - info_extra: list   |
                                | - consultas: list    |
                                +----------------------+

+----------------------+
|     DataRecord       |
+----------------------+
| - login_path: str    |
| - users_path: str    |
+----------------------+
| +save_login(...)     |
| +check_login(...)    |
| +save_user(...)      |
| +load_user(...)      |
+----------------------+

+--------------------------+
|   MedicoController       |
+--------------------------+
| - data_record: DataRecord|
+--------------------------+
| +cadastrar_medico()      |
| +login_medico()          |
| +prescrever_medicamento()|
| +agendar_consulta()      |
| +adicionar_paciente()    |
| +listar_todos_pacientes()|
+--------------------------+

+----------------------------+
|   PacienteController       |
+----------------------------+
| - data_record: DataRecord  |
+----------------------------+
| +cadastrar_paciente()      |
| +login_paciente()          |
| +visualizar_prescricoes()  |
| +visualizar_medico_responsavel()|
| +adicionar_info_relevante()|
| +visualizar_consultas()    |
+----------------------------+
