# TPC5 - Aula 6

## Pergunta P1.1	
Pseudonimização consiste no processamento de dados pessoais de maneira a que estes não possam ser associados a um indivíduo (specific data subject) sem o uso de informação adicional.

Com esta definição em mente existem duas propriedades que devem ser asseguradas pela técnica de pseudonimização:
- D1 - Não deve ser fácil obter os identificadores iniciais a partir dos pseudónimos num contexto de processamento de dados específico;
- D2 - Não deve ser trivial para qualquer terceiro (qualquer um exceto o processador e controlador) reproduzir os pseudónimos (para evitar a utilização dos mesmos pseudónimos em diferentes domínios e evitar associações entre domínios). 

### Hashing without key

Esta técnica usa uma função de hash criptográfica para derivar pseudónimos de tamanho fixo. Esta função hash é determinística, o que significa que para um dado input m o output gerado será sempre igual. Por esta razão as propriedade D1 e D2 não são asseguradas, pois é trivial, para um terceiro, verificar se um pseudónimo corresponde a um identificador (fazendo o hashing do identificador), violando D1, e se dois terceiros utilizarem a mesma função hash obtém o mesmo pseudónimo, violando D2.

Isto significa que hashing sem utilização de chaves é uma forma de pseudonimização fraca pois é possível descobrir os pseudónimos a partir de uma lista de possíveis identificadores, sem necessidade de qualquer informação adicional.

### Hashing with key or salt

Esta técnica usa uma função de hash que gera o output consoante o input e uma chave secreta. Assim é possível gerar pseudónimos diferentes para um mesmo identificador, dependendo da escolha de chave - o que satisfaz a propriedade D2. A propriedade D1 também é satisfeita desde que nenhum terceiro (para além do controlador e processador) tenha acesso à chave secreta. Caso seja necessário usar o mesmo pseudónimo para um indivíduo então deve ser utilizada a mesma chave. Esta técnica pode ser também utilizada se fôr preciso fazer ‘tracking’ de indivíduos sem guardar identificadores. Por último, se as chaves forem destruídas então os dados poderão ser anonimizados, pois deixa de haver uma associação entre os identificadores e os pseudónimos.

Para além desta abordagem existe outra em que é utilizada uma função de hash que não necessita de chave, e em vez da chave é utilizado um salt - informação aleatória que é adicionada ao input. De forma simplificada pode ser dito que esta abordagem apresenta mesmas propriedades enunciadas anteriormente em relação ao hashing com chave. No entanto existem alguns senãos que não estão presentes no hashing com chave: salts não apresentam o mesmo grau de imprevisibilidade que chaves secretas e uma salted hash function é geralmente considerada criptograficamente mais fraca que uma keyed hash function. No entanto existem técnicas criptograficamente fortes para gerar salted hashes; Como salts são geralmente guardados juntamente com o valor hash gerado deve ser considerado o uso de peppers (que são salts secretos que não são guardados com o output).

### Encryption as a pseudonymisaton technique

#### Encriptação Simétrica

É usada uma cifra simétrica para obter pseudónimos. É uma técnica facilmente reversível para quem tem a chave, o que significa que quem a possuir pode obter os identificadores iniciais ao decifrar o pseudónimo. Respeita as propriedades D1 e D2 desde que, para além do controlador e processador, mas nenhum terceiro tenha acesso à chave e que sejam usados algoritmos ‘state-of-the art’ com um tamanho de chave grande o suficiente (256 bits é apropriado).

Esta técnica pode ser empregue em casos onde seja necessário fazer ‘tracking’ de indivíduos e onde também seja necessário reidentificar os indivíduos.

#### Encriptação Assimétrica

Para estes algoritmos assegurarem a propriedade de ciphertext indistinguishability podem introduzir aleatoriedade no processo de encriptação, o que lhes confere uma natureza probabilística. Isto significa que para um identificador é possível gerar vários pseudónimos diferentes com a mesma chave pública.

Assim, este tipo de encriptação pode ser utilizado em casos onde é desejável que para um mesmo utilizador sejam gerados pseudónimos diferentes de cada vez ou em casos em que quem faz o processo de pseudonimização (utiliza a chave pública) não é quem faz o processo de reidentificação (utilizando a chave privada). Esta é também ideal para situações onde não é necessário fazer ‘tracking’ mas é necessário ser possível fazer reidentificação.

### Other cryptography-based techniques

A combinação de vários esquemas de encriptação, quando feita de forma apropriada, pode conduzir à criação de técnicas robustas de pseudonimização. Como exemplo temos Polymorphic Encryption and Pseudonimização (PEP), que é uma técnica que pode ser utilizada em casos nos quais o utilizador precise de ter pseudónimos diferentes em domínios diferentes. Para ilustrar, é como se um paciente tivesse um pseudónimo diferente para cada médico, ou para outras entidades.

Existem também técnicas descentralizadas para pseudonimização que permitem aos utilizadores gerarem e guardarem consigo os seus pseudónimos para casos em que o controlador não deve ter conhecimento da identidade dos utilizadores, a não ser que estes queiram provar a sua identidade. Contudo, esta abordagem apresenta os seus próprios desafios, tais como certificar que não são gerados pseudónimos repetidos.

### Tokenisation
Nesta técnica os identificadores são substituídos por valores gerados aleatoriamente - tokens - onde não existe qualquer relação matemática entre o identificador e o pseudónimo. Desta maneira, ter posse de um token torna-se inútil para todos, exceto o controlador e o processador, que têm acesso ao mapping dos tokens com os identificadores.

Desta maneira, esta técnica assegura as propriedades D1 e D2.
### Outras abordagens

