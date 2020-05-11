# TPC9 - Aula11

## Pergunta P1.1

### 1. Existem pelo menos dois tipos de vulnerabilidades estudadas na aula teórica de "Validação de Input" que podem ser exploradas. Identifique-as.

A primeira vulnerabilidade identificada está na utilização da função *system* sem validação do *input* utilizado, o que permite a posterior execução de vários comandos para além do *file* através da injeção de separadores.

Para além disso, existe a possibilidade de explorar a vulnerabilidade de *path traversal*.

Não valida se é executado mais do que apenas o comando file (ex.: `./filetype filetype.c ; ls -l` mas em vez de `ls -l` modificar um ficheiro, por exemplo).

### 2. Forneça o código/passos/linha de comando que permitem explorar cada uma das vulnerabilidades identificadas na linha anterior.

Para explorar a primeira vulnerabilidade basta executar o programa da seguinte maneira: `./filetype ficheiro; comando_malicioso; ...`. Desta forma o `comando_malicioso` é executado após a execução do comando `file ficheiro`.

Para a segunda vulnerabilidade basta escrever um *path* no input do programa.

### 3. O que aconteceria se o seu programa tivesse permissões setuid root?

Caso o programa tivesse essas permissões poderia executar qualquer comando que quisesse e aceder ou alterar dados aos quais normalmente não deveria ter acesso, o que comprometeria severamente todo o sistema onde o programa fosse executado.

## Pergunta P1.2

A resolução deste execrcício encontra-se no ficheiro P1.2.py
