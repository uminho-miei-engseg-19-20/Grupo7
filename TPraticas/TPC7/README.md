# TPC7 - Aula9
## Pergunta P1.1

Numa execução "normal" os programas pedem que lhes seja dado um número que corresponde à quantidade de inteiros que vamos colocar no array *tests* que tem tamanho 10. Assim, será iniciado um ciclo *for* que terá tantas iterações quantas indicadas anteriormente, e em cada iteração será pedido mais um número que será colocado no em *tests*.

No entanto, podem ser observados também os comportamentos seguintes:

- Caso seja introduzido um número negativo para ser utilizado no ciclo *for*:
  - **Python** - O programa não entra no ciclo;
  - **Java** - O programa não entra no ciclo;
  - **C++** - O programa não entra no ciclo.
  
Não entram no ciclo *for* pois se o número dado fôr negativo não é cumprida a condição de execução do ciclo.

- Caso seja introduzido um número (não muito elevado) acima de 10 para ser utilizado no ciclo *for*: 
  - **Python** - Ocorre o erro `IndexError: list assignment index out of range` ao tentar colocar o 11º inteiro no array;
  - **Java** - Ocorre a exceção `Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10` após a introdução do 10º número;
  - **C++** - Faz mais pedidos de números, o que resulta num *overflow* do *buffer* que permite, por exemplo, modificar o valor da variável *test*.
  
Podemos assumir que Python e Java verificam se estão a escrever em endereços válidos dos arrays, enquanto em C++ isso não é verificado.
  
- Caso seja introduzido um número muito elevado para ser utilizado no ciclo *for*:
  - **Python** - Ocorre `OverflowError: range() result has too many items`;
  - **Java** - Ocorre uma exceção `Exception in thread "main" java.util.InputMismatchException: For input string: "111111111111"`;
  - **C++** - Resulta em pedidos infinitos de números sem esperar por qualquer resposta, possivelmente devido ao *overflow* da variável onde o número será guardado.

- Caso seja introduzido um número com mais de 10 dígitos para ser colocado no *buffer*:
  - **Python** - Não ocorre nenhum erro ou exceção;
  - **Java** - Ocorre uma exceção `Exception in thread "main" java.util.InputMismatchException: For input string: "111111111111"`;
  - **C++** - Continua com a pedir números, mas não espera por resposta e executa o resto do programa.
  
- É também de notar que é possível executar uma função dada como *input** no primeiro pedido de *input* da versão do código em Python.

## Pergunta P1.2

#### RootExploit.c

Neste programa as variáveis *pass* (que controla o acesso às permissões root) e *buf* são declaradas uma após a outra, logo é de esperar que se encontrem próximas na stack.

Assim sendo, ao causar um *buffer overflow* em *buff* quando é chamada a função *gets*, podemos alterar o valor de *pass*, o que nos dará permissões root. Isto é possível pois a função *gets* não é uma função segura, visto que apenas copia o *input* do utilizador para o *buffer* indicado sem qualquer tipo de verificação.

(Ao verificar os endereços das variàveis podemos verificar que apenas se encontram a 5 bytes de distância, ou seja, basta copiar 5 caracteres para *buff* através da função *gets* de forma a cumprir o nosso objetivo.

#### 0-simple.c

Podemos alterar o valor de *control* neste programa usando os mesmos princípios do anterior. Como o inteiro *control* e o array *buffer* são declarados um após o outro podemos assumir que estes se encontram próximos.

Ao verificar os endereços das duas variáveis ficámos a saber que apenas estão separadas por 76 bytes, sendo o que forem copiados 77 caracteres para *buffer* já é possível alterar o valor de *control* devido a *overflow*.

## Pergunta P1.3

Podemos concluir que este programa toma alguns cuidados no que toca ao *input* de dados do parte do utilizador, visto que utiliza *fgets* em vez de *gets*, o que permite validar o tamanho do conteúdo a ser passado para *buf*. 

No entanto não existe controlo dos limites daquilo que é lido no final do programa, sendo que é possível aceder a informação que se encontra para além dos limites de *buf*. Para o fazer basta dar a *len* um tamanho superior a 100 quando é pedido. Para além disso é possível ver parte do texto passado para *buf* em tentativas de correr o código anteriores pois *buf* nunca é limpo.

## Pergunta P1.4

Tendo em conta a estrutura do programa sabemos que o as variáveis *control* e *buffer* vão estar próximas na stack. Como temos acesso ao código fonte podemos modificá-lo para imprimir os endereços das variáveis, ou alternativamente, pode ser utilizado um *debugger* para o mesmo efeito. Após isto pudemos observar que os enderços de *control* e *buffer* eram 0x7fffffffe12c e 0x7fffffffe0e0 respetivamente, o que resulta numa diferença de 76 quando convertido para decimal. Assim, é possível modificar a variável *control* como demonstrado no exemplo seguinte: 

```
user@CSI:~/Desktop/Aula9$ ./1-match iiiiiiiiixiiiiiiiiixiiiiiiiiixiiiiiiiiixiiiiiiiiixiiiiiiiiixiiiiiiiiixiiiiiidcba
You win this game if you can change variable control to the value 0x61626364'
Congratulations, you win!!! You correctly got the variable to the right value
```

São usados como argumentos 76 caracteres com a adição de "dcba" no final, sendo que estes últimos quatro são utilizados pois o seus códigos ASCII em hexadecimal são 64, 63, 62 e 61 respetivamente, mas são colocados nesta ordem pois o sistema UNIX é little-endian.

## Pergunta 1.5

Para mitigar as vulnerabilidades foram utilizadas as seguintes técnicas de programação defensiva:
- Utilizar a função strncpy ao invés da strcpy, pois oferece maior controlo sobre o tamanho de caracteres a copiar;
- Verificar qual a memória necessária para armazenar argc[1] e a string laranja, e alocar na memória esses tamanhos exatos;
- É tambem verificado se são fornecidos os inputs necessários ao correto funcionamento da função.
 
## Pergunta 1.6

As técnicas de programação defensiva utilizada foram as seguintes:
- Utilizar a função strncpy ao invés da strcpy, pois oferece maior controlo sobre o tamanho de caracteres a copiar;
- Em bof, verificar qual a memória necessária para armazenar str, e alocar buffer com esse tamanho exato;
- Fazer a verificação da existência do ficheiro badfile, antes de aceder ao mesmo.
