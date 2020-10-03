
# importando o módulo que faz conexão do python com o banco usando o postgresql e o pgadmin
import psycopg2

# Faz uma conexão já existente ou cria uma nova(outro banco)
dados = input('Deseja alterar os dados da conexão? (sim/não)')
if dados == 'sim':
    # nova conexão
    # dados do banco: nome do host, usuário, senha e banco de dados
    hostname = input('Escolha o hostname: ')
    username = input('Escolha o username: ')
    password = input('Escolha o password: ')
    database = input('Escolha o database: ')
    table = input('Escolha o table: ')

    # tentando uma conexão com base nas informações inseridas
    try:
        #conexão com o banco
        conn = psycopg2.connect(host=hostname ,user=username ,password=password ,dbname=database)
        cur = conn.cursor()
        print('Conectado com sucesso.')

        print("SGDB - Marcsoft Corporation")

        # fazendo uma busca no banco
        # faz uma busca geral com base nos campos q vc escolheu
        def select(conn):
            print("Busca")
            # excuta o comando de busca na linguagem sql
            cur.execute(f"SELECT * FROM {table}")
            print('='* 30)
            # fetchall extrai várias informações do banco
            for dado in cur.fetchall():
                print(dado)
            print('='* 30)
            print('Busca realizada co sucesso.')
                
        # fazendo alterações nos dados do banco
        def update(conn):
            print("Atualização")
            novaId = int(input('Qual a id? '))
            novoNome = input('Qual o nome do aluno?')
            novoCurso = input('Qual o nome do curso? ')
            # excuta o comando de atualização de dados na linguagem sql
            cur.execute(f"UPDATE {table} set nome = '{novoNome}', curso = '{novoCurso}' WHERE id = {novaId}")
            print('Atualização realizada co sucesso.')

        # inserindo dados no banco
        def insert(conn):
            print("Inserção")
            novaId = int(input('Qual a id do curso? '))
            novoNome = input('Qual o nome do aluno? ')
            novoCurso = input('Qual o nome do curso? ')
            # excuta o comando de inserção de dados na linguagem sql
            cur.execute(f"INSERT INTO {table} (id, nome, curso) VALUES ({novaId},'{novoNome}','{novoCurso}')")
            print('Inserção realizada co sucesso.')

        # deletando dados no banco tendo como base a id do conteúdo
        def delete(conn):
            print("Exclusão")
            novaId = int(input('Qual a id? '))
            # excuta o comando de inserção de dados na linguagem sql
            cur.execute(f"DELETE FROM {table} WHERE id = {novaId}")
            print('Exclusão realizada co sucesso.')

        msg = 'sim'

        while True:
            # Informe se deseja ou não executar mais comandos no programa
            if msg == 'sim':
                comando = input('Qual comando executar? (select, insert, delete, update) ')
                if comando == 'select':
                    select(conn)
                elif comando == 'insert':
                    insert(conn)
                elif comando == 'delete':
                    delete(conn)
                elif comando == 'update':
                    update(conn)
                else:
                    print('Valor incorreto. Escolha uma das opções da lista!')
                    continue
            elif msg == 'não':
                break
            else:
                print('Valor incorreto. Vc só pode escolher sim ou não!!')
            msg = input('Deseja efetuar outro comando? (sim/não) ')

    # exceção, algo não foi como o esperado. Verifique suas informações de conexão
    except (Exception, psycopg2.Error) as error :
        print ("Houve um erro na conexão com o banco.", error)

    # o psycopg2 guarda as informações
    # e só passa para o banco de dados se for feito um commit.
    # vc pode fazer alguns testes nesse módulo mesmo sem estar conectado ao banco
    finally:
        if(conn):
            # insere informações no banco
            conn.commit()
            # fecha a conexão
            conn.close()
            print("A conexão com o banco foi encerrada.")

else:
    # conexão padrão com o meu banco
    try:
        conn = psycopg2.connect(host='localhost' ,user='postgres' ,password='pgadmin' ,dbname='teste')
        cur = conn.cursor()
        print('Conectado com sucesso.')

        print("SGDB - Marcsoft Corporation")

        def select(conn) :
            print("Busca")
            cur.execute(f"SELECT * FROM alunos")
            print('='* 30)
            print("ID || Nome || Curso")
            for ID ,nome ,curso in cur.fetchall() :
                print(ID,' ||', nome,'||', curso)
            print('='* 30)
            print('Busca realizada co sucesso.')
                

        def update(conn):
            print("Atualização")
            novaId = int(input('Qual a id? '))
            novoNome = input('Qual o nome do aluno?')
            novoCurso = input('Qual o nome do curso? ')
            cur.execute(f"UPDATE alunos set nome = '{novoNome}', curso = '{novoCurso}' WHERE id = {novaId}")
            print('Atualização realizada co sucesso.')

        def insert(conn):
            print("Inserção")
            novaId = int(input('Qual a id do curso? '))
            novoNome = input('Qual o nome do aluno? ')
            novoCurso = input('Qual o nome do curso? ')
            cur.execute(f"INSERT INTO alunos (id, nome, curso) VALUES ({novaId},'{novoNome}','{novoCurso}')")
            print('Inserção realizada co sucesso.')

        def delete(conn):
            print("Exclusão")
            novaId = int(input('Qual a id? '))
            cur.execute(f"DELETE FROM alunos WHERE id = {novaId}")
            print('Exclusão realizada co sucesso.')

        msg = 'sim'

        while True:
            if msg == 'sim':
                comando = input('Qual comando executar? (select, insert, delete, update) ')
                if comando == 'select':
                    select(conn)
                elif comando == 'insert':
                    insert(conn)
                elif comando == 'delete':
                    delete(conn)
                elif comando == 'update':
                    update(conn)
                else:
                    print('Valor incorreto. Escolha uma das opções da lista!')
                    continue
            elif msg == 'não':
                break
            else:
                print('Valor incorreto. Vc só pode escolher sim ou não!!')
            msg = input('Deseja efetuar outro comando? (sim/não) ')

    except (Exception, psycopg2.Error) as error :
        print ("Houve um erro na conexão com o banco.", error)

    finally:
        if(conn):
            conn.commit()
            conn.close()
            print("A conexão com o banco foi encerrada.")


