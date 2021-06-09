---
# Projeto: Vacinas Salvam Vidas
## Uma análise da eficácia do Programa Nacional de Imunizações (PNI) e uma breve solução para o negacionismo do movimento antivacina


<p align="center">
  <img alt="Na imagem animada, temos uma mão aplicando uma vacina de conhecimento para combater as fakenews" src="images/Vacina_contra_Fakenews.gif" />
 </p>

---
## 👉 Visão geral do projeto:

 - Objetivo do projeto
 - Introdução
    - O movimento antivacina
    - Por que o SUS é importante?
        - Programa Nacional de Imunizações (PNI)
    - Dados públicos
        - Tabnet e o DataSUS
 - Importação de bibliotecas
 - Nota técnica e Origem dos dados
 - Carregamento e Processamento dos dados
 - Levantamento de Hipóteses
 - Visualização dos dados
 - Pesquisa complementar
 - Conclusão
 - Referências
 
 Acesse o projeto:
 
 - Notebook: [Projeto_VacinasSalvamVidas.ipynb](https://github.com/aureliowozhiak/Projeto_VacinasSalvamVidas/blob/main/notebooks/Projeto_VacinasSalvamVidas.ipynb)
  
 ---
 
## Objetivo do projeto

O principal objetivo desse projeto é fazer uma análise da eficâcia do Programa Nacional de Imunizações (PNI) mostrando que vacinas podem sim reduzir o número de mortes relacionadas à determinadas doenças. 

Nesse projeto também será abordado conceitos sobre o negacionismo do movimento antivacina e uma proposta de solução para evitar a disseminação do maior virus da atualidade: as fake news!

---

## ⭐ Introdução

---
### 🚫 O movimento antivacina

Segundo um relatório da OMS, divulgado em 2019, o movimento antivacina é considerado um dos maiores problemas a saúde global. Esse movimento vai contra todo o avançado cientifico alcançado no combate as doenças letais que podem ser evitadas, ou reduzidas, com o Programa de Imunização Nacional.

<p align="center">
  <img alt="Um homem levanta cartaz contra a vacina Coronavac, do laboratório chinês Sinovac, durante manifestação em São Paulo." src="images/vacinas_nao.jpg" />
<br/>foto por: AMANDA PEROBELLI / REUTERS </p>

<br>

Muitas são as razões que uma pessoa pode ter para não se vacinar ou para não levarem seus filhos para a vacinação, um desses motivos é a falta ou dificuldade de acesso, em determinadas regiões sociogeográficas. Entretando, a falta de confiança nas vacinas vem crescendo devido esse movimento negacionista, que por muitas das vezes diz que ou a vacina não funciona, ou é uma forma do governo eliminar determinados grupos sociais ou até mesmo alegando que o governo irá implantar uma espécie de "chip" que irá controlar ou rastear essas pessoas, afirmações que chegam a ser ridiculas dado todo o avanço e beneficio que iremos discutir ao longo do desenvolvimento desse projeto.

---

### 👍 Por que o SUS é importante?

O SUS (Sistema Único de Saúde) dá o direito à saúde para qualquer cidadão brasileiro, oferecendo acesso integral, universal e gratuito a serviços de saúde.

Paralelamente à realização de consultas, exames e internações, o SUS também promove campanhas de vacinação e ações de prevenção de vigilância sanitária, como fiscalização de alimentos e registro de medicamentos.

<p align="center">
  <img alt="Gif animado do personagem Mr.Bean vestido de médico mostrando o dedo polegar, dando um sinal de 'positivo' e sorrindo. Com o texto 'Good Job!!!' na legenda" src="images/mrbean.gif" />
</p>

E apesar de alguns problemas nas questões de distribuição de verba pública pelo governo, o SUS é responsável por disponibilizar, gerenciar e distribuir diversas doses de vacinas anualmente para população alvo de forma completamente gratuita. 

#### 💉 Programa Nacional de Imunizações (PNI)

O Programa Nacional de Imunizações (PNI) é uma ação do Governo Federal e que tem por objetivo eliminar, por meio da vacinação em massa da população, uma série de doenças. Como resultado, entre os casos de sucesso estão a erradicação da varíola e da poliomielite do territorio nacional.

Por meio desse programa, toda a população brasileira tem acesso às vacinas recomendadas pela Organização Mundial de Saúde (OMS).

O PNI tem como objetivos a inclusão social, ao permitir que qualquer cidadão tenha acesso às imunizações.

---

### 🎲 Dados públicos

Dados públicos são dados que estão disponíveis para qualquer pessoa acessar, esses dados não tem nenhum tipo de controle ou privação de acesso.
São dados públicos, geralmente dados que toda população deve ou pode ter acesso, como por exemplo, dados que indicam os gastos de parlamentares com o dinheiro público (dinheiro que provem de impostos de forma direta ou indireta).

#### 📊 Tabnet e o DataSUS

"O aplicativo TABNET é um tabulador genérico de domínio público que permite organizar dados de forma rápida conforme a consulta que se deseja tabular. Foi desenvolvido pelo DATASUS para gerar informações das bases de dados do Sistema Único de Saúde." <sub><sup>[http://www2.datasus.gov.br/DATASUS/APRESENTACAO/TABNET/Tutorial_tabNet_FINAL.pptx_html/html/index.html#2](http://www2.datasus.gov.br/DATASUS/APRESENTACAO/TABNET/Tutorial_tabNet_FINAL.pptx_html/html/index.html#2)</sup></sub>

"O DATASUS disponibiliza informações que podem servir para subsidiar  análises objetivas da situação sanitária, tomadas de decisão baseadas em evidências e elaboração de programas de ações de saúde.

A mensuração do estado de saúde da população é uma tradição em saúde pública. Teve seu início com o registro sistemático de dados de mortalidade e de sobrevivência (Estatísticas Vitais - Mortalidade e Nascidos Vivos). Com os avanços no controle das doenças infecciosas (informações Epidemiológicas e Morbidade) e com a melhor compreensão do conceito de saúde e de seus determinantes populacionais, a análise da situação sanitária passou a incorporar outras dimensões do estado de saúde.

Dados de morbidade, incapacidade, acesso a serviços, qualidade da atenção, condições de vida e fatores ambientais passaram a ser métricas utilizadas na construção de Indicadores de Saúde, que se traduzem em informação relevante para a quantificação e a avaliação das informações em saúde." <sub><sup>[http://www2.datasus.gov.br/DATASUS/index.php?area=02](http://www2.datasus.gov.br/DATASUS/index.php?area=02)</sup></sub>
---
## 📝 Nota técnica e Origem dos dados

Os dados relacionados a cobertura vacinal nesse projeto, são oriundos do [Sistema de Avaliação do Programa de Imunizações - API](http://pni.datasus.gov.br/), sistema este gerido pela Coordenação Geral do Programa Nacional de Imunizações - CGPNI, do Departamento de Vigilância Epidemiológica, Secretaria de Vigilância em Saúde, do Ministério da Saúde, em conjunto com as Secretarias Estaduais de Saúde, suas regionais e as Secretarias Municipais de Saúde.

As Secretarias Municipais de Saúde coletam, por meio do Boletim Diário de Doses Aplicadas de Vacinas, os quantitativos de indivíduos vacinados por faixa etária em cada Estabelecimento de Saúde (salas de vacina), consolidando essas informações nos
Boletins Mensais, com registro no Sistema API em todas as instâncias.

A base de dados estadual é enviada mensalmente para a CGPNI/DEVEP/SVS/MS, quando então é consolidada a base nacional.
<br/><sup><sub>Nota técnica completa em: [http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf](http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf) ou, caso o link chegue a ficar offline futuramente, ficará disponível localmente: [technical_notes/Imun_cobertura_desde_1994.pdf](technical_notes/Imun_cobertura_desde_1994.pdf)</sub></sup>

Esses dados foram coletados no [Tabnet do PNI](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def), aplicando os seguintes filtros:
 - Linha: Ano
 - Coluna: Unidade da Federação
 - Conteúdo: Coberturas Vacinais
 - Período disponíveis: 1994 - 2019

Com isso, foi obitido a seguinte coleção de dados (dataset) em CSV, que se encontra nesse projeto em [datasets/Cobertura_Vacinais_Ano_Unidade_Federacao_1994_2019.csv](datasets/Cobertura_Vacinais_Ano_Unidade_Federacao_1994_2019.csv)

Esses dados coletados são referentes à seguinte tabela de Imunobiológicos com determinada Cobertura:
<br/><sup><sub>Descrição das variáveis disponíveis para tabulação: [http://tabnet.datasus.gov.br/cgi/pni/%5Ccpnidescr.htm](http://tabnet.datasus.gov.br/cgi/pni/%5Ccpnidescr.htm)</sub></sup>
 
 <p align="center">
  <img alt="Tabela que mostra a cobertura dos imunobiológicos, disponibilizada no link mencionado anteriormente"  src="images/tabela_cobertura_imunobiologicos.png" />
</p>
 
 Além disso, também vamos utilizar os dados relacionados aos diagnósticos de Tuberculose disponibilizados no [Tabnet do DataSUS de Tuberculose](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/tubercbr.def), aplicando os seguintes filtros:
 - Linha: Ano Diagnóstico
 - Coluna: UF de notificação
 - Conteúdo: Casos confirmados
 - Período disponíveis: 2001 - 2019

Com isso, foi obitido a seguinte coleção de dados (dataset) em CSV, que se encontra nesse projeto em [datasets/Tuberculose_Ano_UF_Confirmados.csv](datasets/Tuberculose_Ano_UF_Confirmados.csv)
 
 ---
## 👨‍💻 Carregamento e Processamento dos dados

Vamos fazer todo o carregamento e processamento dos dados utilizando o arquivo [notebooks/functions.py](notebooks/functions.py). <br/>
Esse arquivo está separado em seções, sendo elas:
 - Seção de funções adicionais para o processamento (mapeamento de dados e inserção de informações)
 - Seção para definir funções de carregamento das bases de dados (read_csv e primeira tratativa dos datasets)
 - Seção para definir funções de processamento das bases de dados (manipulações dos dados e exclusão de dado lixo)
 - Seção para processamento de todos os dados (aplicação da desnormalização, mapeamento e ajustes finais)
 - Além disso, temos uma seção para definição de funções para gerar gráficos
 
Com essas funções definidas, básicamente o que precisa ser feito aqui, é chamar a função "all_data_processing" e salvar os valores dos dataframes para efetuar as plotagem dos gráficos.
 
---
## 🤔 Levantamento de Hipóteses

Irei deixar aqui, algumas suposições sobre o que acredito que possa acontecer quando efetuarmos a relação entre Cobertura vacinal e a quantidade absoluta de casos confirmados de tuberculose por estado.

<p align="center">
  <img alt="Homer Simpson se balançando pra trás em uma cadeira, com uma perna cruzada em cima da outra, colocando a mão no queixo e fazendo cara de pensativo" src="images/homer_hipotese.gif" />
</p>

⚠️ Deixo aqui também a observação que são só suposições e hipoteses, ou seja, não significa que de fato isso será confirmado ou comprovado, afinal, no mundo real existem diversas variáveis, e analisar a correlação entre Cobertura vacinal e quantidade absoluta de casos confirmados, é apenas uma estimativa que até nos dá uma noção macro do cenário, mas não especifica ou leva em conta outros fatores externos.

 - Com o inicio das campanhas de vacinação, provavelmente haverá alguma redução no número absoluto de casos confirmados de tuberculose;
 
 
 - Caso haja algum tipo de queda na proporção de vacinas aplicadas, o impacto no número absoluto de casos não necessariamente será imediato, visto que o desenvolvimento da doença pode levar um certo período, e temos que levar em conta também em que momento a pessoa foi exposta;
 
 
---
## 📍 Conclusão

Antes de "bater o martelo" em nossas conclusões, vamos verificar se nossas hipoteses iniciais fazem algum sentido!

 - <u><i>Com o inicio das campanhas de vacinação, provavelmente haverá alguma redução no número absoluto de casos confirmados de tuberculose:</i></u> Realmente, após o inicio da campanha de vacinação houve essa redução no número absoluto de casos confirmados de tuberculose;
 
 - <u><i>Caso haja algum tipo de queda na proporção de vacinas aplicadas, o impacto no número absoluto de casos não necessariamente será imediato, visto que o desenvolvimento da doença pode levar um certo período, e temos que levar em conta também em que momento a pessoa foi exposta:</i></u> Verifcamos em diversos momentos que quase sempre que houve uma queda na porcentagem da cobertura vacinal, houve um reflexo no número de casos absolutos após um certo período;
 
  <p align="center">
  <img alt="Desenho animado, Bob esponja batendo as mãos e retirando poeira delas com um sorisso e olhos fechados"  src="images/bob_fim.gif" />
</p>

Com essas hipoteses verificadas e com nossa pesquisa complementar feita, podemos assumir que sim, as vacinas tem um impacto bem grande na redução de casos confirmados de tuberculose, mas além disso, podemos supor com uma certa segurança que as vacinas, de modo geral, ajudam na redução da disseminação de diversos virus pelo mundo todo, o que por consequência salva diversas vidas de doenças graves.


 ##### Informações gerais:

DATASUS: <[http://www2.datasus.gov.br/DATASUS/index.php?area=02](http://www2.datasus.gov.br/DATASUS/index.php?area=02)>

Sistema de Informações do PNI: <[http://pni.datasus.gov.br/](http://pni.datasus.gov.br/)>

Imunizações Cobertura – desde 1994 - Notas Técnicas: <[http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf](http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf) e [http://tabnet.datasus.gov.br/cgi/pni/%5Ccpnidescr.htm](http://tabnet.datasus.gov.br/cgi/pni/%5Ccpnidescr.htm)>

Tutorial TABNET: <[http://www2.datasus.gov.br/DATASUS/APRESENTACAO/TABNET/Tutorial_tabNet_FINAL.pptx_html/html/index.html#2](http://www2.datasus.gov.br/DATASUS/APRESENTACAO/TABNET/Tutorial_tabNet_FINAL.pptx_html/html/index.html#2)>

##### Origem dos dados:

TABNET Imunizações: <[http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def)>

TABNET Tuberculose: <[http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/tubercbr.def](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/tubercbr.def)>
