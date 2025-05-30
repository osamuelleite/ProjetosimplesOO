from models.pessoa import Medico
from models.data_record import DataRecord

class MedicoController:
    def __init__(self, data_record: DataRecord):
        self.data_record = data_record

    def cadastrar_medico(self):
        nome = input('Nome do médico: ')
        crm = input('CRM: ')
        especialidade = input('Especialidade: ')
        senha = input('Senha: ')
        medico = Medico(nome, crm, especialidade)
        self.data_record.save_login(crm, senha, 'medico')
        self.data_record.save_user(crm, {
            'nome': nome,
            'crm': crm,
            'especialidade': especialidade,
            'pacientes': []
        })
        print('Médico cadastrado com sucesso!')

    def login_medico(self):
        crm = input('CRM: ')
        senha = input('Senha: ')
        tipo = self.data_record.check_login(crm, senha)
        if tipo == 'medico':
            print('Login realizado com sucesso!')
            return crm
        else:
            print('CRM ou senha inválidos.')
            return None

    def prescrever_medicamento(self, crm):
        medico = self.data_record.load_user(crm)
        pacientes = medico.get('pacientes', [])
        if not pacientes:
            print('Nenhum paciente cadastrado para este médico.')
            return
        print('Pacientes:')
        for i, email in enumerate(pacientes, 1):
            print(f'{i}. {email}')
        idx = input('Escolha o número do paciente para prescrever: ')
        try:
            idx = int(idx) - 1
            if idx < 0 or idx >= len(pacientes):
                print('Opção inválida.')
                return
        except ValueError:
            print('Opção inválida.')
            return
        email = pacientes[idx]
        medicamento = input('Digite o nome do medicamento: ')
        paciente = self.data_record.load_user(email)
        paciente.setdefault('prescricoes', []).append(medicamento)
        self.data_record.save_user(email, paciente)
        print('Medicamento prescrito com sucesso!')
        input('\nPressione ENTER para continuar...')

    def agendar_consulta(self, crm):
        medico = self.data_record.load_user(crm)
        pacientes = medico.get('pacientes', [])
        if not pacientes:
            print('Nenhum paciente cadastrado para este médico.')
            return
        print('Pacientes:')
        for i, email in enumerate(pacientes, 1):
            print(f'{i}. {email}')
        idx = input('Escolha o número do paciente para agendar consulta: ')
        try:
            idx = int(idx) - 1
            if idx < 0 or idx >= len(pacientes):
                print('Opção inválida.')
                return
        except ValueError:
            print('Opção inválida.')
            return
        email = pacientes[idx]
        data = input('Digite a data da consulta (ex: 01/07/2025): ')
        paciente = self.data_record.load_user(email)
        paciente.setdefault('consultas', []).append({'data': data, 'medico_crm': crm})
        self.data_record.save_user(email, paciente)
        print('Consulta agendada com sucesso!')
        input('\nPressione ENTER para continuar...')

    def adicionar_paciente(self, crm):
        email = input('Digite o email do paciente já cadastrado: ')
        paciente = self.data_record.load_user(email)
        if not paciente:
            print('Paciente não encontrado.')
            return
        medico = self.data_record.load_user(crm)
        if email in medico.get('pacientes', []):
            print('Paciente já está na lista deste médico.')
            return
        medico.setdefault('pacientes', []).append(email)
        self.data_record.save_user(crm, medico)
        paciente['medico_crm'] = crm
        self.data_record.save_user(email, paciente)
        print('Paciente adicionado para acompanhamento!')
        input('\nPressione ENTER para continuar...')

    def listar_todos_pacientes(self):
        users = self.data_record._load_json(self.data_record.users_path)
        print('Lista de todos os pacientes cadastrados:')
        for key, data in users.items():
            if 'email' in data:
                print(f"Nome: {data['nome']}, Email: {data['email']}, Doença: {data['doenca']}")
        input('\nPressione ENTER para continuar...')
