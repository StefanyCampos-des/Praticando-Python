from datetime import datetime  # Importa módulo para lidar com datas e horas

def linha(tam=50): #linhas
    print('-=' *30) 

def calcular_idade(ano_nascimento):
    # Calcula a idade atual
    return datetime.now().year - ano_nascimento

def calcular_tempo_contribuicao(ano_contratacao):
    # Calcula o tempo de contribuição 
    return datetime.now().year - ano_contratacao

def calcular_anos_para_aposentar(tempo_contribuicao, sexo):
    # Define o tempo necessário para aposentadoria, diferente para homem e mulher
    if sexo.lower() == 'f':
        tempo_necessario = 30
    else:
        tempo_necessario = 35

    # Calcula o tempo restante para atingir o tempo necessário, nunca negativo
    restante = tempo_necessario - tempo_contribuicao
    return max(restante, 0)

def coletar_dados():
    # Coleta dados do usuário via input e faz tratamento básico de erros
    dados = {}

    dados['nome'] = input("Nome completo: ").strip()  # Remove espaços extras
    dados['sexo'] = input("Sexo (M/F): ").strip().lower()  # Padroniza para minusculo

    try:
        dados['ano_nascimento'] = int(input("Ano de nascimento: "))
        dados['ano_contratacao'] = int(input("Ano da 1ª contratação: "))
        dados['registro'] = str(input('Esta trabalhando atualmente? (S/N): ')).strip().lower()
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return None  # Sai da função 

    return dados

def mostrar_resultado(dados):
    # Calcula e imprime o resultado da simulação com base nos dados coletados
    idade = calcular_idade(dados['ano_nascimento'])
    tempo_contrib = calcular_tempo_contribuicao(dados['ano_contratacao'])
    anos_faltando = calcular_anos_para_aposentar(tempo_contrib, dados['sexo'])

    linha()  
    print("\n🧾 Resultado da simulação:")
    print(f"Nome: {dados['nome'].title()}")
    print(f"Idade atual: {idade} anos")
    print(f"Tempo de contribuição: {tempo_contrib} anos")
    print(f"⏳ Faltam {anos_faltando} anos para aposentadoria.")
    print("\n📌 Observação: O tempo real de contribuição pode variar conforme vínculos anteriores em outras empresas e registros no INSS.")
    linha()  

def main():
    # controla o fluxo do programa
    dados_usuario = coletar_dados()  # Recebe dados do usuário
    if dados_usuario:                 # Se dados forem válidos, mostra resultado
        mostrar_resultado(dados_usuario)

if __name__ == "__main__":
    # Garante que o programa só execute o main se for o script principal rodando
    main()
