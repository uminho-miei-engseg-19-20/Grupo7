# TPC6 - Aula 7

## Pergunta P1.1	

### \#1: CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer

Esta Weakness ocorre pois certas linguagens de programação, como C e C++ (e consequentemente Assembly), permitem endereçamento direto de memória quando se trabalha com buffers sem verificar que o local ao qual se está a tentar aceder é válido para o buffer que está a ser referenciado, o que pode conduzir a operações de leitura ou escrita serem efetuadas noutras partes da memória. Isso pode levar a que seja executado código arbitrário, seja alterado o fluxo do código, seja revelada informação sensível ou causar o crash do sistema.

**Consequências comuns:**

Este tipo de Weakness pode ter 3 tipos principais de consequências.

- No caso de ocorrer uma leitura out-of-bounds é possível que seja acedida informações sensíveis que podem ser utilizados para levar a cabo mais ataques com consequências mais severas. 

```
Área(s) de segurança impactada(s): Confidencialidade
Impacto: Leitura de memória
```

- Um acesso à memória out-of-bounds pode resultar em corrupção de memória ou instruções, podendo resultar num crash ou outros tipos de DoS como correr em loop infinito, o que pode levar ao elevado consumo de recursos do sistema.

```
Área(s) de segurança impactada(s): Confidencialidade, Disponibilidade
Impacto: Leitura de memória; DoS: Crash, Exit, Restart; DoS: Consumo de recursos (CPU ou Memória)
```
- Caso a memória acessível ao atacante possa ser efetivamente controlada pode ser possível executar código arbitrário. No caso do atacante conseguir reescrever na memória o equivalente a um apontador (32 a 65 bits) este pode modificar o function pointer para apontar para o seu próprio código malicioso. No caso de poder apenas modificar um único byte, execução de código arbitrário pode ser possível, podendo explorar esta tática várias vezes para obter anteriores. Mesmo não o repetindo o atacante pode modificar dados críticos para a segurança da aplicação, como flags que lhe podem conferir o estatuto de administrador.

```
Área(s) de segurança impactada(s): Confidencialidade, Disponibilidade, Integridade
Impacto: Execução de código ou comandos não autorizada; Modificação de memória
```

### \#2: CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

XSS (Cross-Site Scripting) é uma Weakness prevalente em tecnologias Web Based que ocorre quando um website é gerado dinâmicamente utilizando input de utilizadores que contém um script malicoso e este input não é sanitized. Assim, quando o browser gera a página web, o script malicoso que foi injetado através do input anteriormente referido é executado no contexto do domínio do servidor web.

Existem três tipos de XSS:
- Tipo 1: Reflecetd XSS - O servidor lê a informação diretamente do Http Request e refelte-a de volta na Http Response na forma de uma mensagem de erro, os resultados de uma pesquisa ou qualquer outro tipo de resposta que inclua uma parte ou a totalidade do input. Um exemplo ilustrativo deste tipo de XSS consiste em fazer o utilizador aceder a um URL criado pelo atacante que leve a um website vulneráve. Para além disso, o conteúdo contido no URL deve ser utilizado para gerar a página. Ao carregar no link o utilizador faz um Http Request com dados que serão refletidos de volta para si e, assim, ao gerar a página web, o browser executa o script injetado pelo atacante no conteúdo. Este script pode remeter o browser a uma página controlada pelo atacante que desta maneira rouba as cookie/tokens de autenticação do utilizador.
- Tipo 2: Stored XSS - Um script injetado é guardado juntamente com o conteúdo numa base de dados, ou num fórum de mensagens ou qualquer outra data store de confiança. Deste modo, quando o utilizador acede a uma página que peça esse conteúdo e o utilize como conteúdo dinâmico o script injetado é executado.
- Tipo 0: DOM-Based XSS - Neste tipo de XSS o scrip malicioso não é injetado a partir da Http Response, é injetado a partir de uma fonte que pode ser controlada pelo atacante (ex.: URL) para o ambiente DOM. Desta maneira a página (Http Request) não muda. O que muda é o código client-side, devido às alterações malicosas que ocorreram no ambiente DOM. 

**Consequências comuns:**