Masking tenta esconder parte de um identificador com caracteres aleatórios ou outros dados. Esta abordagem não assegura o cumprimento das propriedades D1 e D2, e para além disso se não fôr implementada cuidadosamente pode atribuir o mesmo pseudónimo a utilizadores diferentes. Scrambling refere-se a técnicas que misturem ou ofusquem caracteres. O processo pode ser reversível, dependendo da técnica escolhida. Este tipo de técnicas também não asseguram as propriedades D1 e D2. Blurring é uma técnica que tenta utilizar valores aproximados dos dados para reduzir a precisão de dados, reduzindo assim a possibilidade de identificação. Esta técnica pode ser usada em imagens, mas técnicas de reconhecimento de imagens baseadas em redes neuronais podem conseguir recuperar informação a partir destas imagens.


## Pergunta 1.2

Nesta resposta, irá ser analizado o caso de uso sobre gestão de salários. 

Este caso consiste na avaliação de segurança do processamento de dados dos funcionários de uma PME, aquando do pagamento de salários, segurança social e benefícios aos funcionários. Os dados processados nos processos enumerados anteriormente variam desde o nome, contactos, morada, NIF, NSS, a salário e posição na empresa. Todo este processo é realizado pelos RH, sendo no final de cada mês enviado, para a Segurança Social e instituições financeiras, declarações sobre cada funcionário. Neste caso, apesar de existir uma política de uso em prática, não existe nenhuma política sobre armazenamento e retenção de dados. Apesar de existirem cláusulas de confidencialidade entre os RH e os funcionários, os RH não possuem qualquer treino relativo a proteção de dados.

* ##### Avaliação de Impacto

  Neste capítulo é discutido o impacto nos direitos e liberdades dos funcionários, no caso de perda de segurança nos dados pessoais dos mesmos. O documento *Handbook on Security of Personal Data Processing* avalia o impacto em quatro níveis, baixo, médio, alto e muito alto, definidos na tabela 1 do documento *Handbook on Security of Personal Data Processing*mento.

  Em relação ao caso de uso, foram feitas as seguintes análises utilizando os critérios referidos anteriormente.

    * Perda de Confidencialidade
    
      O impacto na confidencialidade aquando uma perda de segurança neste caso de uso, encontra-se na sua maioria relacionada com o facto de divulgação a terceiros de informações como salários, entre outros, o que pode gerar desconforto nos funcionários, ou até mesmo fazer com que se tornem alvos para roubos. Assim sendo, o impacto da perda de confidencialidade foi classificado como médio.

    * Perda de Integridade e Disponibilidade
    
      O impacto da perda de integridade e disponibilidade foi classicado como baixo, pois os problemas resultantes destas perdas, atraso no pagamento de salários ou a necessidade de ressubmissão de informação, seriam de fácil resolução.

  Assim sendo, tendo em conta as classificações referidas em cima, o impacto geral no caso de perda de segurança dos dados pessoais foi definido como médio, pois foi a classificação mais alta obtida foi média.

* ##### Probabilidade de ocorrência de ameaças

  Neste capítulo discute-se as possíveis ameaças, e as suas probabilidades de ocorrência, no ambiente de processamento de dados pessoais. O documento, com o intuito de simplificar este processo, definiu quatro áreas a serem avaliadas nesta análise, sendo necessário responder com sim/não a cinco perguntas por área. Consoante o número de respostas sim, é atribuído um nível de probabilidade de ocorrência, variando de nível baixo a alto. As áreas e níveis de probabilidade de ocorrência são os seguintes:

    * Rede e Recursos Técnicos (*hardware* e *software*)

      Nesta área, e assumindo que estão a ser utilizadas as melhores práticas para prevenir acesso não autorizado aos dados, o nível de probabilidade de ocorrência de ameaça é baixo. A atribuição de nível baixo deve-se ao facto de o processamento de dados não ocorrer na internet, e também ao facto de o sistema se encontrar isolado de outros sistemas da PME.

    * Processos/procedimentos relacionados com a operação de processamento dos dados

      Também nesta área foi atribuido o nível baixo, devido ao facto de o processamento de dados pessoais estar limitado à organização e de serem criados registos de qualquer processamento. Foi considerado que as funções e responsabilidades dos funcionários dos RH estão definidas tendo em conta uma política de uso aceitável.

    * Diferentes entidades e pessoas envolvidas na operação de processamento dos dados
    
      Já nesta área, foi atribuído o nível médio, pois o processamento dos dados envolve vários funcionários, e é assumido que alguns destes não possuem qualquer treino relativo a proteção de dados.

    * Setor empresarial e escala do processamento
    
      Por fim, foi atribuido um nível de probabilidade de ocorrência baixo, pois não são conhecidas falhas anteriores e o setor de negócio da PME não é conseiderado como um alvo para *cyberattacks*.
  
  Assim sendo, tendo em conta a seção 2.1.3 do documento *Handbook on Security of Personal Data Processing* , a probabilidade geral de ocorrência de ameaças é 5, o que equivale a um nível baixo.

* ##### Avaliação de Risco

  Usando as secções anteriores, e tendo em conta a secção 2.1.4 do documento *Handbook on Security of Personal Data Processing*, o risco geral para este caso é médio. Através deste nível é possível recorrendo aos anexos, A1 e A2, do documento *Handbook on Security of Personal Data Processing* adotar medidas apropriadas para combater o risco obtido.

* ##### Medidas de Segurança

  Tendo em conta os anexos A1 e A2, as medidas de segurança que deveriam ser tomadas de modo a diminuir/mitigar o risco encontrado são as seguintes:

    * A.2;
    * A.3;
    * B.1;
    * G.3;
    * J.2;
    * I.2;
    * F.3;
    * F.4;
    * G.2;
