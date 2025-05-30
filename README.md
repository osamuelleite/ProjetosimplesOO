# ProjetosimplesOO
Primeiro projeto de Orientação a objetos UnB-Prof Henrique


---------- resumo do sistema -----------------

O sistema “Med SYS” é uma aplicação de prontuário médico simples, desenvolvida em Python, que utiliza os princípios da programação orientada a objetos e segue boas práticas pythonicas. O sistema é totalmente operado via terminal, com menus claros e interface intuitiva, sem depender de bibliotecas gráficas externas.

Funcionalidades Principais
Cadastro e Login
Médicos podem se cadastrar informando nome, CRM, especialidade e senha.
Pacientes podem se cadastrar informando nome, e-mail, data de nascimento, doença e senha.
Login para médicos (via CRM) e pacientes (via e-mail).
Ações do Médico
Prescrever medicamentos para pacientes sob seu acompanhamento.
Agendar consultas para seus pacientes.
Adicionar pacientes já cadastrados à sua lista de acompanhamento.
Visualizar sua lista de pacientes.
Visualizar todos os pacientes cadastrados no sistema.
Ações do Paciente
Visualizar o médico responsável.
Visualizar prescrições recebidas.
Adicionar informações relevantes para o médico (ex: sintomas, mensagens).
Visualizar consultas agendadas.
Estrutura e Persistência
Orientação a Objetos:
O sistema é estruturado em classes como Pessoa (abstrata), Medico, Paciente, DataRecord (persistência), MedicoController e PacienteController.
Persistência em Arquivos:
Todos os dados de login e informações dos usuários são armazenados em arquivos JSON separados, garantindo fácil manutenção e portabilidade.
Organização Modular:
O código é dividido em módulos/pastas (models, controllers, utils, data), facilitando a manutenção e a expansão do sistema.
Interface
Menus Limpos:
O terminal é limpo automaticamente a cada troca de menu, deixando a navegação agradável e sem poluição visual.
Confirmação de Leitura:
Sempre que uma informação importante é exibida, o sistema aguarda o usuário pressionar ENTER antes de limpar a tela.
Público-Alvo
Ideal para uso didático, demonstração de conceitos de orientação a objetos, prototipagem de sistemas médicos simples ou para quem deseja um exemplo prático de CRUD em Python com interface de terminal.

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