- O tipo mais comum de consequência é a injeção de um script que será corrido pelo browser para o roubo de cookies. Como o website que está a pedir para ser corrido o script tem acesso às suas cookies, o cript também tem e pode enviá-las para o atacante.

```
Área(s) de segurança impactada(s): Controlo de Acesso, Confidencialidade
Impacto: Bypass de Mecanismos de Proteção; Leitura de Dados da Aplicação
```

- Em algumas instâncias, e em conjunto com outras falhas, é possível correr código arbitrário no computador da vítima.

```
Área(s) de segurança impactada(s): Integridade, Confidencialidade, Disponibilidade
Impacto: Execução de código ou comandos não autorizada
```

- XSS pode causar vários problemas com diferentes graus de severidade. Após injetado, um script pode servir para realizar vários tipos de atos maliciosos. Entre outras coisas, pode ser utilizado para roubar as cookies de sessão de um utilizador e fazer hijack da sua sessão, como foi referido anteriormente, e se esse utilizador possuir privilégios de administrador, a sua sessão pode ser usada para causar danos ao website em causa.

```
Área(s) de segurança impactada(s): Integridade, Confidencialidade, Disponibilidade, Controlo de Acesso
Impacto: Execução de código ou comandos não autorizada; Bypass de Mecanismos de Proteção; Leitura de Dados da Aplicação
```

### \#3: CWE-20: Improper Input Validation

Improper Input Validation acontece quando uma aplicação não valida devidamente o input recebido antes de o usar. Isto permite a um atacante criar um tipo input que o programa não está à espera, o que pode levar à alteração do fluxo do código, execução arbitrária de código ou controlo arbitrário de recursos.

Este tipo de Weakness pode ser introduzido devido à falta de cuidado na fase de design da aplicação e arquitetura ou na fase de implementação.

**Consequências comuns:**

- Um atacante pode fornecer valores inesperados ao programa, fazendo-o crashar ou consumir recursos em excesso, como CPU ou memória.

```
Área(s) de segurança impactada(s): Disponibilidade
Impacto: DoS: Crash, Exit, Restart; DoS: Consumo de recursos (CPU ou Memória)
```

- Se um atacante conseuir controlar as referências a recursos, este pode ler dados confidenciais.

```
Área(s) de segurança impactada(s): Confidencialidade
Impacto: Leitura de Memória; Leitura de Ficheiros ou Diretorias
```

- Um atacante pode introduzir input malicioso para modificar dados ou alterar o fluxo de controlo de maneira inesperada, causando a execução arbitrária de comandos.

```
Área(s) de segurança impactada(s): Integridade, Confidencialidade, Disponibilidade
Impacto: Modificação de Memória; Execução de código ou comandos não autorizada
```

### \#10: CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

De forma geral, operações com ficheiros devem ser feitas dentro de uma diretoria restrita, mas quando esta Weakness existe, através do uso de input externo que não é devidamente tratado, é possível construir um pathname que conduza fora da diretoria restrita na qual devia operar. Na maior parte dos casos, no input são utilizados caracteres especiais como ".." e "/".

**Consequências comuns:**

- O atacante pode criar ou alterar o ficheiros críticos como bibliotecas, programas, ou outros ficheiros importantes. Se o ficheiro visado for utilizado num mecanismo de segurança pode ser possível fazer bypass desse mecanismo.

```
Área(s) de segurança impactada(s): Integridade
Impacto: Modificação de ficheiros ou diretorias
```

- O atacante pode conseguir lêr o conteúdo de ficheiros inesperados e expôr informação sensível. Se o ficheiro visado for utilizado num mecanismo de segurança, este pode ser bypassed (ex.: se o atacante tiver lido um ficheiro de passwords pode utilizá-las para fazer bypass do mecanismo de segurança utilizando força bruta até chegar à password correta).

```
Área(s) de segurança impactada(s): Confidencialidade
Impacto: Leitura de ficheiros ou diretorias
```

- O atacante pode conseguir alterar, apagar ou corromper ficheiros críticos como programas, bibliotecas ou outros ficheiros importantes, o que pode impedir o funcionameto do sofware. No caso de mecanismos como os de autenticação existe o potencial para bloquear o acesso a todos os utilizadores do software.

```
Área(s) de segurança impactada(s): Disponibilidade
Impacto: DoS: Crash, Exit; Restart
```

