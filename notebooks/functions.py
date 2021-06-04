from io import StringIO
import pandas as pd
import seaborn as sns
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

###Seção de funções adicionais para processamento
	
def abreviacao_estados(abreviacao: str):
    estados = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins'
    }
    
    return estados[abreviacao]
	
def regiao_estados(estado: str):
    regiao = {
        'Acre' : 'Norte',
        'Alagoas' : 'Nordeste',
        'Amapá' : 'Norte',
        'Amazonas' : 'Norte',
        'Bahia' : 'Nordeste',
        'Ceará' : 'Nordeste',
        'Distrito Federal' : 'Centro-Oeste',
        'Espírito Santo' : 'Sudeste',
        'Goiás' : 'Centro-Oeste',
        'Maranhão' : 'Nordeste',
        'Mato Grosso' : 'Centro-Oeste',
        'Mato Grosso do Sul' : 'Centro-Oeste',
        'Minas Gerais' : 'Sudeste',
        'Pará' : 'Norte',
        'Paraíba' : 'Nordeste',
        'Paraná' : 'Sul',
        'Pernambuco' : 'Nordeste',
        'Piauí' : 'Nordeste',
        'Rio de Janeiro' : 'Sudeste',
        'Rio Grande do Norte' : 'Nordeste',
        'Rio Grande do Sul' : 'Sul',
        'Rondônia' : 'Norte',
        'Roraima' : 'Norte',
        'Santa Catarina' : 'Sul',
        'São Paulo' : 'Sudeste',
        'Sergipe' : 'Nordeste',
        'Tocantins' : 'Norte'
    }
    
    return regiao[estado]
	
def add_estado_regiao(df):
    coluna_regiao=[] #criando uma lista para registrar os valores das regiões em relação aos estados
    coluna_estado=[] #criando uma lista para registrar os valores dos estados sem o identificador número que contém no indíce

    regioes=['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'] #criando uma lista com as regiões pré-definidas

    for linha in df.iterrows(): #aqui iniciamos um loop for que vai percorrer todas as linhas do "df_aih_aprovadas" 
                                        #para pegar a "Unidade da Federação"(os valores dos estados) e fazer as validações
                                        #porém aqui a gente podia usar qualquer um dos dataframes, dado que todos estão ordenados pela Unidade da Federação
    
        estado=linha[1]["uf"] #criamos uma variável "estado" para pegar o valor de cada estado, que é o indice 0 de cada linha
        id_regiao = int(estado.split(' ')[0]) #aqui pegamos o identificador da região, que no caso são os numeros antes do nome do estado
        estado_sem_id = estado.split(' ', maxsplit = 1)[1] #aqui pegamos apenas o nome do estado
        
        coluna_estado.append(estado_sem_id) #adicionando os estados à lista coluna_estado
        
        #aqui verificamos cada id e adicionamos à coluna_regiao o valor referente da região do estado
        if id_regiao < 20:
            coluna_regiao.append(regioes[0])
        elif id_regiao < 30:
            coluna_regiao.append(regioes[1])
        elif id_regiao < 40:
            coluna_regiao.append(regioes[2])
        elif id_regiao < 50:
            coluna_regiao.append(regioes[3])
        else:
            coluna_regiao.append(regioes[4])
        
    #adicionamos os valores de coluna_regiao para cada dataframe
    df["regiao"] = coluna_regiao
    
    #adicionamos os valores da coluna_estado para cada dataframe
    df["estado"] = coluna_estado
	
def desnormalizar(df, indice):
	df = df.reset_index()
	del df[indice]
	return df




###seção para carregamento de dados
def loading_tabela_cobertura_imunobiologicos():
    cobertura_imunobiologicos = """Imunobiológico	Período (a partir de)	População-alvo	Cobertura com:
    BCG (BCG)	1994	< 1 ano	1ª dose
    Contra Febre Amarela (FA)	1994	< 1 ano	1ª dose
    Contra Haemophilus influenzae tipo b (Hib)(a)	2000 a 2002	< 1 ano	3ª dose
    Contra Hepatite B (HB)	1994	< 1 ano	3ª dose
    Contra Influenza (campanha) (INF)	1999	65 anos e mais (1999)	Dose única
    Contra Influenza (campanha) (INF)	1999	60 anos e mais (a partir de 2000)	Dose única
    Contra Sarampo(b)	1994 a 2002	< 1 ano	Dose única
    Dupla Viral (SR)	2001 a 2004	1 ano(3)	Dose única
    Oral contra poliomielite (VOP)	1994	< 1 ano	3ª dose
    Oral Contra Poliomielite (1ª etapa) (VOP)	1994	até 1999: < 1 ano	Dose única
    Oral Contra Poliomielite (1ª etapa) (VOP)	2000	de 0 a 4 anos(4)	Dose única
    Oral Contra Poliomielite (2ª etapa) (VOP)	1994	até 1999: < 1 ano	Dose única
    Oral Contra Poliomielite (2ª etapa) (VOP)	2000	de 0 a 4 anos(4)	Dose única
    Oral de Rotavírus Humano (RR)	2006	< 1 ano (6 a 24 semanas de vida)	2ª dose
    Tetravalente (DTP/Hib) (TETRA)	2002	< 1 ano	3ª dose
    Tríplice Viral (SCR)	2000	1 ano	1ª dose
    Tríplice Viral (campanha) (SCR)	2004	1 ano(3)	1ª dose"""

    cobertura_imunobiologicos_io = StringIO(cobertura_imunobiologicos)

    df_cobertura_imunobiologicos = pd.read_csv(cobertura_imunobiologicos_io, sep="\t", engine="python")
    df_cobertura_imunobiologicos = df_cobertura_imunobiologicos.set_index("Imunobiológico")
    return df_cobertura_imunobiologicos
	
