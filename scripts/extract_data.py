import mysql.connector
import csv
import os

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='db_mysql',
            database='trabalho2',
            user='root',
            password='valdas',
            port='3306'
        )
        if connection.is_connected():
            print("Conectado ao MySQL")
            return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def extract_data(query, output_file):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [i[0] for i in cursor.description]

        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)
        
        cursor.close()
        connection.close()
        print(f"Dados extraídos para {output_file}")

if __name__ == "__main__":
    queries = {
        'produtos': """
            SELECT id, descricao, quantidade, unidade_medida, preco_custo, preco_venda, criado_em, atualizado_em 
            FROM produtos;
        """,
        'movimentacoes_itens': """
            SELECT id, movimentacao_id, produto_id, quantidade, preco_custo, preco_venda, criado_em
            FROM movimentacoes_itens;
        """,
        'movimentacoes': """
            SELECT id, funcionario_id, cliente_fornecedor_id, tipo_movimentacao, criado_em 
            FROM movimentacoes;
        """,
        'auditorias': """
            SELECT id, auditoria, tabela, usuario, criado_em 
            FROM auditorias;
        """,
        'cargos': """
            SELECT id, descricao, criado_em 
            FROM cargos;
        """,
        'clientes_fornecedores': """
            SELECT id, razao_social, nome_fantasia, data_nascimento, cnpj_cpf, criado_em, atualizado_em 
            FROM clientes_fornecedores;
        """,
        'funcionarios': """
            SELECT id, nome, cpf, data_nascimento, data_admissao, data_demissao, cargo_id, salario_base 
            FROM funcionarios;
        """,
        'setores': """
            SELECT id, setor, responsavel_id, criado_em, atualizado_em 
            FROM setores;
        """,
        'setores_funcionarios': """
            SELECT id, setor_id, funcionario_id, criado_em 
            FROM setores_funcionarios;
        """
    }
    output_dir = '../data/extracted/'
    os.makedirs(output_dir, exist_ok=True)

    for name, query in queries.items():
        output_file = os.path.join(output_dir, f"{name}.csv")
        extract_data(query, output_file)