- O atacante pode criar ou alterar o ficheiros críticos utilizados na execução de código, como bibliotecas ou programas.

```
Área(s) de segurança impactada(s): Integridade, Confidencialidade, Disponibilidade
Impacto: Execução de código ou comandos não autorizada
```

**Exemplo de código:**

O exemplo seguinte está escrito em Java:

```
String filename = System.getProperty("com.domain.application.dictionaryFile");
File dictionaryFile = new File(filename);
```

Neste exemplo, o path para o `dictionaryFile` é lido de uma propriedade do sistema e utilizado para inicializar um objeto `File`. No entanto, este path não é validado ou modificado para impedir que este contenha sequências de path relativo ou absoluto antes de criar o ficheiro. Desta forma, qualquer um que consiga controlar a propriedade do sistema utilizada consegue controlar que ficheiro é utilizado.

**CVE-2018-20250**

Este vulnerabilidade afeta todas as versões anteriores à, e incluindo, 5.61. do WinRar e é descrita como uma vulnerabilidade de Absolute Path Traversal - CWE-36 que é derivada da CWE-22. De forma a sermos mais claros a vulnerabilidade será explicada em conjunto com um exploit.

Para fazer o parsing de arquivos ACE, o WinRAR utiliza um dll (DynamicLink Library) chamado unacev2.dll. Este dll foi compilado em 2006 e possui um bug que faz com que o path relativo ao arquivo (diretoria para a qualserá efetuada a extração) seja tratado como um path absoluto, causando a vulnerabilidade referida. 

Para o processo de extração de um arquivo, o dll invoca uma função chamada `GetDevicePathLen`, que verifica se o dispositivo ou nome da drive aparece no path. Se o resultado da chamada desta função fôr inferior a 0 (não tem o nome de nenhuma drive ou dispositivo, ou seja, a função assume que o path que recebeu não é o completo) ocorreria `sprintf(final\_file\_path,"\%s\%s",destination\_folder,file\_relative\_path)`. No entanto, se o resultado dessa chamada fôr superior a 0 (a função assume que recebeu o path completo) resultará em `sprintf(final_file_path, "%s%s",””, file_relative_path)`, ou seja: em vez de concatenar o path absoluto com o relativo irá substituir o path absoluto por ` ̈ ̈  `, que será concatenado ao path relativo. Isto permite que o caminho para onde ocorrerá a extração possa ser qualquer coisa que seja posta como path relativo. 