def loading_cobertura_vacinais_ano_unidade_federacao_1994_2019():
    df_cobertura_vacinais_ano_uf_1994_2019 = pd.read_csv("../datasets/Cobertura_Vacinais_Ano_Unidade_Federacao_1994_2019.csv", 
                                                     sep=";",skiprows=3, skipfooter=20, 
                                                     decimal=",",thousands=".",
                                                    encoding="ISO-8859-1",
                                                     engine="python")
    return df_cobertura_vacinais_ano_uf_1994_2019
	
def loading_tuberculose_ano_uf_confirmados():
    df_tuberculo_confirmados = pd.read_csv("../datasets/Tuberculose_Ano_UF_Confirmados.csv",
                                      sep=";", skiprows=3, skipfooter=19,
                                      decimal=",",thousands=".",
                                      encoding="ISO-8859-1",
                                      engine="python")
    return df_tuberculo_confirmados
	
	

	
###seção para processamento de dados
def processing_cobertura_vacinais_ano_unidade_federacao_1994_2019():
	df_cobertura_vacinais_ano_uf_1994_2019 = loading_cobertura_vacinais_ano_unidade_federacao_1994_2019() #carregando o dataset
	
	del df_cobertura_vacinais_ano_uf_1994_2019["Total"] #deletando coluna total
	
	
	#setando index
	df_cobertura_vacinais_ano_uf_1994_2019 = df_cobertura_vacinais_ano_uf_1994_2019.set_index("Unidade da Federação")
	
	return df_cobertura_vacinais_ano_uf_1994_2019

	
def processing_tuberculose_ano_uf_confirmados():

    df_casos_tuberculose_confirmados = loading_tuberculose_ano_uf_confirmados() #carregando o dataset
	
	#setando index
    df_casos_tuberculose_confirmados = df_casos_tuberculose_confirmados.set_index("Ano Diagnóstico") 
	
    del df_casos_tuberculose_confirmados["Total"] #deletando coluna total
    del df_casos_tuberculose_confirmados["IG"] #deleta coluna "extra"
	
	#mapeia os nomes de estados com base nas abreviações
    df_casos_tuberculose_confirmados.columns = df_casos_tuberculose_confirmados.columns.map(abreviacao_estados) 
	
    return df_casos_tuberculose_confirmados
	

##seção para processamento de todos os dados

def all_data_processing():
    #puxamos os dados tratados pela função de processamento
    df_cobertura_vacinais = processing_cobertura_vacinais_ano_unidade_federacao_1994_2019() 
    df_casos_tuberculose_confirmados = processing_tuberculose_ano_uf_confirmados()
    
    #aplicamos a função "melt" do python para desnormalizar os dados
    df_cobertura_vacinais_aberto = df_cobertura_vacinais.reset_index().melt(id_vars=["Unidade da Federação"], value_vars=df_cobertura_vacinais.columns)
    df_casos_tuberculose_confirmados_aberto = df_casos_tuberculose_confirmados.reset_index().melt(id_vars=["Ano Diagnóstico"], value_vars=df_casos_tuberculose_confirmados.columns)
    
    #ajustando os nomes das colunas
    df_cobertura_vacinais_aberto.columns = ["uf", "ano", "cobertura"]
    df_casos_tuberculose_confirmados_aberto.columns = ["ano", "estado", "casos"]
    
    #adicionando região e estado
    add_estado_regiao(df_cobertura_vacinais_aberto)
    df_casos_tuberculose_confirmados_aberto["regiao"] = df_casos_tuberculose_confirmados_aberto["estado"].map(regiao_estados)
    
    #removendo o uf, pois já separamos a uf em regiao e estado
    del df_cobertura_vacinais_aberto["uf"]
    
    #ajustando o tipo do ano
    df_cobertura_vacinais_aberto["ano"] = df_cobertura_vacinais_aberto["ano"].astype(str).astype("datetime64[ns]")
    df_casos_tuberculose_confirmados_aberto["ano"] = df_casos_tuberculose_confirmados_aberto["ano"].astype(str).astype("datetime64[ns]")
    
    #ajustando outros tipos numericos
    df_cobertura_vacinais_aberto["cobertura"] = df_cobertura_vacinais_aberto["cobertura"].astype(float)
    df_casos_tuberculose_confirmados_aberto["casos"] = df_casos_tuberculose_confirmados_aberto["casos"].astype(int)
    
    return df_cobertura_vacinais_aberto, df_casos_tuberculose_confirmados_aberto

## seção para definir funções de gráficos
def grafico_cobertura_vacinais_casos_confirmados(estado: str, paleta_cobertura: str, paleta_casos: str):
    df_cobertura_vacinais, df_casos_tuberculose = all_data_processing()

    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(data=df_cobertura_vacinais.query("estado == '" + estado + "' and ano > 2001 and ano <= 2019"), y="cobertura",
                      x="ano", hue="estado", palette=paleta_cobertura)

    plt.xticks(rotation=30)
    plt.ylim(0, 120)
    ax.set_title("Cobertura vacinais - " + estado)
    ax.set_xlabel('Anos')
    ax.set_ylabel('% de cobertura')
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}%"))
    ax.get_legend().remove()
    plt.grid(True, linestyle="--")



    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(data=df_casos_tuberculose.query("estado == '" + estado + "' and ano > 2001 and ano <= 2019"), y="casos", x="ano",
                      hue="estado", palette=paleta_casos)

    plt.xticks(rotation=30)
    ax.set_title("Casos confirmados de tuberculose - " + estado)
    ax.set_xlabel('Anos')
    ax.set_ylabel('Número de casos absolutos')
    ax.get_legend().remove()
    plt.grid(True, linestyle="--")


    plt.show()