No entanto, antes de chegar a esta parte da extração e poder explorar esta vulnerabilidade é necessário passar por mais uma função "filtro", (que é do próprio WinRAR e não do dll) chamada `CleanPath`. Esta função omite sequências que permitam Path Traversal, como `\..\` e `C:\`, `C:` (e `C:\C:` por razões desconhecidas). 

Para explorar este bug é necessário passar por ambas as funções "filtro". Vale a pena recordar que primeiro é necessário passar pela função `CleanPath` e depois pela `GetDevicePathLen`. 

Com base na informação apresentada até agora é possível criar um ar-quivo ACE (terá de ter a extensão .rar mas será tratado como ACE pelo WinRAR porque será identificado como tal pelos seus magic bytes) cujo path relativo consiga passar pelas duas funções "filtro" e explorar a vulnerabilidade. 

O exploit disponível online usa `C:\C:C:../AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup\some\_file.exe` como path relativo. Este path, depois de `CleanPath`, torna-se `C:../AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup\some\_file.exe`. Depois disto, a função `GetDevicePathLen` possuirá um valor de retorno maior que 0 o que executará `sprintf(final_file_path, "%s%s", ””, file_relative_path` e fará com que o path relativo seja tratado como path absoluto. 

No entanto, porquê este path?  Porque se o nosso objetivo é executar código na máquina que estamos a atacar uma das nossas melhores opções é extrair o arquivo malicioso para a pasta Startup, pois todo o código que está nesta pasta é executado no Startup da máquina (no caso Windows). O único senão é que podemos não saber o nome do utilizador que vai ser vítima deste exploit. 

Para dar a volta a isto, em vez de tentar adivinhar o nome, utilizamos `C:../AppData/...` onde `C:` é interpretado como a diretoria atual do arquivo (que só é a da pasta onde o arquivo está se este fôr extraído através da opção apresentada quando se clica no ícone do arquivo com o botão direito do rato) e `../` funciona quando o arquivo é extraído de `C:\Users\<username>\Downloads` ou `C:\Users\<user name>\Desktop`, por exemplo, pois volta para a pasta com o nome do utilizador, o que nos permite continuar para a pasta Startup. 

Assim, após extrair o arquivo malicioso, o código que o atacante quiser fica à espera na pasta Startup para ser corrido da próxima vez que a máquina seja iniciada.

## Pergunta 1.2

Tendo em conta, que se estima, que por cada 1000 SLOC existam uma média de 5 a 50 *bugs* num pacote de *software*, é possível estimar que existam:
  
  * Facebook - Entre 0.31 a 3.1 milhões de *bugs*;
  * *Software* de Automóveis - Entre 0.5 a 5 milhões de *bugs;
  * Linux 3.1 - Entre 75 a 750 mil *bugs*;
  * Serviços Internet Google - Entre 0.5 a 5 milhões de *bugs*.

No entanto, é impossível, a partir do número de *bugs* de um determinado *software*, estimar o número de vulnerabilidades do mesmo.

## Pergunta 1.3

Vulnerabilidade de projeto:
  
  * CWE-352 (*Cross-Site Request Forgery) - Uma aplicação não verifica, ou não possui os meios para verificar, se um pedido é válido e bem formado, de modo a evitar que atacantes usem esta vulnerabilidade para roubar informação ou até mesmo executar código malicioso. Para mitigar este tipo de vulnerabilidades, basta durante o processo de desenho do sistema, garantir que o mesmo vai possuir meios para validar pedidos.

  * CWE-798 (*Use of Hard-coded Credentials*) - Se um *software* possuir, e utilizar, credenciais criptográficas *hard-coded*, está a criar um enorme buraco na sua segurança, buraco esse que pode facilmente ser explorado por atacantes. Para mitigar esta vulnerabilidade, basta garantir durante o desenho da arquitectura do sistema, que o mesmo não utilize credenciais criptográficas *hard-coded*.

Vulnerabilidade de codificação:

  * CWE-20 (*Improper Input Validation*) - O *software* não valida corretamente *input*, o que pode levar a que atacantes criem *inputs* não expectáveis pelo sistema, o que pode originar com o mesmo deixe de funcionar corretamente, pondo em causa a segurança do sistema. Para mitigar este tipo de vulnerabilidades basta fazer uma validação correta dos *inputs*.

  * CWE-125 (*Out-of-bounds Read*) - O *software* lê informação fora das áreas de memória onde uma dada leitura deveria acontecer, permitindo assim que atacantes leiam informação sensível. Um exemplo famoso deste tipo de vulnerabilidade é o *heartbleed bug*. Para mitigar este tipo de vulnerabilidade basta garantir que aquando de uma leitura da memória, esta se realize no local correto.

Vulnerabilidade operacional:
  
  * CWE-400 (*Uncontrolled Resource Consumption*) - Se o *software* não gerir corretamente os recursos limitados que possui, pode levar a atacantes esgotem intencionalmente esses recursos de modo a afetar o bom funcionamento do *software*. Para mitigar, basta implementar uma boa gestão dos recursos utilizados pelo *software*.

  * CWE-269 (*Improper Privilege Management*) - Se um *software* não gerir corretamente as permissões dos seus atores, pode originar situações em que atores possam possuir permissões para aceder a partes do sistema às quais não deveriam ter acesso. Para mitigar este problema, basta criar um sistema de controlo de acessos que faça a correta gestão de todos os utilizadores do sistema.



## Pergunta 1.4

Uma vulnerabilidade dia-zero consiste numa vulnerabilidade que ainda não é conhecida pelas equipas de desenvolvimento de um determinado *software*. Devido a isto, são muito perigosas para os sistemas que as possuem, pois são pontos de entrada para os mesmos.

Já vulnerabilidades não dia-zero, consistem em vulnerabilidades conhecidas, e possivelmente corrigidas, pelas equipas de desenvolvimento, e encontram-se publicadas em base de dados de vulverabilidades.
